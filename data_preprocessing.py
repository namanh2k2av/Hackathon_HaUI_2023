
import numpy as np
import os
from PIL import Image


idx_file = 0
idx_person = 0
FILE = []


PATH = 'PETA dataset/'
OUT_PATH = 'data/'
LABELS = dict()
def execute_label_file(data):

  label = dict()

  for i in data:
    #print(i.split(" ")[0])
    id = i.split(" ")[0].split(".")[0]
    id = int(id)
    temp = ['0'] * 6
    ix = i.find('Male')
    if ix != -1:
      temp[0] = '1'

    if i.find('personalLess15') > 0:
      temp[1] = '1'
    if i.find('personalLess30') > 0:
      temp[2] = '1'
    if i.find('personalLess45') > 0:
      temp[3] = '1'
    if i.find('personalLess60') > 0:
      temp[4] = '1'
    if i.find('personalLarger60') > 0:
      temp[5] = '1'
    #print(temp)
    label[id] = temp
    #print(label[id])
  return  label


def rename_image(path, name, out_path='data/'):
  img = Image.open(path)
  img.save(out_path + name, 'jpeg')


def write_file(label_dict, path):
  global FILE
  global idx_file
  for file in os.listdir(path):
    if not file.endswith('.txt'):
      idx_file += 1
      id_string = file.split("_")[0].split('.')[0]
      id = int(id_string)

      #print(label_dict[id_string])
      name = f'img{idx_file}.jpg'
      label = label_dict[id]
      label_string = ','.join(label)
      FILE.append(f'{name}\t{label_string}\n')

      rename_image(path + file, name)


for sub_path in os.listdir(PATH):
  print(sub_path)
  data = []
  label_path = PATH + sub_path + '/archive/Label.txt'
  path = PATH + sub_path + '/archive/'
  with open(label_path) as f:
    data = f.readlines()
    #print(len(data))
  try:
    label_dict = execute_label_file(data)
  except:
    print(path)
    raise Exception('label exception')

  #print(label_dict)
  write_file(label_dict, path)
  #input("dadsad")


with open('data/Label.txt', "w") as f:
  for line in FILE:
    f.write(line)



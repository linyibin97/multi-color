import argparse
from PIL import Image
import os
import matplotlib.pyplot as plt

def get_imgs(img_dir):
  imgs = []
  for root, _, files in os.walk(img_dir):
      for file in files:
          ftype = os.path.splitext(file)[-1]
          ftype = ftype.upper()
          if (ftype in ['.JPG', '.JPEG', '.PNG', '.BMP']):
              imgs.append(os.path.join(root, file))
  return sorted(imgs)

def process_img(input_path='', output_path='', size=64):
    if (output_path == '' or input_path==''): 
        return
    o_img = Image.open(input_path).convert('RGB').resize((size, size))
    o_img.save(output_path)

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', type=str, default='')
parser.add_argument('--output_dir', type=str, default='')
parser.add_argument('--size', type=int, default=64)
args = parser.parse_args()

size = args.size
imgs = get_imgs(args.input_dir)

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

for i in imgs:
    [img_name, ext] = os.path.splitext(os.path.split(i)[1])
    y = os.path.join(args.output_dir, img_name+'.jpg')
    process_img(i, y, size)
    print(img_name)

'''
python data_preprocessor.py --input_dir D:/anime_face_mini/origin_train --output_dir ./data/anime_face/train
python data_preprocessor.py --input_dir D:/anime_face_mini/origin_val --output_dir ./data/anime_face/val
'''
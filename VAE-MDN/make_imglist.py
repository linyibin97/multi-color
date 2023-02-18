import glob
import os

dataset_path = "D:\\Exp-Chapter4\\code\\03_multi-color\\VAE-MDN\\data\\anime_face_mini"
imglist_dir = "D:\\Exp-Chapter4\\code\\03_multi-color\\VAE-MDN\\data\\imglist\\anime_face_mini"

train_set_path = os.path.join(dataset_path, 'origin_train')
val_set_path = os.path.join(dataset_path, 'origin_val')

# print(train_set_path, val_set_path)

train_imgs = glob.glob(os.path.join(train_set_path, "*.jpg"))
val_imgs = glob.glob(os.path.join(val_set_path, "*.jpg"))

# print(train_imgs)
# print(val_imgs)

if (not os.path.exists(imglist_dir)): os.makedirs(imglist_dir)

list_train = os.path.join(imglist_dir, "list.train.vae.txt")
list_test = os.path.join(imglist_dir, "list.test.vae.txt")

with open(list_train, 'w') as f:
    for i in train_imgs:
        f.write(i+'\n')

with open(list_test, 'w') as f:
    for i in val_imgs:
        f.write(i+'\n')
#### TF v1 安装

```shell
 conda create --name tfv1 python=3.6
 conda activate tfv1
 conda search cudatoolkit
 conda install cudatoolkit=10.0.130
 conda search cudnn
 conda install cudnn=7.6.0
 conda search tensorflow-gpu
 conda install tensorflow-gpu=1.15.0 #或者 pip install tensorflow-gpu==1.15.0
 conda list

 pip install scipy==1.2.1
 pip install Pillow
 pip install matplotlib
```

#### 数据预处理

数据需要存放在 `\data` 目录下

```shell
python data_preprocessor.py --input_dir D:/anime_face_mini/origin_train --output_dir ./data/anime_face/train
python data_preprocessor.py --input_dir D:/anime_face_mini/origin_val --output_dir ./data/anime_face/val
```

#### 训练

```
cd wgan
python main_wgan.py --is_train=True --dataset anime_face --batch_size 36 --epoch 100
```

#### 测试

```
python main_wgan.py --is_train=False --dataset anime_face --batch_size 20
```

```
pytorch-fid D:\anime_face\origin_train D:\03_multi-color\cGAN\wgan\result\output\anime_face\0
```


| fid  | origin_val         | origin_val_256     |
| ---- | ------------------ | ------------------ |
| 0    | 34.10574107950606  | 21.45601674407507  |
| 1    | 33.93370816267122  | 21.196651722634357 |
| 2    | 33.948674909414876 | 21.267042994124154 |
| 3    | 33.95643127518153  | 21.2141973955344   |
| 4    | 34.04906810376093  | 21.312313298005733 |
| 5    | 34.03348336667051  | 21.293916038801342 |


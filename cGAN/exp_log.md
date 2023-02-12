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
python main_wgan.py --is_train=True --dataset anime_face
```


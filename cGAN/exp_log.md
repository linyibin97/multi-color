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


data中的feats由zhang模型生成的

(1, 512, 28, 28) npz文件

通过`get_zhang_colorization.sh` 和 `third_party\save_zhang_feats.py` 处理

训练会生成 lv_color_train.mat

根据错误信息发现在 caffe 提供的 python/caffe/io.py 中，302行 skimage.io.imread() 调用参数 “as_grey” 实际应当修改为 “as_gray”，原因应该是 scikit-image 的 0.17.2 版本修改了参数名称。
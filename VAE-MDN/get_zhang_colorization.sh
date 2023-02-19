cd third_party
git clone -b caffe https://github.com/richzhang/colorization.git
rm -rf colorization/.git
cd colorization/
bash models/fetch_release_models.sh 

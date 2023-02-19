from third_party.save_zhang_feats import save_zhang_feats
import os

dataset = 'anime_face'

list_dir = os.path.join('data/imglist/', dataset)
feat_dir = os.path.join('data/featslist/', dataset)

train_img_fns = []
test_img_fns = []

with open(os.path.join(list_dir, 'list.train.vae.txt'), 'r') as ftr:
    for img_fn in ftr:
        train_img_fns.append(img_fn.strip('\n'))

with open(os.path.join(list_dir, 'list.test.vae.txt'), 'r') as fte:
    for img_fn in fte:
        test_img_fns.append(img_fn.strip('\n'))

train_feats_fns = save_zhang_feats(train_img_fns, ext='jpg')
test_feats_fns = save_zhang_feats(test_img_fns, ext='jpg')

if not os.path.exists(feat_dir): os.makedirs(feat_dir)

with open(os.path.join(feat_dir, 'list.train.txt'), 'w') as fp:
 for feats_fn in train_feats_fns:
   fp.write('%s\n' % feats_fn)

with open(os.path.join(feat_dir, 'list.test.txt'), 'w') as fp:
 for feats_fn in test_feats_fns:
   fp.write('%s\n' % feats_fn)
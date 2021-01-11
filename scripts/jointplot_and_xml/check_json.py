# -*- encoding:utf-8 -*-
import json
from collections import defaultdict

# 统计每张图的目标数量
# 统计目标大小
res = defaultdict(list)

json_path = './train_5k.json'
with open(json_path, 'r') as f:
    data = json.load(f)
    for ann in data['annotations']:
        # int
        image_id = ann['image_id']
        # list:[x, y, w, h]
        bbox = ann['bbox']
        res[image_id].append([bbox[2], bbox[3]])

    f.close()

with open('bbox.json', 'w') as f:
    json.dump(res, f, indent=2)
    f.close()


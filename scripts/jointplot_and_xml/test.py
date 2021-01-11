import json
from collections import defaultdict
import openpyxl
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np


def vis(ip):
    # plt.figure(figsize=(16, 10))
    # plt.figure()
    # plt.scatter(ip[:, 0], ip[:, 1], s=8, marker='o', c=np.mean(ip, axis=1), cmap='rainbow')
    # 构建数据
    width = ip[:, 0]
    height = ip[:, 1]
    ax = sns.jointplot(x=width, y=height, kind='hex', cmap='Oranges')
    # ax.set_axis_labels('width', 'height', fontsize=18)

    plt.xlabel('width', fontsize=18)
    plt.ylabel('height', fontsize=18)
    plt.tick_params(axis="both", labelsize=16)
    # plt.savefig('OUTPUT/op1.png', dpi=300)
    plt.show()


def write2xml(data_dict):
    wb = openpyxl.Workbook()
    # ws = wb.create_sheet("newsheet")
    ws = wb.active

    # tp = sorted(data_dict.items(), key=lambda x: x[0])

    ws.append(['w', 'h'])
    for _, value in data_dict.items():
        for exa in value:
            ws.append(exa)

    wb.save('stat-bbox.xlsx')


# key is object_num, value is image_num owning this object_num
statistic = defaultdict(int)
json_path = './bbox.json'
min_count = 2000
_min = 1000
_max = 0

with open(json_path, 'r') as f:
    data = json.load(f)
    bbox_list = []
    for key, value in data.items():
        for exa in value:
            _min = min(_min, exa[0], exa[1])
            _max = max(_max, exa[0], exa[1])
            if _max == 388:
                continue
            bbox_list.append(exa)

    print(_min, _max)
    vis(np.array(bbox_list[min_count:]))

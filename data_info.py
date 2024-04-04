"""
数据样本分析
画出数据量条形图
画出图像分辨率散点图
"""

import os
import PIL.Image as Image
import matplotlib.pyplot as plt
import numpy as np


def plot_resolution(dataset_root_path):
    img_size_list = []  # 承接所有图片的长宽数据
    for root, dirs, files in os.walk(dataset_root_path):
        for file_i in files:
            file_i_full_path = os.path.join(root, file_i)
            img_i = Image.open(file_i_full_path)
            img_i_size = img_i.size  # 获取单张图像的长宽
            img_size_list.append(img_i_size)

    print(img_size_list)  #

    width_list = [img_size_list[i][0] for i in range(len(img_size_list))]
    height_list = [img_size_list[i][1] for i in range(len(img_size_list))]

    # print(width_list)   # 640
    # print(height_list)    # 346

    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置中文字体
    plt.rcParams["font.size"] = 8
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

    plt.scatter(width_list, height_list, s=1)
    plt.xlabel("宽")
    plt.ylabel("高")
    plt.title("图像宽高分布")
    plt.show()


#   画出条形图
def plot_bar(dataset_root_path):
    file_name_list = []
    file_num_list = []
    for root, dirs, files in os.walk(dataset_root_path):
        if len(dirs) != 0:
            for dir_i in dirs:
                file_name_list.append(dir_i)
        file_num_list.append(len(files))

    file_num_list = file_num_list[1:]
    # 求均值，并把均值以横线形式显示出来
    mean = np.mean(file_num_list)
    print("mean = ", mean)

    bar_positions = np.arange(len(file_name_list))

    fig, ax = plt.subplots()  # 定义画的区间和子画
    ax.bar(bar_positions, file_num_list, 0.5)  # 画柱图，参数：柱间的距离，柱的值，柱的宽度

    ax.plot(bar_positions, [mean for i in bar_positions], color="red")  # 显示平均值

    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置中文字体
    plt.rcParams["font.size"] = 8
    plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

    ax.set_xticks(bar_positions)  # 设置x轴的刻度
    ax.set_xticklabels(file_name_list, rotation=90)  # 设置x轴的标签
    ax.set_ylabel("类别数量")
    ax.set_title("数据分布图")
    plt.show()


if __name__ == '__main__':
    dataset_root_path = "dataset"

    plot_resolution(dataset_root_path)

    # plot_bar(dataset_root_path)
"""
项目初始化
"""

import os


def create_folders():
    try:
        os.mkdir("output")
        os.mkdir("dataset")
        print("文件夹创建成功！")
    except FileExistsError:
        print("文件夹已存在。")


if __name__ == "__main__":
    create_folders()

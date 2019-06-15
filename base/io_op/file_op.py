import os
import shutil
import numpy as np


def file_remove_parent():
    path = "F:\\BaiduYunDownload\\QCon上海2017演讲幻灯片"
    file_cnt = 0
    for file_l1 in os.listdir(path):
        file_l1_path = os.path.join(path, file_l1)
        for file_l2 in os.listdir(file_l1_path):
            file_l2_path = os.path.join(file_l1_path, file_l2)
            for file_l3 in os.listdir(file_l2_path):
                file_l3_path = os.path.join(file_l2_path, file_l3)
                file_l3_new = os.path.join(path, file_l3)
                shutil.copy(file_l3_path, file_l3_new)
                print(file_l3_path)
                file_cnt += 1
    print("file_cnt: {}".format(file_cnt))


def file_rename():
    path = "F:\\BaiduYunDownload\\QCON\\QCon上海2017演讲幻灯片"
    for file in os.listdir(path):
        if "QCon上海2017-" in file:
            new_name = file.replace("QCon上海2017-", '')
            os.rename(os.path.join(path, file), os.path.join(path, new_name))


def file_name_match():
    path1 = "F:\\BaiduYunDownload\\QCon\\QCon-2016"
    path2 = "F:\\BaiduYunDownload\\QCon\\QCon-2016-上海"
    file2_set = set()
    for file2 in os.listdir(path2):
        file2_set.add(file2)
    print(len(file2_set))
    for file1 in os.listdir(path1):
        if np.any([file1.split("-")[0] in s for s in file2_set]):
            os.remove(os.path.join(path1, file1))
            print("file1 {} in file2".format(file1))
        else:
            print("file1 {} not in file2".format(file1))


if __name__ == '__main__':
    # file_remove_parent()
    # file_rename()
    file_name_match()
    pass



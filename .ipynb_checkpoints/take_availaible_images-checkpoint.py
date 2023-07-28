import os

lines = list()
with open("data/nuscenes_list/test.txt", "r") as f:
    lines = f.readlines()
with open("data/nuscenes_list/train.txt", "r") as f:
    lines = lines + f.readlines()

with open("data/nuscenes_list/new_test.txt", "w") as f:
    lst = os.listdir("../Datasets/v1.0-mini/v1.0-test/samples/LIDAR_TOP/")
    for name in lst:
        for ref_name in lines:
            if "samples/LIDAR_TOP/" + name == ref_name.split(" ")[0] or "samples/LIDAR_TOP/" + name == ref_name.split(" ")[1]:
                f.write(ref_name)

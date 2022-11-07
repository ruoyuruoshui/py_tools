# coding=UTF-8<code>
import shutil
import os

def read_map(path):

    map_file = open(path, 'r')
    lines = map_file.readlines()
  
    map = {}
    for line in lines:
        kv = line.split(":")
        k = kv[0].replace('"', '')
        splited_v = kv[1].split(".")
        v = splited_v[len(splited_v) - 1].strip()
        #name = v.replace('_', '')
        #print(k)
        map[v] = k
    return map 

def rename(path, to_path, map):
    if not os.path.exists(to_path):
        os.makedirs(to_path)
    for k, v in map.items():
        image = path + "/" + k + ".png"
        to_file = to_path + "/" + v + ".png"
        if not os.path.exists(image):
            #/Users/jiquan.chen/work/py_tools/shortcut/st_car/action_condition/action8.png
            print(image)
            continue
        shutil.copy(image, to_file)


def check_file(path, path_to_check):
    files = os.listdir(path)
    for file in  files:
        file_path = os.path.join(path_to_check, file)
        if not os.path.exists(file_path):
            print(file)
        

def copy_file_to(from_path, to_path):
    if not os.path.exists(to_path):
        os.makedirs(to_path)

    files = os.listdir(from_path)
    for file in  files:
        from_file = os.path.join(from_path, file)
        to = os.path.join(to_path, file)
        shutil.copy(from_file, to)
       

if __name__ == "__main__":

    portrait_map = read_map("shortcut/portrait.map")
    rename("shortcut/shortcut_image/portrait/36px/黑", "st_image/flag", portrait_map)

    #check_file("shortcut/st_car/action_condition", "shortcut/shortcut_image/action_condition")

    ac_map = read_map("shortcut/action_condition.map")
    rename("shortcut/st_car/action_condition", "st_image/action_condition", ac_map)

    copy_file_to("shortcut/st_car/card", "st_image/card")

    shutil.copy("shortcut/st_bg_map.json", "st_image/st_bg_map.json")
# coding=UTF-8<code>

import os
import sys
import shutil

name_to_amend = [
        ("@", "at"), 
        ("#", "pound"), 
        ("- ", "_"),
        (" ", "_"),
        ("-", "_"),
        ("installingaccessories", "installing_accessories"),
        ("findmycar", "findcar"),
        ("airconditioning", "airconditioner"),
        ("air_conditioning", "airconditioner"),
        ("/ ", "_"),
        ("／", "_"),
        ("__", "_"),
        ("12v", "12v_"),
        ]

def amend_name(old_name):
    new_name = old_name
    for tuple in name_to_amend:
        if new_name.find(tuple[0]) != -1:
            new_name = new_name.replace(tuple[0], tuple[1])
            print("rename:" + old_name + "----->" + new_name.lower() + "\n")       
    return new_name
    

def rename_vd(vd_path):
    file_list = os.listdir(vd_path)
    n = 0
    
    for vd in file_list:
        new_name = amend_name(file_list[n])
            
        old_name_with_path = vd_path + os.sep + file_list[n]
        new_name_with_path = vd_path + os.sep + "lg_widget_core_" + new_name.lower()
        os.rename(old_name_with_path, new_name_with_path)
        #print(new_name_with_path + "\n")
        n += 1

def svg_2_vd(svg_path, out_vd_path):
    cmd = "./vd/vd-tool/bin/vd-tool -c -in " + svg_path + " -out " + out_vd_path
    print(cmd)
    os.system(cmd)
    rename_vd(out_vd_path)

if __name__ == "__main__":
    svg_path = sys.argv[1]
    out_vd_path = sys.argv[2]
    if os.path.exists(out_vd_path):
        shutil.rmtree(out_vd_path)
    os.makedirs(out_vd_path)

    svg_2_vd(svg_path=svg_path, out_vd_path=out_vd_path)
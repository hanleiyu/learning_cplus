import os

def cal_num(g, num, object):
    for path, _, file_list in g:  
        for file_name in file_list: 
            with open(os.path.join(path, file_name), encoding='UTF-8') as f:
                for line in f.readlines():
                    if object in line:
                        num += 1
    return num
    
cnum = cal_num(os.walk(".\\effective\\"), 0, "<!-- [C++]")
cnum = cal_num(os.walk(".\\C++ primer\\"), cnum, "<!-- [C++]")
unum = cal_num(os.walk(".\\other\\"), 0, "<!-- [unity]")
bnum = cal_num(os.walk(".\\other\\"), 0, "<!-- [base]")

print(cnum)
print(unum)
print(bnum)
import logging
import os
PATH=os.path.join(os.getcwd())
print(PATH+"/requirements.txt")
if os.path.isfile(PATH+"/requirements.txt"):
    logging.info("存在文件requirements.txt")
    libs = []
    for line in open(PATH+"/requirements.txt", "r"):  # 设置文件对象并读取每一行文件
        libs.append(line)  # 将每一行文件加入到list中
    try:
        for lib in libs:
            print("start install {0}".format(lib))
            os.system("pip3 install " + lib)
            print("{} install successful".format(lib))
        print("All Successful")
    except:
        print("Failed SomeHow")
else:
    logging.debug("不存在文件requirements.txt")



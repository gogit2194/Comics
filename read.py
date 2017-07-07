import os
import sys
import string

def read(filename):
    d = []
    with open(filename, 'r') as input:
        for line in input.readlines():
            line = line.strip('\n')
            d.append(line)
    return d

def mkdir(dir_name):
    dir_path = os.path.join(dir_name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    return dir_path

if __name__ == '__main__':
    urls_comic = read('./comic_urls.txt')
    #print (urls_comic[95])
    #读取当前下载集数，建立相应文件夹
    for url in urls_comic:
        dp = url
        pp = (urls_comic.index(dp)) #int
        ppp = str(pp+1)
        print ('当前读取第',pp+1,'集')
        mkdir(ppp)
        print ('建立',pp+1,'集的文件夹')
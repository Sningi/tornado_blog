import os


def ls_all_file(filepath, flist):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            ls_all_file(fi_d, flist)
        else:
            flist.append(fi_d[12:])


if __name__ == '__main__':
    flist = []
    ls_all_file('static/file', flist)
    for i in flist:
        print(i)

import codecs


label_dir = 'coco128/annos.txt'
save_dir = 'coco128/classes.txt'
f = codecs.open(label_dir, mode='r', encoding='utf-8')  # 打开txt文件，以‘utf-8'编码读取
line = f.readline()  # 以行的形式进行读取文件
list1 = []

while line:
    flag = True
    a = line.split()
    c = a[1]
    print(c)
    for b in list1:
        if c == b:
            flag = False
    if flag:
        with open(save_dir, 'a') as fw:
            fw.write(c)
            fw.write('\n')
            list1.append(c)
    line = f.readline()
f.close()




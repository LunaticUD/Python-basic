# 合并文件并转化格式

# 读取第一个文件
# 1.[读取第6行第三个“"”到第4个“"”]:[读取第4行第三个“"”到这行结尾的“,”]
# --> 6:4 / 12:10 / 18:16 ......
# 组成放在字典中
# 多个文件操作

def JSONDic(sy):
    with open('D:/Python/JSON/{sy}.json'.format(sy=sy), mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        # 读取到第5行目标值
        with open('CET-4.json', mode='a', encoding='utf-8') as f1:
            i = 3
            f1.write('{' + '\n')
            while True:
                try:
                    a = lines[i + 2].split(":")[1].strip()
                    # 读取到第3行目标值
                    b = lines[i].split(":")[1].strip()
                    f1.write(a + ":" + b + '\n')
                    i = i + 6
                except:
                    break
            f1.write('}')


# nuu = 1
for s in range(65, 91):
    JSONDic(chr(s))
    # nuu = nuu + 1
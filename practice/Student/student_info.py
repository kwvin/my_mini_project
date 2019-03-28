from student import Student

def input_student():
    L = []
    while True:
        info_name = input("请输入姓名(空=退出)：")
        if info_name == "":
            break
        while True:
            try:
                info_age = int(input("请输入年龄："))
                if 0 <= info_age <= 100:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("不合法年龄：" + str(info_age))
        while True:
            try:
                info_score = int(input("请输入成绩："))
                if 0 <= info_score <= 100:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("不合法成绩：" + str(info_score))
        d = Student(info_name, info_age, info_score)
        L.append(d)
        print("当前人数：",Student.count)
    return L

def output_student(L):
    print("+------------+-------+---------+")
    print("|    name    |  age  |  score  |")
    print("+------------+-------+---------+")
    for i in L:
        name, age, score = i.get_info()
        print("|" + "%10s" % name + "  |" + "%5d" % age + "  |" + "%7d" % score + "  |")
    print("+------------+-------+---------+")
    print("当前人数：",Student.count)
    return 0


def updata_student(L):
    name = input("请输入要修改的学生姓名：")
    for dict in L:
        if dict.is_name(name):
            while True:
                try:
                    score = int(input("请输入修改后的成绩"))
                    dict.set_score(score)
                except ValueError:
                    print("不合法的成绩信息" + str(score))
                else:
                    break
            print("修改成功")
            return 0
    print("为找到该学生")
    return 0


def del_student(L):
    name = input("请输入要删除的学生姓名：")
    for i, dict in enumerate(L):
        if dict.is_name(name):
            del L[i]
            print("删除成功")
            print("当前人数：", Student.count-1)
            return 0
    print("为找到该学生")
    return 0


def sort_score_high(L):
    l =[]
    for i in L:
        l.append(i.get_score())
    l = sorted(range(len(l)), key=l.__getitem__,reverse=True)
    print("+------------+-------+---------+")
    print("|    name    |  age  |  score  |")
    print("+------------+-------+---------+")
    for i in l:
        name, age, score = L[i].get_info()
        print("|" + "%10s" % name + "  |" + "%5d" % age + "  |" + "%7d" % score + "  |")
    print("+------------+-------+---------+")
    return 0


def sort_score_low(L):
    l =[]
    for i in L:
        l.append(i.get_score())
    l = sorted(range(len(l)), key=l.__getitem__)
    print("+------------+-------+---------+")
    print("|    name    |  age  |  score  |")
    print("+------------+-------+---------+")
    for i in l:
        name, age, score = L[i].get_info()
        print("|" + "%10s" % name + "  |" + "%5d" % age + "  |" + "%7d" % score + "  |")
    print("+------------+-------+---------+")
    return 0


def sort_age_old(L):
    l =[]
    for i in L:
        l.append(i.get_age())
    l = sorted(range(len(l)), key=l.__getitem__,reverse=True)
    print("+------------+-------+---------+")
    print("|    name    |  age  |  score  |")
    print("+------------+-------+---------+")
    for i in l:
        name, age, score = L[i].get_info()
        print("|" + "%10s" % name + "  |" + "%5d" % age + "  |" + "%7d" % score + "  |")
    print("+------------+-------+---------+")
    return 0


def sort_age_young(L):
    l =[]
    for i in L:
        l.append(i.get_age())
    l = sorted(range(len(l)), key=l.__getitem__)
    print("+------------+-------+---------+")
    print("|    name    |  age  |  score  |")
    print("+------------+-------+---------+")
    for i in l:
        name, age, score = L[i].get_info()
        print("|" + "%10s" % name + "  |" + "%5d" % age + "  |" + "%7d" % score + "  |")
    print("+------------+-------+---------+")
    return 0

def save_student(L):
    try:
        with open("si.txt", mode="w") as f:
            for i in L:
               i.save(f)
    except :
        print("写入文件失败，请重试")
    print("保存成功")
    return 0


def read_student():
    L = []
    try:
        with open("si.txt", mode="r") as f:
            while True:
                str1 = f.readline()
                if  str1 == "":
                    break
                name, age, score = str1.split(",")
                d = Student(name, int(age), int(score))
                L.append(d)
    except :
        print("读取失败，请重试")
    print("读取成功")
    print("当前人数：", Student.count)
    return L
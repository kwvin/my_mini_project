
class Student:
    """学生类，用于记录学生信息"""
    count = 0

    def __init__(self, n, a, s):
        self.__name = n
        self.__age = a
        self.__score = s
        Student.count += 1

    def __del__(self):
        Student.count -=1

    def get_info(self):
        return (self.__name, self.__age, self.__score)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def set_score(self,score):
        """ 该方法用于更改成绩"""
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("不合法的成绩信息" + str(score))

    def is_name(self, name):
        return self.__name == name

    def save(self,file):
        file.write(self.__name)
        file.write(',')
        file.write(self.__age)
        file.write(',')
        file.write(self.__score)
        file.write('\n')
        return 0

    @classmethod
    def getTotalCount(cls):
        """获取记录的学生人数"""
        return cls.count
"""

输入学生考试成绩计算平均分

"""


def main():
    number = int(input('请输入学生人数:'))
    names = [None] * number
    socres = [None] * number
    for index in range(len(names)):
        names[index] = input('请输入第%d个学生的名字:' % (index + 1))
        socres[index] = float(input('请输入第%d个学生的成绩:' % (index + 1)))
    total = 0
    for index in range(len(names)):
        print('%s,%.1f' % (names[index], socres[index]))
        total += socres[index]
    print('平均成绩为:%.1f分' % (total / number))


if __name__ == '__main__':
    main()

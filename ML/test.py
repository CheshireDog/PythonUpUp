#  coding = utf-8 

# @Time : 2022/9/3 9:07
# @Author : HJH
# @File : test.py
# @Software: PyCharm

if __name__ == '__main__':
    age = 20

    age1 = 20
    print(id(age))
    print(id(age1))

    print(age is age1)

    money = 2000000
    salary = 2000000
    print(id(money))
    print(id(salary))

    print(money is salary)
    
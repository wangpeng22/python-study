'''
修改外层的局部变量、全局变量

nonlocal 用来声明外层的局部变量
global 用来声明全局变量
'''
a = 100

def outer():
    b = 10

    def inner():
        nonlocal b
        b = 20

        global a
        a = 1000

    inner()
    print("outer b=", b) # outer b= 20

outer()
print("outer a=", a) # outer a= 1000
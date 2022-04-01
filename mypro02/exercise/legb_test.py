# 测试LEGB
str ='global'
def outer():
    str = 'outer'

    def inner():
        str ='inner'
        print(str)
        inner()
outer()
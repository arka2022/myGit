'''
#Q1:
def dec(fn):
    print('begin Executing')
    def inner(*args,**kwargs):
        x=fn(2,3)
        print(x)
    return inner()
@dec
def multiply(num1, num2):
    return num1 * num2
'''
#Q2:
n=7
def fibonacci():
    a=0
    b=1
    for i in range(n):
        yield b
        t=a
        a=b
        b=a+t

obj = fibonacci()
for i in obj:
    print(i)





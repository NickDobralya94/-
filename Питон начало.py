
def Калькулятор(what,x,y):
    print(what, x, y)
what=input("Выберите что хотите сделать: +,-,/,*,**,%:")
x=float(input('Введите первое число:'))
y=float(input('Введите второе число:'))
if what=="+":
    z=x+y
    print(z)
elif what=='-':
    z = x - y
    print(z)
elif what == '*':
    z = x * y
    print(z)
elif what == '/':
    z = x / y
    print(z)
elif what == '**':
    z = x ** y
    print(z)
elif what == '%':
    z = x % y
    print(z)
else :
    print("Выбрана не верная функция попробуйте еще раз!")



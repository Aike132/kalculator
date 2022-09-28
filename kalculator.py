from math import sqrt
print("Введите номер операции (1 если сложение, 2 если вычитание, 3 если умножение, 4 если деление, 5 если квадратное уравнение)")
oper = int(input())
print("Введите число 1")
num1 = int(input())
print("Введите число 2")
num2 = int(input())
if (oper > 5) or (oper < 1):
    print("Необходимо ввести число от 1 до 5")
if oper == 1:
    res = num1 + num2
    print(str(res))
else:
    if oper == 2:
        res = num1 - num2
        print(str(res))
    else:
        if oper == 3:
            res = num1 * num2
            print(str(res))
        else:
            if oper == 4:
                res = num1 / num2
                print(str(res))
            else:
                if oper == 5:
                    print("Введите число 3")
                    num3 = int(input())
                    d = num2**2 - 4*num1*num3
                    if d < 0:
                        print("Нет корней")
                    if d == 0:
                        x = (-1 * num2)/(2*num1)
                        print(str(x))
                    if d > 0:
                        x = (-1 * num2 + sqrt(d))/(2*num1)
                        y = (-1 * num2 - sqrt(d))/(2*num1)
                        print(str(x)+", "+str(y))

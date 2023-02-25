a = int(input()) # вводим переменные
b = int(input())

# если a и b равны нулю, то решений нет
if (a == 0 and b == 0):
    print("INF")
# если b != 0 , то решение конечно
elif (a == 0 or (b%a) != 0):
    print("NO")
# чтобы решить уравнение мы должны -b поделить на a
else:
    print(int(-b/a))

k = int(input())
m = int(input())
n = int(input())

if k >= n:  # если вместимость сковороды не меньше числа котлет, то на все котлеты потерубется ровно 2m минут
    b = 2*m 
# потребуется обжарить, как мин 2n стороны котлет, затратив на это (2*n//k)*m минут
else: 
    b = (2*n//k)*m
# если число котлет не делится нацело на вместимость сковороды и при этом остаток от деления не равен половине
# вместимости, то некоторое количество котлет придется переворачивать еще раз, затратив на это лишнее время m минут
    if n%k != 0 and n%k != k//2:
        b += m
print(b)





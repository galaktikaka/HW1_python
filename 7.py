n = int(input())

if n >= 5 and n <= 20: # говорим коров если их от 5 до 20
    print( n, "korov")
elif n % 10 == 1: # если число заканчивается единицей, то говорим корова
    print( n ,"korova")
elif n % 10 >= 2 and n % 10 <= 4: # промежуток от 2 до 4 - говорим коровы
    print( n, "korovy")
elif n % 10 >= 5 and n % 10 <= 9 or n % 10 == 0: # от 5 до 9 или 0 - коров
    print( n, "korov")

    
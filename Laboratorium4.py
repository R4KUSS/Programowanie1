# Importowanie pakietów/bibliotek w Python
#sposób 1
# import math   # importuje wszystkie funkcje i metody dostępne w bibliotece math
# x=30*math.pi/180
# print(math.sin(x))

#sposób 2
# from math import sin # importuje funkcje sin dostępną w bibliotece math
# from math import pi
# x=30*pi/180
# print(sin(x))

#####################################
# oblicz pierwiastek z liczby 4
# from math import sqrt
# print(4**(1/2))
# print(sqrt(4))

#############################operatory logiczne 1 - teoria
# odpowiedż: False/True
# <	mniejsze
# <=	mniejsze lub równe
# >	większe
# >=	większe lub równe
# ==	równe co do wartości
# !=	negacja powyższego
# is	identyczne referencje
# is not	zaprzeczenie powyższego

####################Przykład 1
#Sprawdź wynik działania następujących operacji:
# l1 = [5,10]
# l2 = [5,10]
# print('l1 == l2 wynik:',l1 == l2)
# print('l1 != l2 wynik: ',l1 != l2)
# print(l1 >= l2)
# print(l1 is l2)
# print(l1 is not l2)
#############################operatory logiczne 2 - teoria
# x or y	jeżeli x == False, to y, w przeciwnym razie x
# w przybliżeniu alternatywa
# x and y	jeżeli x == False, to x, w przeciwnym razie y
# w przybliżeniu koniunkcja
# not x	negacja
####################Przykład 2
# a = False
# b = 2
# c = True
#
# print(a or b)
# print(b or a)
# print(c or a)
# print(a or c)
# print(b and a)
# print(a and b)
# print(a and c)
#################Instrukcje sterujące tj. instrukcje warunkowe i pętle  Teoria
 ################# 1. Instrukcja warunkowa "IF"#########struktura
# if warunek_1:
#     #lista instrukcji
# elif warunek_2:
#     #lista instrukcji
# elif warunek_3:
#     #lista instrukcji
#     ...
# else:
#     #lista instrukcji

######################Przykład 3########################
# liczba = int(input('Podaj liczbę od 1 do 10 :'))
# if liczba == 1:
#     print('Liczba 1')
# elif liczba == 2:
#     print('Liczba 2')
# elif liczba == 3:
#     print('Liczba 3')
# else:
#     print('Liczba inna niż 1,2,3')

# liczba = int(input('Podaj liczbę od 1 do 10 :'))
# if liczba == 1:
#     print('Liczba 1')
# else:
#     print('Liczba inna niż 1')

 ################# 1. Pętla "FOR" #########struktura
#for x in kolekcja:      uwaga: elementy kolekcji moga być dowolnego typu,
    #lista instrukcji           #nie musi to być wektor liczb.

################Przykład 4#########################################
# for i in range(1,11):      #range(1,11) --> 1,2,3,4,5,6,...,10
#     print('Python'*i)

# for i in range(0, 5):  #range(0,5) --> 0,1,2,3,4
#     print('Aneta')

##############Przykład 5 #####################################3
# litery2 = 'kognitywistyka'
# print(litery2.upper())
#
# litery = ['k','o','g','n','i','t','y','w','i','s','t','y','k','a']
# for x in litery:
#     z = x.upper()
#     print(z)

################# 1. Pętla "WHILE #########struktura
# while warunek:  # pętla dział dopóki warunek jest prawdziwy
#     lista instrukcji
##############Przykład 6###########################################
# iter = 0
# while iter < 5:
#    print('Lubię Pythona')
#    iter = iter + 1      # można też zapisać   iter += 1
#

##########tu liczymy kolejne pierwiaski liczb 1 do 10
# import math
# i = 1
# while i < 11:
#     print(math.sqrt(i))
#     i = i + 1
#############Zadania do wykonania##############################
#Zadanie 1
# Oblicz wartosc funkcji f(x)  dla dowolnego x
# f(x)=x  dla x<0  oraz  f(x)=2x  dla x>0

# x = int(input('Podaj wartosc x = '))
#
# if x < 0:
#     y = x
#     print('Wartosc funkcji f(x) = ',y)
# elif x > 0:
#     y = 2*x
#     print('Wartosc funkcji f(x) = ', y)
# else:
#     print('Wartosc x = 0, brak rozwiazan')



#Zadanie 2
# Napisz skrypt, wypisze pierwiastki liczb o wartosciach od 1 do 10
# import math
# for x in range(1,11):
#     #print(math.sqrt(x))
#     print(x**(1/2))
    #
#Zadanie 3
# Napisz program, ktory obliczy dowolna potege dowolnie wybranej liczby wiekszej od zera.
# x = int(input('Podaj liczbę x = '))

# if x < 0:
#     y = x
#     print('Wartosc x^2 = ',x**2)

# else:
#     print('Podałeś liczbę mniejszą od 0')


# Zadanie 4
#  Napisz skrypt, w ktorym w zaleznosci od wybranej przez uzytkownika liczby
#  calkowitej z zakresu od 1 do 5, wykonane zostana nastepujace działania:
#  dla wpisanej liczby 1  zostanie obliczona wartosc sin(x)
#  dla liczby 2 obliczona cos(x)  oraz dla pozostalych tg(x),

# import math
# from math import sin
# from math import tg
# from math import cos
# x = int(input('Podaj całkowitą liczbę od 1 do 5: x = '))

# if x == 1:
#     print('Wartosc sin(x) = ',math.sin(x))
#elif x==2:
#     print('Wartość cos(x)= ',math.cos(x))
#elif x<6:
#     print('Wartość tan(x)= ',math.tan(x))



#Zadanie 5
# Napisz skrypt, oblicz silnie z dowolnie wprowadzonej liczby całkowitej n
# n=4

# silnia = 1
# for i in range(1,n+1):
#   silnia = silnia*i
#   # print(i, silnia)

# print('silnia {} wynosi {}' .format(n,silnia))


#Zadanie 6
# Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n
# gdzie: zmienna wejsciowa n jest dowolnie zadana przez uzytkownika
# n=2

# suma = 1
# for i in range(1,n):
#   suma = suma+1/n
#   print('suma{} wynosi {}' .format(n,suma))
 
# n=int(input('podaj liczbę x ='))
# suma=1
# i=1
# while i <= n-1:
#   suma = suma +1/n
#   i=i+1
#   print(suma)

#Zadanie 7
# Utworz skrypt, ktory obliczy pierwiastki równania kwadratowego postaci ax^2+bx+c=0
#  dla dowolnie zdeklarowanych przez użytkownika stałych  a, b, c
#Zadanie 8
# Napisz program, ktory dla dowolnej liczby x podanej przez użytkownika
# czy jest to liczba (a) parzysta, (b) nieparzysta, (c) całkowita.

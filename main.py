from math import *
import math

# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmiennea

print("zadanie 1:\n")

a=13
a1 = 5
a2 = 10
b1 = 5.1
b2 = 5.2
c1 = 'cos1'
c2 = 'cos2'
d1 = (5j+5)
d2 = (10j+5)

print(a1,a2,b1,b2,c1,c2,d1,d2)

# Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne

print("zadanie 2\n")

dodawanie = a1+b1
odejmowanie = a1-b1
mnozenie = a1*b1
dzielenie = a2/a1

print(dodawanie, odejmowanie, mnozenie, dzielenie)

# Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

print("zadanie 3:\n")

x=a+a
print(x)
x=a-a
print(x)
x=a*a
print(x)
x=a/a
print(x)
x=a**a
print(x)
x=a%a
print(x)
print("\n")

# Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:

print("zadanie 4:\n")

print(math.e**10)
print("\n")
y=pow((math.log(5+((math.sin(8.00)**2)))),1/6)
print(y)
print("\n")
print(math.floor(3.55))
print("\n")
print(math.ceil(4.80))
print("\n")

# Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody capitalize)

print("zadanie 5:\n")

imie="MICHAL"
nazwisko="TARASZKIEWICZ"

print(imie.capitalize())
print(nazwisko.capitalize())
print("\n")

# Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)

print("zadanie 6:\n")

muza="O Sia La La Jak on ją tra la la la I ona ula la lal al a I on jej tira tara"

print(muza.count("la"))
print("\n")

# Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu. Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.

print("zadanie 7:\n")

lancuch="siatadajta"

print(lancuch[1])
print(lancuch[9])
print("\n")

# Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)

print("zadanie 8:\n")

print(muza.split())
print("\n")

# Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.

print("zadanie 9:\n")

string='lalala'
float=21.37
hex=hex(2115)

print(string)
print(float)
print(hex)
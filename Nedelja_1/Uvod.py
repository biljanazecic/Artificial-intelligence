
#UVOD U PYTHON

#prenos svih podataka je po referenci, svaka referenca u pythonu je vezana za neki objekat
#i kada radimo dodelu zaparavo vezujemo referencu za taj objekat

#precice za kretanje kroz jypter:
#CTRL+Enter za pokretaje celije u kojoj se trenutno nalazimo
#za kretanje po celijama koristimo tastaturu i mis
#za ubacivanje nove celije ispod koristimo slovo b
#za ubacivanje nove celije iznad koristimo slovo a
#za samo pisanje u celiji u kojoj se nalazimo enter
#za izlazak iz moda za pisanje esc

#Ispis podataka
from re import U
from tkinter import PIESLICE


print(10)
print("String")
a = 10
print(10)

#Ucitavanje podataka sa standarnog ulaza
a = input() #uvek vraca string
print(a)

#Formatiranje ispisa
x = 3 
y = 4
print(f'x = {x}, y = {y}')

#Obrada izuzetaka
try:
    a = int(input())
    print(a)
except ValueError as e:
    print("Greska", e)

#Ucitavanje podataka iz datoteke
ulazni_fajl = open('ulaz.txt', 'r')
sadrzaj_fajla = ulazni_fajl.read() #ucitavamo celokupan fajl, bice u obliku stringa
print(sadrzaj_fajla)

try:
    u_fajl = open('ulaz.txt', 'r')
    s_fajla = u_fajl.read()
    print(s_fajla)
except:
    print('Greska prilikom ucitavanja datoteke!')

#Ispis podataka u datoteku

try:
    izlazni_f = open('izlaz.txt', 'w')
    izlazni_f.write('Ovo je sadrzaj izlazne datoteke.\n')
except:
    print('Doslo je do grekse. Ne moze se upisati u datoteku.')

with open('izlaz.txt', 'w') as f:
    f.write('jos jedan izlaz')

try:
    with open('nepostoji.txt', 'r') as f:
        f.read()
except OSError as e:
    print(e)
#je l mogu u trenutnoj celiji da se koriste vrednosti iz starijih ili su odvojene
#upravo je to poenta, da u novim celijama mozemo da koristimo vrednosti iz starih

#If-else, for, while

if a % 2 == 0:
    print("Parno")
else:
    print("Neparno")

try:
    a = int(input('Unesite vrednost celog broja a: '))
    if a % 3 == 0:
        print('Broj a je deljiv brojem tri.')
    elif a % 3 == 1:
        print('Broj a daje ostatak 1 pri deljenju sa brojem 3.')
    else:
        print('Broj a daje ostatak 2 pri deljenju sa brojem 3.')
except:
    print('Neispravna vrednost broja a.')

godina = 2000
if (godina % 4 == 0 and godina % 100 != 0) or (godina % 400 == 0):
    print(f'Godina {godina} je prestupna')
else:
    print(f'Godina {godina} je prosta.')

for i in range(0,5):
    print(i)

for i in range(10, 0, -2):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1 #operator ++ nije podrzan

#Funkcije

def minimum_maximu(a, b):
    minimum = min(a,b)
    maximum = max(a,b)
    return (minimum, maximum) #preko tuple

min, max = minimum_maximu(24,12)

def saberi(a, b, c = 0):
    return a + b + c
saberi(1,2)

def change(a):
    a = 10
x = 15
change(x)
print(x)
#x ce ostati 15

def niz_neparnih():
    return [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

svi_neparni = niz_neparnih()
[prvi, drugi, treci] = niz_neparnih()[:3]

print(svi_neparni)
print(prvi, drugi, treci)

#Liste
#mozemo pristupati elementima liste
#mozemo menjati elemente liste

lista = [1, 2, 3, 4]
print(lista)

lista = [1, 2, 3, 4]
n = len(lista)
print(f'Duzina liste je {n}.')

#Iteracija kroz listu po indeksima
lista = [1, 2, 3, 4]
n = len(lista)
for i in range(0,n):
    print(list[i])

#Iteracija kroz listu po elementima (foreach petlja)
lista = [1, 2, 3, 4]
for element in lista: #foreach
    print(element)

#Ako nam trebaju indeksi
for index, el in enumerate(lista):
    print(index, el)

#List comprehension
lista = [1, 5, 2, 4, 3]
kvadrirana = [x**2 for x in lista] # ** stepen
print(kvadrirana)

lista = [1, 2, 3, 4, 5]
neparni = [x for x in lista if x % 2 == 1]
print(neparni)

#Zipovanje lista
lista1 = [1, 2, 3, 4]
lista2 = ['a', 'b', 'c', 'd']
zipovana = zip(lista1, lista2)
print(zipovana) #ispisace <zip object at pa neka adresa>
#ovako ce ispisati uredjene dvojke: (1, 'a'), (2, 'b')...
for e in zipovana:
    print(e)

#Obrtanje liste
lista = [1, 2, 3, 4, 5]
lista.reverse() #ne mozemo print(lista.reverse()) jer metod reverse ne vraca listu
print(lista)

#Sortiranje liste
lista = [1, 5, 2, 4, 3]
lista.sort(reverse = True) #posto smo stavili True lista ce biti sortirana od najveceg ka najmanjem
print(lista)

#Izdvajanje podlisti
# [polazni_indeks:zavrsni_index(n+1):korak]
lista = [1, 2, 3, 4]
print(lista[1:3]) # [1:3) desni interval nije ukljucen

lista = [1, 2, 3, 4]
print(lista[1:4:2]) # 2, (3), 4

lista = [1, 2, 3, 4] # -4 -3 -2 -1
print(lista[-4:-1]) # [1, 2, 3, 4]
#ispisace [1, 2, 3]

#Matrice (visedimenzioni nizovi)
matrica = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(matrica)
print(matrica[2][2])

#Dodavanje elemenata u listu i konkatenacija listi
lista = [1, 2, 3, 4]
lista.append(5) #dodavanje elementa na kraj liste
print(lista)

lista = [1, 2, 3, 4]
lista.insert(3, 3.4) #dodavanje vrednosti 3.4 na poziciju 3
print(lista)

lista = [1, 2, 3, 4]
lista.pop() #uklanjanje elementa sa kraja liste
print(lista)

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
print(lista1 + lista2) #konkatenacija listi

element = 0
lista = [1, 2, 3, 4]
print([element] + lista) #dodavanje elementa na pocetak liste

lista = [1, 2, 3, 4]
lista = lista[1:] #uklanjanje elementa sa pocetka liste izdvajanjem podliste

#Torke
#mogu da sadrze razlicite tipove
ntorka = (3, 'df', True, 3.42)
print(ntorka)
print(ntorka[1]) #pristupamo im preko njihovog indeksa
#jedino sto ne mozemo sa ntorkama je sto ne mozemo da dodamo novi element i ne mozemo da menjamo elemente ntorke
#ntorka[1] = 42 ne moze!

#Stringovi
#imutabilni
s = 'Hello world!'
#ne moze s[3] = 'H'
s_arr = list(s)
s_arr[3] = '!'
''.join(s.arr)

import random
#uniformna raspodela od 0 do 1
random.random()
lista = [1,2,3,4,5,6,7]
random.choices(lista) #vraca neki random broj iz liste
random.sample(lista, 4) #vraca k elemenata iz liste

#skupovi
skup = set([3,42,2,3,2,3])
s1 = set([1,2,3,4,5,6,7])
s2 = set([5,6,7,8,9,10])
s1 - s2 #razlika
s1 | s2 #unija
s1 & s2 #presek

#mape - niz kljuceva i vrednosti, gde su kljucevi jeidnstveni
mapa = {
    'a' : 34,
    'b' : [34123]
}
#moze da sadrzi kljuceve razlicitih tipova
mapa['c'] = 34 #dodavanje elemenata u mapu
del mapa['b'] #brisanje elementa iz mape

mapa.items() #da bi pristupili svim elementima

#iteriranje:
for key, value in mapa.items():
    print(key, value)
    
mapa.keys() #vraca kljuceve
mapa.values() #vraca vrednosti

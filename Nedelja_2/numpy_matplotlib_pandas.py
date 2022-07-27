# NumPy - biblioteka za opsta numericka izracunavanja i implementira neka najcesca izracunavanja nad nizovima i matricama,
# i omogucava nam da veoma lako implementiramo sopstvene numericke algoritme.
# NumPy je implementiran u C-u. Moguce je iz Python koda pozivati iskompajlirani C kod. Zbog toga dobija na efikasnosti i optimizovanosti.

# Matplotlib - biblioteka za vizualizaciju podataka.

# Pandas - biblioteka za manipulaciju i obradu podataka.

import numpy as np

a = np.array([1,,2,3])
# razlika izmedju obicnog i numpy niza:
# kod ovih numpy nizova - numpy ovo u pozadini cuva kao kontinualni niz elemenata (alocira kontinualni blok memorije i poredja sve elemente redom u memoriji)
# to je nesto sto ga cini efikasnijim od pythona (jer je numpy implementiran u C-u)
# obican niz je lista objekata, koji su alocirani kako gde je bilo mesta na heap-u
a.shape # oblik niza npr. (3,) znaci da je jednodimenzioni niz
type(a)  # numpy.ndarray
a[0] = 10 # array([10,2,3])

for i in a:
  print(i)
  
# matrice = visedimenzioni niz
b = np.array([
  [1,2,3],
  [4,5,6]
])
b
b.shape # (2,3) matrica 2x3
type(b) # numpy.ndarray

b[0][0], b[0][1], b[0][2] # (1,2,3)
b[1,0], b[1,1], b[1,2] # (4,5,6) preporuceni nacin

c = np.array([1, 3.4, True]) # dedukovace sve u float
d.dtype # dtype('float64')

c = np.array([1, 3.4, True, 'asdf', [3, False]]) # zalice se
c.dtype # dtype('O') object type vrati

# jedinicna matrica 3x3
a = np.eye(3)
a
a = np.eye(3,6)
a
# nula matrica 4x5
a = np.zeros((4,5))
a

# full popunjava n-dimenzioni niz prosledjenom vrednoscu
# niz koji se sastoji od 3 elementa, tj. array ([14, 14, 14])
np.full(3, 14)

np.full((4,6), 42) #matrica 4x6 gde su svi elementi = 42

# sve jedinice
np.ones((4,5))

# nasumicne vrednosti u matrici, uniformna raspodela iz intervala [0,1]
np.random.random((4,3))

a = np.array([
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13, 14, 15, 16]
])
# NxM
# hocemo da izdvojimo sve kolone sem prve i pretposlednje
a[:, 1:-1]  # a[x:y] -> [a[x], a[x+1]...[x+y+1]] x:y -> [x,y]
# preskoci jos i prvi red
c = a[1:, 1:-1] # slajsing, vraca referencu na originalnu matricu i deo nje po ovim indeksima, ne kreira novu matricu
c[1,1] = 100
# da li ce i originalni niz, a, da se promeni
# c ce se promeniti
# svaka dodela je po referenci, postavili smo c da pokazuje na matricu a
# tako da ako nesto izmenimo preko reference, izmenicemo i original, 11 ce postati 100
# ako nam treba bas kopija:
a_copy = a[1:, 1:-1].copy()
a_copy[0,0] = 123
# i sada je ovo zapravo kopija, koja je potpuno odvojena od originala
# a_copy ce se promeniti, ali original a nece

# racunske operacije

x = np.array([
  [1,2],
  [3,4]
])
y = np.array([
  [5,6],
  [7,8]
])
#sabiranje
x + y
#oduzimanje
x - y
# mnozenje
x * y
# deljenje
x / y
# radi pokoordinatno

# pravo mnozenje matrica
# 1. nacin
x.dot(y)
# 2. nacin
np.dot(x, y)

# 2. nacin
np.add(x, y)
np.subtract(x, y)
np.multiply(x, y)
np.divide(x, y)

x + 2 # svakom clanu matrice dodace 2
3.4 * x # svaki element matrice pomnozice sa 2

np.sqrt(x) # koren ce se pozvati nad svakim elementom
np.power(x, 2) # kvadrirace sve elemente pokoordinatno

# zadatak : Ax = b
A = np.array([
  [2,0],
  [0,2]
])
b = np.array([3.4, 7.8])
# Ax = b
# x = A_inv.dot(b)
A_inv = np.linalg.inv(A)
A_inv
x = A_inv.dot(b)
x
A.dot(x) # vraca vektor b

# hocemo da pronadjemo maksimalni element u nizu
x = np.array([1,5,2,3,7,8,4,6])
np.max(x) # 8
np.argmax(x) # na kom se indeksu nalazi max = 5
x == 3 # vraca False na svim mestima na kojima nije trojka, izuzev na mestu gde jeste trojka, vraca True

index = x == 3
index # array([False, False, False, True, False, False, False, True, False, True])
x[index] # bice neki pozdniz, vratice sve one vrednosti koje ispunjavaju ovaj uslov false/true
x[x > 5] # svi elementi veci od 5
x[(x > 5) & (x % 2 == 0)] # svi parni elementi koji su veci od 5

import matplotlib.pyplot as plt

plt.plot([0,1,2,3,4], [0,1,4,9,16]) # prvi parametar je x koordinata, a drugi y koordinata

plt.xlabel('x osa')
plt.ylabel('y osa')

plt.show() # prikazujemo grafik

# linspace pravi niz ekvidistantnih tacaka od pocetka do kraja
x = np.linespace(0, 5, 100) # podeli interval [0,5] na 100 jednakih delova
y = x
y_1 = x*x # pokoordinatno mnozenje 
y_2 = np.sqrt(x**3)

plt.plot(x, y, color = 'red')
plt.plot(x, y_1, color = 'green')
plt.plot(x, y_2, color = 'blue')

# formatiramo po  mocu latex-a
plt.legend([
  'y = x'
  'y = $ x^{2} $'
  'y = $ \sqrt{x^{3}} $'
])

plt.savefig('funkcija.pdf')
plt.savefig('funkcija.png')
plt.savefig('funkcija.svg')

plt.xlabel('x osa')
plt.ylabel('y osa')

plt.show()

import pandas as pd

# DataFrame - pandas kada ucitava podatke i kada ih smesta negde to radi u DataFrame
# ucitava podatke po kolonama

# ucitava podatke u data frame
df = pd.read_csv('iris.csv')
type(df)

# ispisuje prvih n redova, ali podrazumevana vrednost je prvih 5
df.head(n = 10)

# shape nam kaze koliko ima redova i kolona
df.shape # (150,5)

# size nam kaze koliko ima ukupno celija
df.size # 750

# ispisuje neke elementarne statistke za svaki od numerickih atributa (count, mean, std, min, 25%, 50%, 75%, max)
df.describe()

# dobijamo sve kolone
df.columns

for col in df.columns:
  print(col)
  
# uzorkovanje podataka
# cesto su nam podaci dimenzija koje nisu pogodne za eksperimentisanje i pravljenje prototipova
# tj. podaci mogu da budu preveliki
# bolje je uzeti manji uzorak, kao prototip
df_sample = df.sample(frac = 0.1) # ovo 0.1 znaci da smo uzeli nekih 10% 
# i sad ovaj sample ce biti uniformno sample-ovan iz celog skupa podataka

# 1. nacin za indeksiranje
# da bismo uzeli sve redove ali nekih atributa(kolona):
df[['sepal_length', 'petal_length']].head()
# dobicemo sve redove ovog data frame, ali samo one kolone koje smo naveli u listi iznad
# moze i ovako
columns = ['sepal_length', 'petal_length']
df[columns].head()

# 2. nacin za indeksiranje
# da koristimo zaista integer-e redova i kolona i to radimo preko atributa iloc
# levo od zareza idu redovi, desno od zareza idu kolone
x = df.iloc[:,:4] # svi redovi, ali za samo prve 4 kolone # data = ono na osnovu cega predvidjamo
y = df.iloc[:,-1] # samo poslednja kolona y = df[['species']] # target = ono sta zelimo da predvidimo

# kombinacija ova dva nacina (columns + iloc):
df.loc[4:10, ['petal_length', 'sepal_width']]

# matplotlib + biblioteka za ucitavanje podataka
# odvojimo dva atributa, jedan uzmemo kao x osu, a drugi kao y osu
# i da te uredjene parove stavimo na grafikon kao tacke
# i da svaku tacku obojimo bojom vrste kojoj pripada
# vrste cemo da konvertujemo u neku boju i da svaku tacku obojimo onom vrstom kojoj ta tacka pripada
# scatter u matplotlib-u

plt.scatter([3, 4, 1],[2, 5, 7], c = ['red', 'green', 'blue']) # to su tacke : (3,2), (4,5), (1,7)
plt.show()

# treba da izmapiramo sve ove vrste u neku boju
species = df[['species']]
type(species) # pandas.core.frame.DataFrame
# postoji nesto bas u data frame-u sto vrednosti iz kolone enumerise tj. konvertuje ih u enumeraciju i zove se Categorical
categories = pd.Categorical(species)
categories.codes # uz pomoc codes iz kategorija izvucemo koji su njihovi redni brojevi

petal_length = df[['petal_length']]
sepal_length = df[['sepal_length']]

plt.scatter(petal_length, sepal_length, c = categories.codes)
plt.show()

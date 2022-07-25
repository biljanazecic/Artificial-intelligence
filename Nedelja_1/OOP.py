#Python podrzava objektno orijentisano programiranje.
# U python-u je sve objekat, cak je i klasa objekat.

class Vozilo:
  pass
type(Vozilo) #ima tip type

#za def konstruktora neke klase potpis je:
class Vozilo:
  #atributi objekta klase
  reg_broj = 'asd' #staticke promenljive
  
  def __init__(self, rb): #self == this
    printf('Vozilo')
    self.reg_broj = rb
    Vozilo.__update(self)
    #U Python-u unutra klasa sve je podrazumavano public.
    #Postoji konvencija sta ce biti private - tako sto se stavi jedna donja crta
    #Po konvenciji je private, a kompajler ga zapravo vidi kao public.
    #pravljenje atributa nije vezano za konstruktor.
    self._private_var = 42 #ovo ne znaci da ne mozemo ovoj promenljivoj da pristupimo van klase, mozemo bez problema, mozemo i da je promenimo (linija 48)
    
  def __str__(self):
    return f'Reg broj : {self.reg_broj}'
  
  def update(self):
    print('Vozilo.update')
    
  def add_atribute(self, a):
    self.a = a
    
   __update = update # __Vozilo_update (staticka promenljiva)

class Automobil(Vozilo):
  def __init__(self, rb, broj_tockova):
    super().__init__(rb)
    print('Automobil')
    self.broj_tockova = broj_tockova
    Automobil.__update(self)
    
  def update(self):
    print('Automobil.update')
    
#novi objekat ove klase pravimo tako sto pozovemo njegov konstruktor i navedemo ime klase
a = Vozilo()
b = Vozilo('BG-1234')
c = Automobil('BG-4,3434', 4)
c._private_var = 23
c.add_atribute(52)
c.a #52
print(b.reg_broj, Vozilo.reg_broj) #BG-1234, asd

#Dinamicnost python-a : tokom izvrsavanja mozemo praviti objekte, dodeljivati im atribute, metode i pravila po kojima ce cela klasa funkcionisati.
#Zasto je ovo korisno?
#Npr. ako imamo skup podataka, neka je to neka tabela i ona ima neke kolone i te kolone imaju imena i tipove.
#Uz pomoc python-a mozemo u istom kodu da procitamo kolone te tabele, da pogledamo koji su tipovi, 
#konstruisemo klasu koja ce kao atribute imati kolone te tabele koji ce biti tog tipa koje su vrednosti zapisane u tabeli
# i sve to raditi tokom citanja i parsiranja same tabele.
#To u kompajliranim programskim jezicima koji su staticki tipizirani nije bas tako moguce uraditi.

 

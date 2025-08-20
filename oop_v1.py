from typing import Any
from collections.abc import Sized


# class - namespace, (schema)

# class keyword
# pascal case (upper camelcase)
#syntatic sugar -> inna składnia, nie nowa funkcjonalność
class Name:
    ...

# object to najwyższa class, zawsze musi być w drzewie dziedziczenia
# type to najwyższa metaclass
# other_params to **kwargs, tylko tak pisane bo to wywołanie, a nie deklaracja
# wszystkie parametry po metaclass=type, zostaną użyte do tworzenia metaklasy
class NameTwo(object, metaclass=type, #other_params='value'
              ):
    pass



# jak udowodnić, że class są tylko namespace?
# jak udowodnic, że metaclass tworzą class?
# by metaclass
NameThree = type('NameThree', (), {})
# type to jest metaclass (tworzy klasy), (a klasy tworzą obiekty)
#print(NameThree) # >> <class '__main__.NameThree'>  można sprawdzić w deklaracji

# by metaclass with attributes

def init_(self, x):
    self.x = x

attrs = {
    "__init__": init_,
    "value": 42
}

NameFour = type('NameThree', (), attrs)
# NameFour = type('NameThree', (object,) -> tu klasy bazowe, attrs -> tu atrybuty)
nf = NameFour(666)
#print(nf.x, nf.value)

# class

class NameFive:
    def __new__(cls, *args: Any, **kwargs: Any) -> "NameFive":
        self = super().__new__(cls) # __new zwraca obiekt przypisany do self na podstawie parametru cls
        # self.value_ = args[0] dowód, że 666 najpierw wchodzi do __new__
        return self # nasz __new__ nic nie robi , to defaultowa metoda tworzenia obiektu

    def __init__(self, value): # za każdym razem jak wywołuje init obiekt już istnieje
        self.value = value
        self.temp = 42

# Poniżej kolejność wywołań przy powstaniu nowego obiektu
# constructor - __new__ - funkcjonalność, która tworzy obiekt. Tylko class object ma
# initializer - __init__
n_five = NameFive(666) # przy wywołaniu podajemy parametry __init__, które wcześniej przechodzą przez __new__ :D

#print(n_five.value)



# type inference - auto wykrywanie typu
# API - application programming interface

class Auto:
    color = 'red' # share state param (współdzielony stan)

    def __init__(self, model: str, max_speed: int, year: int):
        self.model = model
        self.max_speed = max_speed
        self.year = year
        self.start_engine = True
        self._color = type(self).color #type(self) zwraca klasę obiektu
        self.speed = 0


    def speed_up(self, amount): # metoda na rzecz obiektu
        if self.start_engine:
            self.speed = min(self.speed + amount, self.max_speed)

    @classmethod # oto custom constructor
    def auto_nitro(cls, model:str, max_speed: int, year: int, nitro: bool) -> 'Auto':
        self = super().__new__(cls)
        self.__init__(model, max_speed, year)
        self.nitro = nitro
        return self

    @staticmethod # metoda statyczna mogłaby być funkcją bez zmiany implementacji
    def magic():
        return 'brum!!'

    def __str__(self) -> str: # tak naprawdę print(str(bmw)
        return self.model

    def __len__(self):
        return 42 # jak to wywołać aby pokazać drzewo drzedziczenia?

toyota = Auto.auto_nitro('auris' , 270, 1990, True)
print(toyota.nitro)

# class method od zwykłej różni się tym, że manipulujemy klasą, a w zwykłej manipulujemy obiektem.

bmw = Auto("E46", 180, 1995)
fiat = Auto("Uno", 240, 1999)

# bmw.yolo = 42 zła praktyka. Na rynku w krk nie sikamy

bmw.color = 'blue' # ten zapis dynamicznie tworzy pole color do obiektu

        
# syntactic sugar
bmw.speed_up(20)

# type(bmw).speed_up(bmw, 20)

# to samo bez syntatic sugar. ludzie nie wiedzą, że powyższe to ss dla poniższego
Auto.speed_up(bmw, 50)

print(dir(Auto)) # udowadnia, że metoda speed_up nie należy do obiektu
print(bmw) # tak naprawdę print(str(bmw)
print('-----------------------------')
# jak to wywołać aby pokazać drzewo dziedziczenia?
print(Auto.__mro__)
print('-----------------------------')
print(issubclass(Auto, object)) # sprawdzam, czy Auto jest podklasą object? True
print(issubclass(Auto, Sized)) # sprawdzam, czy jest podklasą klasy Sized?


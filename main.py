from lib2to3.pgen2 import driver
from pprint import pprint
from account import Account
from car import car
from cash import cash
from uberX import uberX
from uberConfort import uberConfort

if __name__ == "__main__":
    print("hola mundo")
    
    car = car("PBO5555", Account("david", "1726210790", "25"))
    print(vars(car))
    print(vars(car.driver))
    
    uberX = uberX("PCC-12345", Account("david", "145478245", "35"), "chevy", "spark")
    print(vars(uberX))
    print(vars(uberX.driver))
    
    uberConfort = uberConfort("p3k-45621", Account("jose", "152463245"), "dogde", "cuero", "6")
    print(vars(uberConfort))
    print((uberConfort.driver))
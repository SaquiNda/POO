from lib2to3.pgen2 import driver
from pprint import pprint
from account import Account
from car import car
from payment import payment
from router import router

if __name__ == "__main__":
    print("hola mundo")
    
    carro = car()
    carro.id          = 5
    carro.brand       ="toyota"
    carro.driver      ="David"
    carro.passager    = 5

    pprint(vars(car))

    carro2 = car()
    carro2.id           = 5
    carro2.brand        ="kya"
    carro2.driver       ="sad"
    carro2.passager     = 6

    pprint(vars(carro2))
    
    user = Account()
    user.id             = 8
    user.name           ="Solis"
    user.Document       ="xml"
    user.mail           ="eliasdavidsch@hotmail.com"
    user.Password       ="242514"
    
    pprint(vars(Account))
    
    buy = payment()
    buy.id              = 9
    buy.ammount         = 15
    
    pprint(vars())
    
    get = router()
    get.id              = 6
    get.start           = "inicio"
    get.end             = "fin"
    
    pprint(vars())
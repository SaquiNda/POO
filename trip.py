from car import car
from driver import driver
from payment import payment
from router import router
from user import user

class trip(car, user, driver, router, payment):
    idTrip      = int
    
    def __init__(self, idTrip, iduser, idDriver, star, end, kmDistance, typePayment, ammount, date, licence, drive):
        super().__init__(idTrip, iduser, idDriver, star, end, kmDistance, typePayment, ammount, date, licence, drive)
        self.idTrip             = idTrip
        
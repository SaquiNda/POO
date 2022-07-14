from typing_extensions import Self
from car import car

class uberConfort(car):
    numberpassanggers          = int
    carAccepted                = []
    seatMaterial               = str
    
    def __init__ (sef, license, driver, carAccepted, seatMaterial, numberpassanggers):
        super().__init__(license, driver)
        Self.carAccepted            = carAccepted
        Self.numberpassangers       = numberpassanggers
        Self.seatMaterial           = seatMaterial
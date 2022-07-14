from car import car

class uberfast(car):
    brand           = str
    model           = str
    loadsize        = []
    loadweight      = int
    
    def __init__(self, license, driver, brand, model, loadsize, loadweight):
        super.__init__(license, driver)
        self.brand          =brand
        self.model          =model
        self.loadsize       =loadsize
        self.loadweight     =loadweight
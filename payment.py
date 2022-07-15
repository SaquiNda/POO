from datetime import date


class payment :
    id              = int
    ammount         = int
    date            = str
    typePaytment    = []
    
    def __init__(self, id, ammount, date, typePayment):
        self.ammount                = ammount
        self.id                     = id
        self.date                   = date
        self.typePaytment           = typePayment
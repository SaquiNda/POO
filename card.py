from datetime import date
from bank import bank

class card(bank):
    cardNumber            = int
    cardSecurity          = int
    cardDate              = int
    
    def __init__(self, id, ammount, date, bankname, identification, numberAccount, cardDate, cardNumber, cardSecurity, typePayment):
        super().__init__(id, ammount, typePayment, date, bankname, identification, numberAccount)
        self.cardDate           = cardDate
        self.cardNumber         = cardNumber
        self.cardSecurity       = cardSecurity
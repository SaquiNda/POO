from payment import payment

class bank(payment):
    bankname            = str
    identification      = str
    numberAccount       = int
    
    def __init__(self, id, typePayment, date, ammount, bankname, identification, numberAccount):
        super().__init__(id,typePayment, ammount, date)
        self.bank               = bankname
        self.identification     = identification
        self.numberAccount      = numberAccount
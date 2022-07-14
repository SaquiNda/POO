from account import Account

class driver(Account):
    id          = int
    license     = str
    
    def __init__(self, name, document, mail, Password, gender, numberCell, age):
        super().__init__(name, document, mail, Password, gender, numberCell, age)
        
        self.id             = id
        self.license        = license
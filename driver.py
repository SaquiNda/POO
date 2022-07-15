from account import Account

class driver(Account):
    idDriver          = int
    license           = str
    
    def __init__(self, idDriver, license, name, document, mail, Password, gender, numberCell, age):
        super().__init__(name, document, mail, Password, gender, numberCell, age)
        
        self.idDriver             = idDriver
        self.license              = license
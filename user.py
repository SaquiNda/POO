from account import Account

class user(Account):
    iduser       = int
    
    def __init__(self, iduser, name, document, mail, Password, gender, numberCell, age):
        super().__init__(name, document, mail, Password, gender, numberCell, age)
        
        self.iduser         = iduser
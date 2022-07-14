from account import Account

class user(Account):
    id = int
    
    def __init__(self, name, document, mail, Password, gender, numberCell, age):
        super().__init__(name, document, mail, Password, gender, numberCell, age)
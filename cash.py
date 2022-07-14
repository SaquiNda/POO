from payment import payment

class cash(payment):
    def __init__(self, id, ammount):
        super().__init__(id, ammount)
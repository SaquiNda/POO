from payment import payment

class paypal(payment):
        def __init__(self, id, ammount):
                super().__init__(id, ammount)
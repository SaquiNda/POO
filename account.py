class Account :
    id          = int
    name        = str
    Document    = int
    mail        = str
    Password    = int
    gender      = str
    numberCell  = int
    age         = int
    
    #METODO CONSTRUCTIVO EN PYTHON
    def __init__(self, name, document,):
        self.name           = name
        self.Document       = document
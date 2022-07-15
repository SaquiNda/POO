from tracemalloc import start


class router :

    start           = []
    end             = []
    kmDistance      = int
    timeAprox       = int
    payAprox        = float
    
    def __init__(self, star, end, kmDistance, timeAprox, payAprox):
        self.start          = star
        self.end            = end
        self.kmDistance     = kmDistance
        self.timeAprox      = timeAprox
        self.payAprox       = payAprox
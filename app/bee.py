class Bee(object):
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp

class QueenBee(Bee):
    hit = 8
    def __init__(self):
       Bee.__init__(self,"queen",100)

class WorkerBee(Bee):
    hit = 10
    def __init__(self):
       Bee.__init__(self,"worker",70)

class DroneBee(Bee):
    hit = 12
    def __init__(self):
       Bee.__init__(self,"drone",50)

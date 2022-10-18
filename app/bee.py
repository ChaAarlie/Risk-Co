#Bee module
#attack non implemented yet
class Bee(object):
    def __init__(self,name,hp, attack):
        self.name=name
        self.hp=hp
        self.attack=attack

# 3 bee subclasses that inherit Bee
class QueenBee(Bee):
    attack : 20
    hit = 8
    def __init__(self):
       Bee.__init__(self,"queen",100)

class WorkerBee(Bee):
    attack : 5
    hit = 10
    def __init__(self):
       Bee.__init__(self,"worker",70)

class DroneBee(Bee):
    attack : 3
    hit = 12
    def __init__(self):
       Bee.__init__(self,"drone",50)

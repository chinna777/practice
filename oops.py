class Animals():
    #feed="based on species"
    def __init__(self,name=None,weight=None,species=None):
        self.name=name
        self.weight=weight
        self.species=species
    def eat(self):
        print(f"hey i ate {self.name}")
        print('and iam not hungry anymore good night')
    def __str__(self):
        return 'nothing'
    def danny(self):
        print('hey danny your doing fine')
a1=Animals(name='wolf',weight=200,species='carnivore')


a1.species
a1.eat()
a1.name       
class Circle(Animals):
    pi=3.14
    def __init__(self,radius,diameter):
        super().__init__(self)
        self.radius=radius
        self.diameter=diameter
    def area(self):
        print(4*self.pi*self.radius**2)
    
a2=Circle(34,62)
a2.radius
a2.eat()

    
  
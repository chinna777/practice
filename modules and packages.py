from hello import Hey
class Hi:
    def __init__(self,name):
        self.name=name
    def hifun(self):
        print(f"hey {self.name} how ru doing")

print(__name__)
if __name__ == "__main__":
    h=Hi('danny')
    h.hifun() 
    h1=Hey('coding')
    h1.improve()
else:
    pass

   
    



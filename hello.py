
class Hey():
    def __init__(self,wow):
        self.wow=wow

    def improve(self):
        print(f"i wanna imorove my skills{self.wow}")   
if  __name__ == "__main__": 
    m=Hey('wow')
    m.improve()
else:
    pass
l1=[4,5,5,61,5]

for i in range(len(l1)-1,0,-1):
    print(i)
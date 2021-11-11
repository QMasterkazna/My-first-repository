class Simple(object):
    def __init__(self,A,B,C):
        self.a=A
        self.b=B
        self.c=C
    def Changes(self):
        return self.a+self.b+self.c
S1=Simple(5,10,15)
print("Площадь будет:")
print(S1.Changes())

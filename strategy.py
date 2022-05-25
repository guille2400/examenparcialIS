from typing import Container


class cincoPare():
    def __init__(container):
        container = 0
    def winner(self,value):
        if value%2==0:
            container = container+1
        if self.container == 5:
            return True
        return False

class cincoImpar():
    def __init__(container):
        container = 0
    def winner(self,value):
        if value%2==1:
            container = container+1
        if self.container == 5:
            return True
        return False

class numPrimo():
    def __init__(container):
        container = 0
    def winner(self,value):
        for n in range(2, value):
            if value % n == 0:
                return False
        container = container+1
        return True

class tresmultidiez():
    def __init__(container):
        container = 0
    def winner(self,value): 
        if value % 10 ==0:
            container = container+1
        if self.container == 3:
            return True
            

class dosmulti25():
    def __init__(container):
        container = 0
    def winner(self,value): 
        if value % 25 ==0:
            container = container+1
        if self.container == 2:
            return True
        return False

            


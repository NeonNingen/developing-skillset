class calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.display(self.num1 + self.num2)
    
    def minus(self, gofirst):
        if gofirst == "1":
            return self.display(self.num1 - self.num2)
        else:
            return self.display(self.num2 - self.num1)
        
    def multiply(self):
        return self.display(self.num1 * self.num2)
    
    def divide(self, gofirst):
        if gofirst == "1":
            return self.display(self.num1 / self.num2)
        else:
            return self.display(self.num2 / self.num1)
        
    def display(self, result):
        print(result)
        

    '''
    Todo: 
    Allow multiple numbers to be siphened into the calculator (Use an array)
    
    Functions to add to the calculator:
    Sort function
    Pythagoras theorem
    
    '''
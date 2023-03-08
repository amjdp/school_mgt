class Operation:
    pass

# method overriding

class A: 
    def display(self):
        print('from class A')

class B(A): 
    def display(self):
        print('from class B')

obj = B()

obj.display()
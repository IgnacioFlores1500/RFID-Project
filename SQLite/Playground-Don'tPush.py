



print("First Test Line - Ignacio Flores\n If you see this text, someone commited something they shouldn't")

def add(x,y):
    total = 0
    total = x + y
    return total


def main():
    five = 5
    two  = 2
    print(add(two,five))

class dog:
    
    def __init__(self,name):
        self.name = name

    def getName(self):
        print(self.name, 'is my name')
    

test = dog('Rex')
test.getName()


if __name__ =="__main__":
    main()


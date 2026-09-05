class complex:
    def __init__(self, rl, img):
        self.real = rl
        self.img = img

    def shownum(self):
        print(self.real, "+ i",self.img)

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newreal, newimg)

num1 = complex(1,4)
num2 = complex(3,5)

num1.shownum()
num2.shownum()
num3 = num1+num2
num3.shownum()
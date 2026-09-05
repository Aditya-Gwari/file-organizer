class car:

    def __init__(self, type):
         self.type = type

    @staticmethod
    def start():
        print("START")

    @staticmethod
    def stop():
        print("STOP")

class toyota(car):
    def __init__(self, name, type):
            self.name = name
            super().__init__(type)
            super().start()


car1 = toyota("prius","diesel")
print(car1.type)
print(type(car1))
class Pai:
    def __init__(self):
        self.result = None

    def minus(self,no1,no2):
        self.result = no1 - no2

        return self.result

a = Pai()
answer = a.minus(30,20)
print(answer)

# TASK1

# class Bank_Account:
#     def __init__(self):
#         self.b = 0

#     def dep(self):
#         a = int(input("Введите сумму которую вы хотите вывести: "))
#         self.b = self.b + a
#
#     def output(self):
#         a = int(input("Сколько денег вы хотите вывести?: "))
#         if self.b >= a:
#             self.b = self.b - a
#             print("Средства успешно выведены!" )
#             print("Остаток на балансе", self.b,"$")
#         else:
#             print("У вас недостаточно средств для вывода")
#             print("На счету", self.b,"$")
#
# S = Bank_Account()
# S.dep()
# S.output()

# TASK 2

class Money:
    def __init__(self, number=float(input("Введите намбер денег ")),
                 currency=str(input("Введите валюту [USD,EUR,RUB] ")),
                 amount=float(input("Введите эмаунт денег "))):
        self.number = number
        self.currency = currency
        self.amount = amount



    def to_tenge(self):
        USD = 480
        EUR = 500
        RUB = 8
        # currency = str(input('Какую валюту вы хотите конвертировать в тенге [USD, EUR, RUB]? '))
        if self.currency == "USD":
            return self.amount*self.number*USD
        elif self.currency == "EUR":
            return self.amount*self.number*EUR
        elif self.currency == "RUB":
            return self.amount*self.number*RUB
        else:
            print("нет такой валюты ты че")

    def Get(self):
        print(f'{self.amount} of {self.number} {self.currency}')

class Wallet(Money):
    def __int__(self,dengi):
        self.money=[]
        self.money.append(Money.Get(dengi))
    def addwallet(self,dengi):
        self.money.append(Money.Get(dengi))
    def getIndex(self,a):
        print(self.money[a])
    def __str__(self):
        return self.money

a=Money()
a.Get()
# m=Wallet()
# m.addwallet()
# print(a.__str__())











class User:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money

    def add_money(self, money):
        self.money += money
        print(f"{self.owner}現在有{self.money}元")
ming = User ("小明",100)
ming.add_money(50)
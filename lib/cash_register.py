#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.last = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for num in range(quantity):
            self.items.append(title)
        self.last = [price, quantity]

        

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = int(self.total) * (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def items(self):
        return self.items
    
    def void_last_transaction(self):
        num = self.last[1]
        self.items = self.items[:-num]
        self.total -= self.last[0] * self.last[1]

        

        

    


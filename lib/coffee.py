#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.price = price
        if size not in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
        else:
            self.size = size
    
    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1    
    pass

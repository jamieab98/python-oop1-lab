#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not size in ("Small", "Medium", "Large"):
            print("size must be Small, Medium, or Large")
        else:
            self._size = size
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1    
    pass

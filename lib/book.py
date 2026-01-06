#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_Count):
        self.title = title
        self.page_Count = page_Count
        print(f"You are on page {self.page_Count} of {self.title}")
    
    def turn_page(self):
        self.page_Count += 1
        print(f"You are now on page {self.page_Count} of {self.title}")
    pass
    
Book1 = Book("A court of thorns and roses", 49)
Book1.turn_page()
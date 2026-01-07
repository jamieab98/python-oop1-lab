#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        if not isinstance(page_count, int):
            print("page_count is not an integer")
        else:
            self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
    pass
    
Book1 = Book("A court of thorns and roses", 10)
Book1.turn_page()
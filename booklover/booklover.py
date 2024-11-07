import pandas as pd

class BookLover:
    
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name                                                                 # name of person; string type
        self.email = email                                                               # email of person; string type
        self.fav_genre = fav_genre                                                       # person's fav book genre; string type
        self.num_books = num_books                                                       # number of books person's read; int type
        self.book_list = book_list
    
    def add_book (self, book_name, book_rating):
        if book_name in self.book_list['book_name'].to_list():
            print("Book is already in the list.")
        else:
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books +=1
            
    def has_read(self,book_name):
        if book_name in self.book_list["book_name"].to_list():
            return True
        else:
            return False
        
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list.query('book_rating > 3')
    
        

import unittest
import pandas as pd
import numpy as np
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        booklover1 = BookLover("Jane", 'jane23@gmail.com', 'classics')
        book = "Jane Eyre"
        booklover1.add_book(book,4)
        self.assertTrue(book in booklover1.book_list.book_name.to_list())

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover2 = BookLover("Tyler", 'tyler23@gmail.com', 'mystery')
        book2 = "Fight Club"
        booklover2.add_book(book2,4)
        booklover2.add_book(book2,3)
        self.assertEqual(sum(booklover2.book_list.book_name.str.count(book2)),1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklover3 = BookLover("Austin", "austin1234@gmail.com", 'adventure')
        book3 = "Outliers"
        booklover3.add_book(book3,4)
        self.assertTrue(booklover3.has_read(book3))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover4 = BookLover("Emily", "emily@hotmail.com", "romance")
        book4 = "Me Before You"
        booklover4.add_book(book4,5)
        self.assertFalse(booklover4.has_read("Pride and Prejudice"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        blist = pd.DataFrame([('Night Shift',3), ("IT", 4), ("The Red Room",5)], columns = ["book_name" , "book_rating"])
        booklover5 = BookLover("Maddy", "madinusa@gmail.com", "thriller", 3, blist)
        expected = len(blist)
        self.assertEqual(len(booklover5.book_list) , expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklover6 = BookLover("Nate", "nathaniel24@virginia.edu", "horror")
        booklover6.add_book("Dracula" , 4)
        booklover6.add_book("The Invisible Man", 5)
        booklover6.add_book("The Shining", 3)
        favs = booklover6.fav_books()
        fav_ratings = np.array(favs.book_rating)
        over3 = sum(fav_ratings > 3)                       # how many books in favs have ratings > 3
        self.assertEqual(over3, len(favs))                 # if length of how many are over 3 is the same as length of list of fav movies
        
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
# This program has two parts. 
# Part I takes a list of books (any length)
# and uses function print_first_three_books to slice the first three books 
# out of the list of favorites. 
#--------------------------------------------#
# Test implemented checks for no more than 3 books and whether the
# return list is a data type of list.

# Part II uses a dictionary of a student database
# with keys as names (strings) and values as id numbers (int)
#---------------------------------------------#
# Test checks for correct data types of student database, its keys, and values.


### Part I ###
list_favorite_books = ["Demons by Dostoevsky", "The Creature from Jekyll Island by G. Edward Griffin", "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
                       "The Gulag Archipelago by Alexander Solzhenitsyn"]

# function returns sliced (at most) 3 books from list of favorites
def print_first_three_books(list_of_books):
    first_three_books = list_favorite_books[0:3]
    return first_three_books


# Check that function print_first_three_books returns a) data type list b) length is less than 4
class Test_First_Three_Books:


    def setup_method(self):
        self.list_favorite_books = list_favorite_books
        self.first_three_books = print_first_three_books(self.list_favorite_books)


    def test_first_three_books_size(self):
        assert len(self.first_three_books) < 4

    def test_first_three_books_type(self):
        assert isinstance(self.first_three_books, list) == True



### Part II ###

student_database = {   
        "Abe": 1,
        "Bill": 2,
        "Cindy": 3,
        "Dorry": 4,
        "Ellie": 5,
        "Fred": 6,
        "James": 7
    }


# Test student database
# database needs to be dictionary, keys are strings, values are ints
class TestStudentDatabase:

    # initialize student database
    def setup_method(self):
        self.student_database = student_database


    # test for keys as strings
    def test_keys_are_strings(self):
        keys = list(self.student_database.keys())
        for key in keys:
            assert isinstance(key, str) == True

    # test for values as ints
    def test_values_are_ints(self):
        values = list(self.student_database.values())
        for value in values:
            assert isinstance(value, int) == True

    # test student database as dictionary
    def test_student_database_is_dictionary(self):
        assert isinstance(self.student_database, dict) == True



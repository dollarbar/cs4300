

list_favorite_books = ["Demons by Dostoevsky", "The Creature from Jekyll Island by G. Edward Griffin", "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
                       "The Gulag Archipelago by Alexander Solzhenitsyn"]

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


student_database = {   
        "Abe": 1,
        "Bill": 2,
        "Cindy": 3,
        "Dorry": 4,
        "Ellie": 5,
        "Fred": 6,
        "James": 7
    }


# test student database is key: value -> str: int

class TestStudentDatabase:

    def setup_method(self):
        self.student_database = student_database

    def test_keys_are_strings(self):
        keys = list(self.student_database.keys())
        for key in keys:
            assert isinstance(key, str) == True

    def test_values_are_ints(self):
        values = list(self.student_database.values())
        for value in values:
            assert isinstance(value, int) == True

    def test_student_database_is_dictionary(self):
        assert isinstance(self.student_database, dict) == True



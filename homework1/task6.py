# This uses file handling and metaprogramming.
# User needs to type the working directory of the file of choice
# and the function file_word_count returns the word count of the file

# Testing is done through a metaprogramming technique that tests
# the correct word count with a dynamically named function
# depending on the file name stored in variable name_of_file

# ex. if file name is example.txt, test function will be named test_example
# So, file input should only have one period '.' in the file name
# to identify file name (example) and file type (.txt)



# type name of file to do word count
name_of_file = "task6_read_me.txt"

# opens the file - used as input for word count function
a_file = open(name_of_file, "r")


# name of file delimited - without file type
name_left_split = name_of_file.rsplit('.')[0]

# file type (.txt, .pdf, etc)
name_file_type = name_of_file.rsplit('.')[1]


# input file object
# typically from function like file = open("example.txt", "r")
def file_word_count(file):

    contents = file.read()
    file.close()                   # close file in case need of re-use
    word_list = contents.split()
    num_words = len(word_list)

    return num_words


# metaprogramming - dynamically named test function
# function is named as test_{name_left_split}
# ex. if file is example.txt, test function is def test_example
# test function applies test to word count function
code = f'def test_{name_left_split}():\n   file=open("{name_of_file}", "r") \n'
'contents = file.read() \n file.close() \n word_list = contents.split() \n'
'expected_num_words = len(word_list)\n test_num_words = file_word_count({a_file})\n'
'assert test_num_words == expected_num_words'


# python built-in function to execute dynamic code
exec(code)

    



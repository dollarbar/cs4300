# This program tests for functionality of control structures - 3 parts
# Part 1 is testing and if-then control structure with the sign of a number
# Part 2 tests for the outcome of a function that calculates the first 10 primes
# - This uses a for-loop in the test function to check for the correctness of all 10 primes
# Part 3 tests for the correct total sum of numbers 1 to n
# - This uses the while loop in the function to be tested
# - simply tests for correct outcome


### Part 1 ###

# function takes a number and should return string "positive", "negative", or "zero"
# based on the sign 
def check_sign_of_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

# test function
def test_sign_of_number():
    assert check_sign_of_number(0.00001) == "positive"
    assert check_sign_of_number(-0.00001) == "negative"
    assert check_sign_of_number(0) == "zero"





### Part 2 ###

# is_prime returns True or False boolean whether or not num is prime
def is_prime(num):
    boolean = False
    divisor = num - 1
    while divisor > 0:
        if divisor == 1:
            boolean = True
            divisor -= 1
        else:
            is_int = (num / divisor ).is_integer()
            if is_int is True:
                divisor = 0
            else:
                divisor -= 1
    return boolean


# nth_prime returns the nth prime number with n as parameter
# ex. 3rd prime number is 7.
def nth_prime(n):
    prime_count = 0
    num = 3
    current_prime = num

    while prime_count < n:
        is_prime_bool = is_prime(num)
        if is_prime_bool:
            prime_count += 1
            current_prime = num
            num += 1
            
        else:
            num += 1
        
    return current_prime


# using list of the first 10 primes, asserts that nth_prime function
# returns the correct 1 to 10 primes.
def test_first_ten_primes():
    first_ten_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for i in range(1, 11):
        assert nth_prime(i) == first_ten_primes[i-1]
        
            

### Part 3 ###

# function returns total sum of numbers 1 to 100
def add_one_to_one_hundred():
    num = 1
    total = 0
    while (num < 101):
        total += num
        num += 1
    return total


def test_one_to_one_hundred():

    # Guass formula total = n(n+1)/2 shows 100(101)/2 should be 5050
    expected_result = 100 * (100 + 1) / 2

    assert add_one_to_one_hundred() == expected_result

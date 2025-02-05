
# part 1
def check_sign_of_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"



def test_positive():
    assert check_sign_of_number(0.00001) == "positive"

def test_negative():
    assert check_sign_of_number(-0.00001) == "negative"

def test_zero():
    assert check_sign_of_number(0) == "zero"



# part 2
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

print(nth_prime(3))




def test_first_ten_primes():
    first_ten_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for i in range(1, 11):
        assert nth_prime(i) == first_ten_primes[i-1]
        
            

def add_one_to_one_hundred():
    num = 1
    total = 0
    while (num < 101):
        total += num
        num += 1
    return total

def test_one_to_one_hundred():
    # Guass formula total = n(n+1)/2 shows 100(101)/2 should be 5050
    assert add_one_to_one_hundred() == 5050

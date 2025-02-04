

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
        
            


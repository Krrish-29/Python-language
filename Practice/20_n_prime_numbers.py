#wap to find first n prime numbers
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
primes = []
n=2
number=0
number_of_primes = int(input("Enter the number of primes numbers needed : "))
while number_of_primes> number:
    if isprime(n):
        number+=1
        primes.append(n)
    n+=1
print(primes)

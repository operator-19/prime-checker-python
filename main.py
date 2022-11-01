
def prime_checker(number):
    isPrime = True
    for i in range(2, number): # looping every number till input
        if number % i == 0: # if number is divisble by the number getting looped
            isPrime = False
    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)




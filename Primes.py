

class Primes:
    """
    generates a list of prime numbers to work with
    the argument initializes the list filling it with prime numbers up to
    the specified number.

    The method prime_factorization does a prime factorization on a given number
    """

    def __init__(self, amount_of_primes=100):
        self.factors = []
        self.prime_numbers = []
        self.generate_primes(amount_of_primes)


    def generate_primes(self, limit):
        """ generates a list of prime numbers up to the provided limit"""

        prime_flag = 0
        for dividend in range(2, limit):
            for divisor in range(2, limit):
                if dividend > divisor:
                    if dividend % divisor == 0:
                        prime_flag = 1
                        break
                else:
                    break
            if prime_flag == 0:
                self.prime_numbers.append(dividend)
                prime_flang = 0
            else:
                prime_flag = 0

        return self.prime_numbers


    def prime_factorization(self, number):
        """ this function gets the prime self.factors of a number
        Arguments: number to factorize, list of prime numbers to compare,
        list to write to"""
        counter = 0
        while number >= 2:
            try:
                if number % self.prime_numbers[counter] == 0:
                    number = number / self.prime_numbers[counter]
                    self.factors.append(self.prime_numbers[counter])
                else:
                    counter += 1
            except IndexError:
                print("couldn't find the factors, "
                "there are not enough primes on the list."
                "Use Primes.generate_primes() to make the list larger")
                break

        return self.factors




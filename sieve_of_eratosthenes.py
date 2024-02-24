# Amir Abu Hani

# create a list called main numbers list for number between 4 and 150
main_number_list = []
for number in range(4, 151):
    main_number_list.append(number)
print(f"The initial main list number is:\n{main_number_list}")
# create a list called prime numbers list for the prime numbers. At first append the numbers 2 and 3
prime_numbers_list = [2, 3]


# This function will extract the prime numbers from the main numbers list using the auxiliary function isPrime
def extract_primes():
    # creating copy of the main_number_list to avoiding skipping elements while iterating the main list
    main_number_list_copy = main_number_list[:]
    for main_number in main_number_list_copy:
        # if the main number is prime
        if isPrime(main_number):
            # The main number enters to the prime list
            prime_numbers_list.append(main_number)
            main_number_list.remove(main_number)
            # And the multiplication of the prime number is removed from the main list
            for i in range(main_number * 2, 151, main_number):
                # Check if the number is existed in the main list, before removed it
                if i in main_number_list_copy:
                    main_number_list_copy.remove(i)


# This function determines whether the number is prime or not according to the prime numbers list
def isPrime(number):
    for prime in prime_numbers_list:
        if number % prime == 0:
            return False
    return True


extract_primes()
# print(isPrime(113))
print(f"The prime numbers list is:\n{prime_numbers_list}")
print(f"The current main number list is:\n{main_number_list}")
prime_list_length = len(prime_numbers_list)
print(f"The length of the prime list is: {prime_list_length}")


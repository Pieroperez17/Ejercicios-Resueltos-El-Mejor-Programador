is_prime = lambda num: all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1

# uso
print(f"2 es primo: {is_prime(2)}")
print(f"10 es primo: {is_prime(10)}")
print(f"17 es primo: {is_prime(17)}")
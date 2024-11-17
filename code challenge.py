# Qn.1 Large power
def large_power(base, exponent):
    # Calculate the power
    result = base ** exponent
    
    # Check if result is greater than 5000
    if result > 5000:
        return True
    else:
        return False
    
    print("Testing large_power:")
print(large_power(10, 3))  # True, since 10^3 = 1000 > 5000
print(large_power(2, 10))  # False, since 2^10 = 1024 <= 5000
print(large_power(5, 5))   # True, since 5^5 = 3125 > 5000

#Qn.2 Divisible by 10
def divisible_by_ten(num):
    # Check if num is divisible by 10
    if num % 10 == 0:
        return True
    else:
        return False
    
    print("\nTesting divisible_by_ten:")
print(divisible_by_ten(50))  # True, divisible by 10
print(divisible_by_ten(33))  # False, not divisible by 10
print(divisible_by_ten(100)) # True, divisible by 10



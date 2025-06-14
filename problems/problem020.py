def solve():
    """
    Find the sum of the digits of the number 100!
    """
    # Start with 1
    digits = [1]
    
    # Multiply by each number from 2 to 100
    for n in range(2, 101):
        carry = 0
        # Multiply each digit by n and handle carries
        for i in range(len(digits)):
            digits[i] = digits[i] * n + carry
            carry = digits[i] // 10
            digits[i] %= 10
        
        # Add any remaining carry as new digits
        while carry > 0:
            digits.append(carry % 10)
            carry //= 10
    
    return sum(digits)


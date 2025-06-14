def number_to_words(n):
    if n == 0:
        return ""
    
    # Dictionary for numbers 1-19
    ones = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
        19: "nineteen"
    }
    
    # Dictionary for tens
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }
    
    result = ""
    
    # Handle thousands
    if n >= 1000:
        result += ones[n // 1000] + " thousand"
        if n % 1000 != 0:
            result += " "
        n %= 1000
        
    # Handle hundreds
    if n >= 100:
        result += ones[n // 100] + " hundred"
        if n % 100 != 0:
            result += " and "
        n %= 100
    
    # Handle tens and ones
    if n >= 20:
        result += tens[n // 10]
        if n % 10 != 0:
            result += "-" + ones[n % 10]
    elif n > 0:
        result += ones[n]
    
    return result

def solve():
    """
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
    how many letters would be used?
    """
    total_letters = 0
    for i in range(1, 1001):
        # Convert number to words and count letters (excluding spaces and hyphens)
        words = number_to_words(i)
        total_letters += len(words.replace(" ", "").replace("-", ""))
    
    return total_letters


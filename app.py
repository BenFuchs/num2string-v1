def num_to_str(n):
    if n < 1 or n > 1000:
        return "Number out of range"
    
    def unit_to_str(unit):
        units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return units[unit]
    
    def teen_to_str(teen):
        teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return teens[teen - 10]
    
    def ten_to_str(ten):
        tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        return tens[ten]
    
    if n == 1000:
        return "one thousand"
    
    result = ""
    
    if n >= 100:
        hundred, n = divmod(n, 100)
        result += unit_to_str(hundred) + " hundred"
        if n > 0:
            result += " and "
    
    if 10 < n < 20:
        result += teen_to_str(n)
    else:
        ten, unit = divmod(n, 10)
        result += ten_to_str(ten)
        if unit > 0:
            if ten > 0:
                result += "-"
            result += unit_to_str(unit)
    
    return result

def print_numbers_as_strings(up_to):
    for i in range(1, up_to + 1):
        print(num_to_str(i))

i = int(input('Please enter a number: '))
print_numbers_as_strings(i)

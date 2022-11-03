
def roman_to_arabic(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i - 1]]:
            arabic += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
        else:
            arabic += roman_dict[roman[i]]
    return arabic

def arabic_to_roman(arabic):
    arabic_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman = ''
    for key in sorted(arabic_dict.keys(), reverse=True):
        while arabic >= key:
            roman += arabic_dict[key]
            arabic -= key
    return roman

#tests for roman_to_arabic function
print(roman_to_arabic('DCCXXIX'))
print(arabic_to_roman(93))
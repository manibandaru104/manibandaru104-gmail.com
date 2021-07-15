def small_numbers(number):
    number_in_english = ""
    if number < 1000 and number >= 100:
        tens = number // 100
        number = number % 100
        number_in_words = below_19_list[tens-1]
        number_in_english += number_in_words + " " + "hundred "
    if number<100 and number>=20:
        tens = number // 10 
        number = number % 10 
        number_in_words = tens_list[tens-2]
        number_in_english += number_in_words 
    if number < 20 and number != 0:
        number_in_words = below_19_list[number-1]
        number_in_english += number_in_words + " "
    return number_in_english
def start_number(number):
    number_in_english = ''
    if number >= 1000000000 and number <= 10000000000:
        req = number // 1000000000
        number = number % 1000000000
        number_in_words = small_numbers(req)
        number_in_english += number_in_words +"billion "
    if number >=1000000 and number < 1000000000:
        req = number // 1000000 
        number = number % 1000000
        number_in_words = small_numbers(req)
        number_in_english += number_in_words + "million "
    if number < 1000000 and number >= 1000:
        req = number // 1000 
        number = number % 1000 
        number_in_words = small_numbers(req)
        number_in_english += number_in_words + "thousand "
    if number < 1000 and number > 0:
        number_in_english +=small_numbers(number)
    
    return number_in_english

number = int(input())
number_in_english = ''
below_19_list= ["one", "two", "three", "four", "five", "six", "seven dollars", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_list = ["twenty-", "thirty-", "forty-", "fifty-", "sixty-", "seventy-", "eighty-", "ninety-"]
number_in_english = start_number(number)
print(number_in_english)
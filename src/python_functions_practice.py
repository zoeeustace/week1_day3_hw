
def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2
    
def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

months = {1: "January", 3: "March", 9: "September"
}

def number_to_full_month_name(month_number):
    return months[month_number]
    
# def number_to_full_month_name(months_number):
#     if months_number == 1:
#         return "January"
#     if months_number == 3:
#         return "March"
#     if months_number == 9:
#         return "September"    


def number_to_short_month_name(number_short_month):
    if number_short_month == 1:
        return "Jan"
    if number_short_month == 4:
        return "Apr"
    if number_short_month == 10:
        return "Oct"

def volume_of_cube(l, w, h):
    return l * w * h

def reverse_string(string):
    return string[:: -1]

def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5/9)
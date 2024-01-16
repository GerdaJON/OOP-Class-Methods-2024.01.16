# 2024.01.16
# Exercises:

# 1. Create a class method to return the factorial of a given number.
class MyClass:
    @classmethod
    def factorial(cls, number):
        if number < 0:
            raise ValueError('Number must be a non-negative.')
        if number == 0 or number == 1:
            return 1
        else:
            return number * cls.factorial(number - 1)

given_number = MyClass()
print(given_number.factorial(8))
print(given_number.factorial(18))
print(given_number.factorial(7))
print(given_number.factorial(1))


# 2. Create a class method to return the reversed string of a given string.

class OtherClass:
    @classmethod
    def return_reversed_string(cls, string):
        reversed_string = string[::-1]
        return reversed_string


print(OtherClass.return_reversed_string('Hello there!'))
print(OtherClass.return_reversed_string('Gerda'))

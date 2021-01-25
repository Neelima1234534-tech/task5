class LengthError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

number = input('Enter any 4 digit number\n')
try:
    if(len(number) == 4):
        print('You entered ',number)
    else:
        raise LengthError('The length is too short/long!!! please provide only four digits')
except LengthError as err:
    print(err.value)
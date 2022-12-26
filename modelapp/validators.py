from django.forms import ValidationError
def first_letter(value):
    if not(value[0].isupper()):
        raise ValidationError(f'the first letter of {value} should be uppercase')


def Minchar(value):
    if len(value)<8:
        raise ValidationError(f'the minimum number of char should be more than 5')
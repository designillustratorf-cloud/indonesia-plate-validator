import re

def regex_validate(plate):
    pattern = r'^[A-Z]{1,2}\s?[0-9]{1,4}\s?[A-Z]{1,3}$'
    return bool(re.fullmatch(pattern, plate.upper()))
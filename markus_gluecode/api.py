import re

# TODO replace this with actual text from paigo OCR
text = "Markus Stahl\n\nSpitalstraße 4\n\n64807 Dieburg"

address_regex = r'(?P<name>.*)\n*(?P<street>.*)\n*(?P<town>.*)'

matcher = re.search(address_regex, text)

person = matcher.group('name')
street = matcher.group('street')
town = matcher.group('town')

print(f'Tokens:\nName: {person}\nStreet: {street}\nTown: {town}')
import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o telefone no formato: (+Código do pais)ddd-número do telefone: ')

phone_number = phonenumbers.parse(phone)

print('A localidade do número de telefone informado é: '+geocoder.description_for_number(phone_number,'pt'))
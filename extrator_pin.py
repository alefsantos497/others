#Função para extrair os códigos pin de uma lista de poesias
from pin_extractor import pin_extractor
#Exemplo de uso da função pin_extractor
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'
#Imprime os códigos pin extraidos
print(pin_extractor([poem,poem2,poem3]))


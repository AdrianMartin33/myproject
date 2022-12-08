
def search4letters(phrase:str, letters:'aeiou')->set:
  """ Función que busca las letras en una palabra y las imprime"""
  return( set(letters).intersection(set(phrase)))
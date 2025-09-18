import re 

string = "Contando Las Mayúsculas y Minúsculas con Signos Especiales! 123!"

Mayusculas_letras = re.findall(r'[A-Z]', string)
Minusculas_letras = re.findall(r'[a-z]', string)
signos_especiales = re.findall(r'[! , ?]', string)
numeros_aqui = re.findall(r'[0-9]', string)

print("Total mayúsculas:", len(Mayusculas_letras))
print("Total minúsculas:", len(Minusculas_letras))
print("Total signos especiales:", len(signos_especiales))
print("numeros_aqui:", len(numeros_aqui))

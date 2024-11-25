import os

#with open('contatore_cartelle.txt', 'r') as file:
#    valore = file.read()
#valore = int(valore)
#
#print(valore)
#
##for i in range(valore): #INFINITO
#valore = valore + 1
i = 20
os.system(f"mkdir arlotti_es{i}") #crea cartella esercizio
with open(f'arlotti_es{i}/arlotti_esercizio_python_numero_{i}.py', 'w') as file_da_creare: #crea file python
    file_da_creare.write("")
with open(f'arlotti_es{i}/arlotti_puml_numero_{i}.puml', 'w') as file_da_creare: #crea flie puml
    file_da_creare.write("")
with open('contatore_cartelle.txt', 'w') as file:
    valore = file.write("valore")
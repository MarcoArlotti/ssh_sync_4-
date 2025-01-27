import os

i = 26 #numero esercizio da preimpostare
os.system(f"mkdir arlotti_es{i}") #crea cartella dell'esercizio
with open(f'arlotti_es{i}/arlotti_esercizio_python_numero_{i}.py', 'w') as file_da_creare: #crea esercizio in python
    file_da_creare.write("")

with open(f'arlotti_es{i}/arlotti_uml_numero_{i}.md', 'w') as file_da_creare: #crea file uml
    file_da_creare.write("")

with open(f'arlotti_es{i}/{i}.md', 'w') as file_da_creare: #crea file uml
    file_da_creare.write("")

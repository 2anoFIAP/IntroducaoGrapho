'''amizades = {
    "Maria": ["João", "Pedro", "Ana", "NaN"],
    "João": ["Maria", "Pedro", "Lucas", "NaN"],
    "Pedro": ["Maria", "João", "Ana", "Lucas"],
    "Ana": ["Maria", "Pedro", "Clara", "NaN"],
    "Lucas": ["João", "Pedro", "NaN", "NaN"],
    "Clara": ["Ana", "NaN", "NaN", "NaN"]
}

comuns = set(amizades["Maria"]) & set(amizades["João"])

import pandas as pd

df = pd.DataFrame(amizades)
print(df.head())'''

#1
amizades = {
    "Maria": ["João", "Pedro"],
    "João": ["Maria", "Pedro", "Lucas"],
    "Pedro": ["Maria", "João", "Ana", "Lucas"],
    "Ana": ["Maria", "Pedro", "Clara"],
    "Lucas": ["João", "Pedro"],
    "Clara": ["Ana"]
}
comuns = set(amizades["Pedro"]) & set(amizades["Ana"])
diferenca = set(amizades["Pedro"]) - set(amizades["Ana"])
uniao = set(amizades["Pedro"]) | set(amizades["Ana"])

print(diferenca)
print(uniao)

#2
materiais = {
"Projeto1": {"madeira", "cola", "tinta", "pregos", "verniz"},
"Projeto2": {"cola", "papel", "tinta", "lixa", "verniz"}, "Projeto3": {"madeira", "papelão", "parafusos", "cola quente"}, "Projeto4": {"cimento", "areia", "tinta", "cola"},
"Projeto5": {"papel", "papelão", "cola", "tinta", "pregos"},
"Projeto6": {"madeira", "lixa", "parafusos", "cimento"},
"Projeto7": {"papelão", "cola quente", "tinta", "areia"},
}


comuns2 = materiais["Projeto1"] & materiais["Projeto2"]
print(f"Materiais comuns entre Projeto1 e Projeto2: {comuns}")

exclusivos = materiais["Projeto3"] - materiais["Projeto1"]
print(f"Materiais exclusivos de Projeto3 (em relação a Projeto1):{exclusivos}")


uniao = materiais["Projeto2"] | materiais["Projeto5"]
print(f"Materiais presentes em pelo menos um dos dois projetos:{uniao}")

comuns_tres = materiais["Projeto1"] & materiais["Projeto2"] & materiais["Projeto5"]
print(f"Materiais comuns aos três projetos: {comuns_tres}")


vistos = set()
repetidos = set()
for materiais_do_projeto in materiais.values():

	for material in materiais_do_projeto:
		if material in vistos: repetidos.add(material)
	else:
		vistos.add(material)
	print(f"Materiais usados em pelo menos dois projetos: {repetidos}")
amizades = {
    "Maria": ["João", "Pedro", "Ana"],
    "João": ["Maria", "Pedro", "Lucas"],
    "Pedro": ["Maria", "João", "Ana", "Lucas"],
    "Ana": ["Maria", "Pedro", "Clara"],
    "Lucas": ["João", "Pedro"],
    "Clara": ["Ana"]
}

comuns = set(amizades["Maria"]) & set(amizades["João"])

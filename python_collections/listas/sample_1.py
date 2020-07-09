import copy

estudantes = ["Eliseu", "Alexandre", "Witney"]
turma_a = copy.deepcopy(estudantes)
turma_a.append("Vilse")
print(estudantes)
print(turma_a)

informatica = copy.copy(turma_a)
estudantes.append("Braune")
print(informatica)

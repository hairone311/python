estudantes = []
estudantes.append("Eliseu Hairone")
estudantes.append("Alexandre Inacio")
estudantes.append("Momed Ossufo")
estudantes.append("Tonecas Antonio")
estudantes.append("Braune Paulo")
estudantes.sort()

print(estudantes)

estudantes.remove("Momed Ossufo")
print(estudantes)

estudantes.insert(1, "Adelina Luis")
print(estudantes)

indice = estudantes.index("Eliseu Hairone")
print(indice)

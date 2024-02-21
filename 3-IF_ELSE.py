# Estruturas Condicionais

# ---------- IF and ELSE ----------------------------

nota_av1 = 7

if nota_av1 >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")

# ---------- IN --------------------------------------
notas_lancadas = [154, 176, 234, 654, 2343]

if 154 in notas_lancadas:
    print("Nota lançada")
else:
    print("Nota não lançada")

# ------------- Exercicio --------------------------

av1 = float(input("Nota av1: "))
av2 = float(input("Nota av2: "))
media = (av1 + av2) / 2

if media >= 7:
    print(f"Aluno aprovado com media: {media}")
else:
    print(f"ALuno reprovado com media: {media}")

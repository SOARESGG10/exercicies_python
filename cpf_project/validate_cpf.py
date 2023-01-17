from random import randint


def generate_cpf():
    generated_cpf = ""
    for _ in range(0, 11):
        generated_cpf += str(randint(0, 9))
    return generated_cpf

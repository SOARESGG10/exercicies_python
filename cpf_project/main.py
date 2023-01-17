from check_cpf import get_cpf, generate_cpf

amount_user = input("Inform how many cpfs you want to generate: ")


with open("cpf_project/cpf.txt", "w+") as file:
    for amount in range(0, int(amount_user) + 1):
        output = get_cpf(generate_cpf())
        file.write(f"CPF: {output}\n")
    print(f"Operação concluída com sucesso. Foram gerados {amount_user} CPS's")

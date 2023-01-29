from check_cpf import get_cpf
from validate_cpf import generate_cpf
from functionalities import check_is_exists_folder, random_digits, clean_terminator

check_is_exists_folder()

while True:
    get_time_now, get_random_digits = random_digits()
    amount_user = input("Inform how many cpfs you want to generate: ")

    while not amount_user.isdecimal():
        clean_terminator()
        print("* This is a not number!!\n")
        amount_user = input("Inform how many cpfs you want to generate: ")

    with open(f"cpfs/{get_time_now}_{get_random_digits}.txt", "w+") as file:
        for amount in range(0, int(amount_user)):
            output = get_cpf(generate_cpf())
            file.write(f"CPF: {output}\n")
        print(f"\nOperation completed successfully. {amount_user} CPS's were generated.\n")

    option = input("Do you want to continue?(y/n): ")
    if option in ["n", "N"]:
        clean_terminator()
        print("* BYE, BYE. Close program.")
        break
    elif option in ["y", "Y"]:
        clean_terminator()
        continue
    else:
        while option not in ["n", "N", "y", "Y"]:
            clean_terminator()
            print("\nInvalid option.\n")
            option = input("Do you want to continue?(y/n): ")
            clean_terminator()
        continue

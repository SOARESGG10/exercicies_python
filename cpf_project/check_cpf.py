from re import sub


def clean_cpf(val):
    return sub(r"\D+", "", val)


def check_sequence(cpf):
    get_is_sequence = cpf[0] * len(cpf)
    return True if get_is_sequence == cpf else False


def get_cpf(cpf):
    get_clean_cpf = clean_cpf(cpf)

    if check_sequence(get_clean_cpf):
        return "CPF inválido. Você informou uma sequência."

    get_part_cpf = get_clean_cpf[0:9]
    get_first_check_digit = check_digits(get_part_cpf)
    get_second_check_digit = check_digits(get_part_cpf + get_first_check_digit)
    get_verified_cpf = get_part_cpf + get_first_check_digit + get_second_check_digit
    return get_verified_cpf


def check_digits(cpf):
    get_inverted_cpf = cpf[::-1]
    get_total_cpf = 0
    for index, number in enumerate(get_inverted_cpf):
        get_total_cpf += (index + 2) * int(number)
    get_total_remained_cpf = (get_total_cpf * 10) % 11
    return str(get_total_remained_cpf) if get_total_remained_cpf <= 9 else "0"

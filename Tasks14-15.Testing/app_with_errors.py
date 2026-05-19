def process_string_buggy(data):
    # ERROR 1: Проверяется только первый символ, а не вся строка
    if len(data) > 0 and data[0].isdigit(): 
        return 0
    
    # ERROR 2: Опечатка в имени метода подсчета (.cont вместо .count)
    try:
        count_k = data.cont('k') 
        count_m = data.count('m')
        return {"k": count_k, "m": count_m}
    except AttributeError:
        return "System Error"

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    print(process_string_buggy(user_input))
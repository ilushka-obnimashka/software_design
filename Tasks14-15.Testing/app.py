
def process_string(data):
    # Проверяем наличие цифр во всей строке
    if any(char.isdigit() for char in data):
        return 0
    
    # Считаем символы 'k' и 'm'
    count_k = data.count('k')
    count_m = data.count('m')
    
    return {"k": count_k, "m": count_m}

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    print(process_string(user_input))
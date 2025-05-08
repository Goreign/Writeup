FUNCTIONS = {
    '1': ('Hex to String', 'hex_to_string'),
    '2': ('Count Letters for a String', 'count_letters'),
    '3': ('Dec <--> Hex', 'dec_hex_convert'),
}

func_table = {}

def update_func_table():
    for key, (desc, func_name) in FUNCTIONS.items():
        func_table[key] = (desc, globals()[func_name])

def hex_to_string():
    print('Enter hex such as 0x66 0x6c 0x61 0x67')
    text = input('==> ')
    flag = ""
    try:
        for s in text.split(' '):
            flag += bytes.fromhex(s[2:]).decode()
        print('\nEncoded String:\n', flag)
    except ValueError:
        print('Error -  enter valid hex values in the format 0xXX')


def count_letters():
    print('Enter a string to count the number of characters')
    s = input('==> ')
    print(f'count: {len(s)}')

def dec_hex_convert():
    user_input = input('==> ').strip()

    if user_input.lower().startswith('0x'):
        decimal_value = int(user_input, 16)
        print(f'\nHex: {user_input} \nDec: {decimal_value}')
    else:
        try:
            decimal_value = int(user_input)
            hex_value = hex(decimal_value)
            print(f'\nDec: {decimal_value} \nHex: {hex_value}')
        except ValueError:
            print("Input Error")

update_func_table()

def check_functions():
    print('Available Functions:')
    for key, (desc, _) in func_table.items():
        print(f"{key}. {desc}")

def agent():
    USER_ALIVE = True
    while(USER_ALIVE):
        choice = input('\nEnter Function Index ==> ')
        if choice in ['quit', 'exit', 'q']:
            USER_ALIVE = False
        elif choice in ['help', '?']:
            check_functions()
        elif (choice in func_table):
            func_table[choice][1]()
        else:
            print("Try '?' or 'help'")


if __name__ == "__main__":
    agent()

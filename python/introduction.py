import os

def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def function_print():
    print('Hello, world!')
    print("Hello, world with double quotes")
    print()
    print('Hello\nWorld!')

def function_comment():
    print("To comment on code, you can use # or 3 single quotes or 3 double quotes, like on code below:")
    # this is a comment
    
    '''
    This
    is
    a
    comment
    also
    '''
    
    """
    And
    this
    """

def function_math_operations():
    print('1 + 1 =', 1 + 1) # sum
    print('3 - 1 =', 3 - 1) # subtraction
    print('10 / 3 =', 10 / 3) # division
    print('5 * 2 =', 5 * 2) # multiplication
    print('2³ =', 2 ** 3) # exponentiation
    print('10 / 4 =', 10 % 4) # remainder
    print("'5' * 2 =", 5 * '2') # multiplication with string

def function_variables_types():
    print(type(1))
    print(type(1.2))
    print(type('a'))
    print(type(True))
    print(type([1,2,3]))

def function_list():
    numbers = [1, 2, 3, 4, 5]
            #  0  1  2  3  4 -> positive position
            #  0 -4 -3 -2 -1 -> negative position
    
    print(numbers[0])
    print(numbers[4])
    print(numbers[-1])
    
    numbers.append(6)
    numbers.remove(3)
    
    print(numbers)
    
    for number in numbers:
        print(number)
    
    colors = ['blue', 'yellow', 'red', 'green']
    
    if 'Blue' in colors:
        print('Blue is in the list!')
    else:
        print("Blue ins't in the list.")
        
        for color in colors:
            print(color)

def function_type_checking():
    print('Blue' == 'blue')
    print('Blue' != 'blue')
    print(5 > 5)
    print(5 < 5)
    print(5 >= 5)
    print(5 <= 5)

def function_random_game():
    import random
    
    secret_number = random.randint(1, 1000)
    tries = 0
    
    while True:
        try_number = int(input('Enter a number between 1 and 1000: '))
        tries += 1
        
        if try_number == secret_number:
            break
        elif try_number > secret_number:
            print('Try a smaller number.')
        else:
            print('Try a biggest number.')
    
    print(f'Congratulations! You guessed the {secret_number} that was the secret number in {tries} attempts.')

def function_api():
    import requests
    
    api_return = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    dollar = api_return.json()
    dollar = float(dollar['USDBRL']['bid'])
    real = float(input('(R$): '))
    result = real / dollar
    
    print(f'(US$): {result:.2f}')

def function_register_with_list():
    products_list = []
    
    while True:
        name = input('Product name: ')
        category = input('Category: ')
        price = input('Price (US$): ') # For decimal values, use a . in this field.
        
        products_list.append({
            'name': name,
            'category': category,
            'price': price
        })
        
        continue_registration = input('Do you want to register another product? (y/n)')
        
        if continue_registration.lower() != 'y':
            break
    
    print('Registered products:')
    for product in products_list:
        print(f"Product name: {product['name']} | Category: {product['category']} | Price: {product['price']}")

def function_generate_json():
    import json
    
    products_list = []
    
    while True:
        name = input('Product name: ')
        category = input('Category: ')
        price = input('Price (US$): ') # For decimal values, use a . in this field.
        
        products_list.append({
            'name': name,
            'category': category,
            'price': price
        })
        
        continue_registration = input('Do you want to register another product? (y/n)')
        
        if continue_registration.lower() != 'y':
            break

    with open('products.json', 'w', encoding='utf-8') as archive:
        json.dump(products_list, archive, ensure_ascii=False, indent=4)

    print('Registered products:')
    for product in products_list:
        print(f'Product name: {product['name']} | Category: {product['category']} | Price (US$): {product['price']}')
    
    print("Check the generated JSON file in the 'python' folder.")

def function_display_menu():
    var_selected_option = input("\n---------- Menu ----------\n"
                                "Choose an option:\n"
                                "[01] - print a message on terminal\n"
                                "[02] - comment on code\n"
                                "[03] - math operations\n"
                                "[04] - variables types\n"
                                "[05] - list variable\n"
                                "[06] - type checking\n"
                                "[07] - random game\n"
                                "[08] - request an API\n"
                                "[09] - products register with list\n"
                                "[10] - generate .JSON\n"
                                "[11] - exit\n")
    return var_selected_option

def function_navigation_menu(param_selected_option):
        clear_terminal()
        if param_selected_option == '1' or param_selected_option == '01':
            function_print()
        elif param_selected_option == '2' or param_selected_option == '02':
            function_comment()
        elif param_selected_option == '3' or param_selected_option == '03':
            function_math_operations()
        elif param_selected_option == '4' or param_selected_option == '04':
            function_variables_types()
        elif param_selected_option == '5' or param_selected_option == '05':
            function_list()
        elif param_selected_option == '6' or param_selected_option == '06':
            function_type_checking()
        elif param_selected_option == '7' or param_selected_option == '07':
            function_random_game()
        elif param_selected_option == '8' or param_selected_option == '08':
            function_api()
        elif param_selected_option == '9' or param_selected_option == '09':
            function_register_with_list()
        elif param_selected_option == '10':
            function_generate_json()
        elif param_selected_option == '11':
            return 'exit'
        else:
            print('Invalid option. Try again.')
        return None

def main():
    while True:
        var_selected_option = function_display_menu()
        navigation_controll = function_navigation_menu(var_selected_option)
        if navigation_controll == 'exit':
            print("Exiting the program. Goodbye!")
            break
    
if __name__ == '__main__':
    main()
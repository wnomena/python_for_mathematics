simple_binary_value:str = None
reseult_binary_par_four_group:str = None
x:int = 0
try:
    b = int(input("Entrer la base de votre nombre : "))
    x = b
except:
    print("Vueillez respecter les criteres demandé")
    while 1:
        try :
            c = int(input("Entrer la base de votre  nombre : "))
            if int(c) == 2 or int(c) == 8 or int(c) == 16:
                x = c
        except:
            print("\n")
def converter_to_hexa_or_octa(d):
    base_to_convert_out_try:int = None
    try:
        base_to_convert = int(input("Entrer la base sur lequel on va le convertir (8/16) : " ))
        if base_to_convert == 8 or base_to_convert == 16:
            base_to_convert_out_try = base_to_convert
        else:
            print("Veuillez respecter les criteres")
            while 1:
                try:
                    base = int(input("Entrer la base sur lequel on va le convertir (8/16) : "))
                    if base == 8 or base == 16:
                        base_to_convert_out_try = base
                        break
                except:
                    print("Veuillez respecter les criteres")
    except:
        print("Veuillez respecter les criteres")
        while 1:
            try:
                base = int(input("Entrer la base sur lequel on va le convertir (8/16) : "))
                if base == 8 or base == 16:
                    base_to_convert_out_try = base
                    break
            except:
                print("Veuillez respecter les criteres")
    print(base_to_convert_out_try)
    print(d)
    variable:int = 0
    
    #Boucle pour grouper les valeur par 4 ou  3 selon le choix de pas de l'utilisateur
    #trouver les valeurs octal ou decimal correspondant selon les donnes    
    
        
def convert_value_to_decimal(a:str):
    decimal_value:int = 0
    input_value:int = 0
    try:
        input_value_for_try = int(input("Entrer le nombre à convertir : "))
        input_value = input_value_for_try
    except:
        while 1:
            print("Veuillez respecter les criteres")
            try:
                input_value_for_try = int(input("Entrer le nombre à convertir : "))
                if str(type(input_value_for_try)) == "<class 'int'>":
                    input_value = input_value_for_try
                    break
            except:
                print("\n")
            
    b:int = len(str(input_value))
    for i in range(0,b):
        # print(decimal_value)
        decimal_value += int(str(input_value)[::-1][i]) * int(a)**i
    print(decimal_value)
    return decimal_value
def convert_value_of_fonction_into_binary(x:int):
    binary_one_by_one:str = "0"
    temporary_value:int = x
    while int(temporary_value) != 0:
        temporary_value /= 2
        binary_one_by_one += str(int(temporary_value % 2))
    return binary_one_by_one[::-1]
print(converter_to_hexa_or_octa(convert_value_of_fonction_into_binary(int(convert_value_to_decimal(int(x))))))
        
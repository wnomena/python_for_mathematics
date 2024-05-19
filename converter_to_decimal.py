print("____________To_Decimal_converter____________")
inpu:int = None
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
    return decimal_value
            
    
def input_and_recusrsivity_function():
    inpu = input("Entrer la base de votre  nombre : ")
    # print(type(int(inpu)))
    # print(type(5))
    if int(inpu) == 2 or int(inpu) == 8 or int(inpu) == 16:
        return inpu
    else:
        print("Veuillez entrer un base valide")
        input_and_recusrsivity_function()
try:
    inpu = input_and_recusrsivity_function()
except:
    print("Veuillez respecter les critères demandé")
    while 1:
        try:
            value_of_except = input_and_recusrsivity_function()
            if int(value_of_except) == 2 or int(value_of_except) == 8 or int(value_of_except) == 16:
                inpu = value_of_except
                break
        except:
            print("Veuillez respecter les critères demandé")
# print(inpu)
print(f"Resultat du calcul : {convert_value_to_decimal(str(inpu))}")
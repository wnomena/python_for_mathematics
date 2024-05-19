import math
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
def trouveer_la_valeur_respective_apre_regroupement_binaire(a:str,choice:int):
    valeur_apres_division_apres:str = None
    #Boucle qui me permet voir la verion decimal des valeur trier par trois ou 4 et le rendre avec return

def regroupement_des_valeur_selon_le_choix_de_l_utilisateur(choice,d):
    value_separated:str = None
    print(f"choice :  { choice }")
    know_if_there_are_value_not:int = int(len(d)%int(math.ceil(math.sqrt(choice))))
    print(f"know_if_there_are_value_not : {int(math.ceil(math.sqrt(choice)))}")
    for i in range(0,int(math.ceil(math.sqrt(choice))) - know_if_there_are_value_not):
        if value_separated == None:
            value_separated = "0"
        else:
            value_separated =  "0" + value_separated
    print(value_separated)
    if value_separated == None:
        value_separated = str(d)
    else:
        value_separated = str(value_separated) + str(d)
    print(f"{value_separated} : {len(value_separated)}")
    print(int(len(value_separated)/int(math.ceil(math.sqrt(choice)))))
    value_after_loop_in_binary_before_final_result = None
    z = len(value_separated) - 1
    print(f"len(value_separated) : {len(value_separated)}")
    for i in range(0,int(len(value_separated)/int(math.ceil(math.sqrt(choice))))):
        for x in range(z, int(z - int(math.ceil(math.sqrt(choice)))) , -1):
            try:
                # print(f"value_separated[i] : {value_separated[x]}")
                if value_after_loop_in_binary_before_final_result == None:
                    value_after_loop_in_binary_before_final_result = value_separated[x]
                else:
                    value_after_loop_in_binary_before_final_result = value_separated[x] + value_after_loop_in_binary_before_final_result
                    z = z - int(math.ceil(math.sqrt(choice)))
            except IndexError:
                value_after_loop_in_binary_before_final_result = "0" + value_after_loop_in_binary_before_final_result
                break
        value_after_loop_in_binary_before_final_result = " " + value_after_loop_in_binary_before_final_result
    print(value_after_loop_in_binary_before_final_result)
    print(f"len(value_after_loop_in_binary_before_final_result.split( )) : {len(value_after_loop_in_binary_before_final_result.split( ))}")
    enfin_resultat_final_en_octal_ou_hexadecimal:str = None
    for a in range(0,len(value_after_loop_in_binary_before_final_result.split( ))):
        print(f"a : {a}")
        print(f"int(value_after_loop_in_binary_before_final_result.split( )[a]) : {int(value_after_loop_in_binary_before_final_result.split( )[a])}")
        if enfin_resultat_final_en_octal_ou_hexadecimal == None:
            enfin_resultat_final_en_octal_ou_hexadecimal = str(trouveer_la_valeur_respective_apre_regroupement_binaire(value_after_loop_in_binary_before_final_result.split( )[a],int(choice)))
        else:
            enfin_resultat_final_en_octal_ou_hexadecimal = enfin_resultat_final_en_octal_ou_hexadecimal + str(trouveer_la_valeur_respective_apre_regroupement_binaire(int(value_after_loop_in_binary_before_final_result.split( )[a]),int(choice)))
    print(enfin_resultat_final_en_octal_ou_hexadecimal)
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
    # print(base_to_convert_out_try)
    # print(d)
        
    regroupement_des_valeur_selon_le_choix_de_l_utilisateur(int(base_to_convert_out_try),str(d))
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
    # print(decimal_value)
    return decimal_value
def convert_value_of_fonction_into_binary(x:int):
    binary_one_by_one:str = "0"
    temporary_value:int = x
    while int(temporary_value) != 0:
        temporary_value /= 2
        binary_one_by_one += str(int(temporary_value % 2))
    return binary_one_by_one[::-1]
print(converter_to_hexa_or_octa(convert_value_of_fonction_into_binary(int(convert_value_to_decimal(int(x))))))
        
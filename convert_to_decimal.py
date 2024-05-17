#convert decimal number into binary
input:int = input(": ")
temporary_value:int = input
binary_value_in_function:int = []
def do_something_to_get_binary_value(n:int):
    binary_value_in_function.append(int(n)%2)
    return int(n)/2
while temporary_value != 0:
    temporary_value = int(do_something_to_get_binary_value(int(temporary_value)))
    print(int(temporary_value))
print(binary_value_in_function)
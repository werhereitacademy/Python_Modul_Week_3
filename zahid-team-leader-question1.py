from base_class import base_class
base_function = base_class()

try:
    menu_list = base_function.menu_list()
    for menu in menu_list:
        print(f"{menu["text"]}\n")
except Exception as e:
    print(e)
try:
    menu_choice = int(input("Please Select from above menu "))
    if(menu_choice == 1):
        print(base_function.add_new_task())
    elif(menu_choice == 2):
        print(base_function.complete_task())
    elif(menu_choice == 3):
        print(base_function.delete_task())
    elif(menu_choice == 4):
        print(base_function.view_list_task())
except Exception as e:
        print("You selected Wrong option")
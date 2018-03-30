import os

# make a list to hold onto our items
shopping_list = []

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def show_help():
    # print out instructions on how to use the app
    print(" {}".format("-"*55))
    print("""|   What should we pick up at the store?                |
|   Enter 'DONE' to stop adding items.                  |
|   Enter 'SAVE' to stop adding items.                  |
|   Enter 'HELP' to show help messages.                 |
|   Enter 'SHOW' to see what your list contains.        |""")
    print(" {}".format("-"*55))

def show_list():
    clear_screen()
    # print out the list
    print("Here's your list:")
    index = 1
    print(" {}".format("-"*20))
    for item in shopping_list:
        print("| {}. {} {} |".format(index, item, int((int(14)-int(len(item))))*" "))
        index += 1
    print(" {}".format("-"*20))


def save_list(shopping_list):
    final_shopping_list = []
    index = 1
    for item in shopping_list:
        items = str("| {}. {} {} |".format(index, item, int((int(14)-int(len(item))))*" "))
        final_shopping_list.append(items)
        index += 1
    #string1 = ", ".join(final_shopping_list)
    
    with open("shopping_list_file.txt", "w") as file:
            file.write(" {}\n".format("-"*20))
    for item_1 in final_shopping_list:
        with open("shopping_list_file.txt", "a") as file:
            file.write(item_1+"\n")
    with open("shopping_list_file.txt", "a") as file:    
        file.write(" {}\n".format("-"*20))
    #print(string1)
    
    

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)

def main():
    # Clear your screen
    clear_screen()
    show_help()
    while True:
        # ask for new items
        new_item = input("> ")
        
        # be able to quit the app
        if new_item.upper() == 'DONE':
            show_list()
            save_list(shopping_list)
            break
        if new_item.upper() == 'SHOW':
            show_list()
            continue
        if new_item.upper() == 'HELP':
            show_help()
            continue
        if new_item.upper() == 'SAVE':
            save_list(shopping_list)
            continue
        add_to_list(new_item)
        
        
main()
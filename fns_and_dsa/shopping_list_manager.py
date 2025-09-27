def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter the item to add: ").strip()
            shopping_list.append(add_item)
        elif choice == '2':
            remove_item = input("Enter the item to remove: ").strip()
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print("The menus you selected is not in the shopping list")
        elif choice == '3':
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
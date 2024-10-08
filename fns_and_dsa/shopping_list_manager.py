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

            new_item = input("Enter the item to add: ")
            shopping_list.append(new_item)
            pass

        elif choice == '2':
            item_to_delete = input("enter the item to delete:").lower()

            for index, item in shopping_list:
                if item == item_to_delete:
                    shopping_list.remove(item)
                else:
                    print("item not found")
            pass

        elif choice == '3':
            for item in shopping_list:
                print(item)
            pass

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
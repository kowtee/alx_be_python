# shopping_list_manager.py
# A simple menu-driven program to manage a shopping list using Python lists.

def display_menu():
    """Prints the menu options for the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []   # start with an empty list

    while True:          # loop until the user chooses to exit
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Add an item
            item = input("Enter the item to add: ").strip()
            if item:  # avoid adding empty strings
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("No item entered. Nothing added.")

        elif choice == '2':
            # Remove an item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' was not found in the shopping list.")

        elif choice == '3':
            # View the current list
            if shopping_list:
                print("\nYour Shopping List:")
                for i, product in enumerate(shopping_list, start=1):
                    print(f"{i}. {product}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

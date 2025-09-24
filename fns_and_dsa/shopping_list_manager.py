# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # empty list

    while True:
        display_menu()  # show menu each time
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number (1-4).")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added.")
            else:
                print("No item entered.")
        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed.")
            else:
                print(f"'{item}' not found.")
        elif choice == 3:
            if shopping_list:
                print("Current shopping list:")
                for i, thing in enumerate(shopping_list, 1):
                    print(f"{i}. {thing}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid number. Please choose 1–4.")

if __name__ == "__main__":
    main()

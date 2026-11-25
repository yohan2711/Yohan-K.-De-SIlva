shopping_list = []

while True:
    print("\n--- Shopping List Menu ---")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Show the list")
    print("4. Count the items")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to the list.")

    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from the list.")
        else:
            print(f"'{item}' was not found in the list.")

    elif choice == "3":
        print("\nYour Shopping List:")
        if len(shopping_list) == 0:
            print("The list is currently empty.")
        else:
            for item in shopping_list:
                print(f"- {item}")

    elif choice == "4":
        print(f"Total items in list: {len(shopping_list)}")

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

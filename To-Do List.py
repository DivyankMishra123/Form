# Create your daily to-do list
print("----Welcome to your Daily To-Do List----")

works = []

while True:
    work = input("Enter your Daily tasks (Press q to quit): ").strip()

    if work.lower() == "q":
        break
    elif work == "":
        print("Work cannot be empty!")
    elif work.lower() in [w.lower() for w in works]:
        print("This work already exists!")
    else:
        works.append(work)

# Display Result
while True:
    print("\n---Your Daily Task List---")

    if len(works) == 0:
        print("No work in your To-Do List!")
    else:
        for i, work in enumerate(works, start=1):
            print(f"{i}. {work}")

    print()
    print("Press 1 --> Add new work")
    print("Press 2 --> Edit work")
    print("Press 3 --> Delete work")
    print("Press 4 --> Count total work")
    print("Press 5 --> Exit")

    choice = input("Enter your choice: ").strip()

    # Add new work
    if choice == '1':
        while True:
            work_1 = input("Enter new work (Press q to quit): ").strip()

            if work_1.lower() == "q":
                break
            elif work_1 == "":
                print("Work cannot be empty!")
            elif work_1.lower() in [w.lower() for w in works]:
                print("This work already exists!")
            else:
                works.append(work_1)
                print("Your new work added successfully!")

        print()

    # Edit work
    elif choice == '2':
        Old_work = input("Enter your work to be edited: ").strip()

        index = next(
            (i for i, w in enumerate(works)
             if w.lower() == Old_work.lower()),
            -1
        )

        if index != -1:
            New_work = input("Enter the new work: ").strip()

            if New_work == "":
                print("Work cannot be empty!")

            elif New_work.lower() in [
                w.lower() for i, w in enumerate(works) if i != index
            ]:
                print("This work already exists!")

            else:
                works[index] = New_work
                print("Your work is edited successfully!")

        else:
            print("This work is not present in your To-Do List!")

        print()

    # Delete work
    elif choice == '3':
        work = input("Enter the work to delete: ").strip()

        index = next(
            (i for i, w in enumerate(works)
             if w.lower() == work.lower()),
            -1
        )
        if index != -1:
            works.pop(index)
            print("Your work is deleted successfully!")
        else:
            print("This work is not present in your To-Do List!")

        print()

    # Count the work
    elif choice == '4':
        print("The total number of work in the list is", len(works))
        print()

    # Exit the list
    elif choice == '5':
        print("\n---Your Final To-Do List---")

        if len(works) == 0:
            print("No work in your To-Do List!")
        else:
            for i, work in enumerate(works, start=1):
                print(f"{i}. {work}")
        print("Thank you for adding your work in To-Do List!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please try again.")
        print()
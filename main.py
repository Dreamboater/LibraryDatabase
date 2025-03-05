print("Welcome to the library database software program.")

file_list = []

file = open('database.txt', 'r')
for line in file:
    file_list.append(line)
file.close()

while True:
    response = input("What would you like to do?\n Add \n Remove \n Display all \n Save \n Exit \n")

    if response == "list":
        print(file_list)

    if response == "Display all":
        print("\n")
        for line in file_list:
            print(line, end='')
        print("\n")

    if response == "Add":
        file_list.append(input("Please enter the name of the book:")+"\n")

    if response == "Remove":
        file_list.remove(input("Please enter the name of the book:")+"\n")

    if response == "Save":
        file = open('database.txt', 'w')
        for item in file_list:
            file.write(item)

    if response == "Exit":
        break







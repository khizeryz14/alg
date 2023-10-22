myList = ["Arqam", "Abdur Rahman", "Afridi", "Bilawal"]

toSearch = input("Enter name to search: ")
pos = 0
for name in myList:
    if (toSearch == name):
        print("Found at",pos, "position")
        break
    pos += 1
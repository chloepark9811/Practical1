out_file = open("name.txt", "w")
name = input("what is your name?")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("your name is", name)
in_file.close()
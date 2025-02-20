arquivo = open("file.txt", "r")
print(arquivo.readline())


with open("file.txt", "r") as arquivo:
    print(arquivo.readline())

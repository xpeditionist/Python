f=open("file1.txt",'r')
number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in f:
    line = line.strip("\n")
    words = line.split()
    number_of_lines += 1
    number_of_words += len(words)
    number_of_characters += len(line)
f.close()
print(("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters))    
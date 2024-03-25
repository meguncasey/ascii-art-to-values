readFile = open ("input.txt", "r")
writeFile = open ("ascii_vals.txt", "w")
EOF = False

while not EOF:
    line = readFile.readline()

    if line == "":  EOF = True
    else:
        line = line.replace(",", "\n")
#        print(line)

        line = line.replace("35", "#")
        print(line)

        for char in list(line):
            ascii = str(ord(char)) + "#"
            writeFile.write (ascii)



    writeFile.write("\n")

               

readFile = open ("input.txt", "r")
writeFile = open ("ascii_vals.txt", "w")
EOF = False

while not EOF:
    line = readFile.readline()

    if line == "":  EOF = True
    else:
        line = line.replace("#", " ")
        print(line)
 
    for number in list(line):
            ascii = str(chr(number)) + ","
            writeFile.write (ascii)
          

    writeFile.write("\n")
 

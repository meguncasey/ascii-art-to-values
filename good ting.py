
readFile = open ("input.txt", "r")
writeFile = open ("ascii_vals.txt", "w")
EOF = False

while not EOF:
    line = readFile.readline()
   

    if line == "":  EOF = True
    else:
        line = line.replace("#", " ")
        line = line.replace(",", "")
        line = line.replace("35", "#")
        line = line.replace("46", ".")
        line = line.replace("56", "8")
        line = line.replace("111", "o")
        line = line.replace("100", "d")
        line = line.replace("34", '"')
        line = line.replace("96", "`")
        line = line.replace("44", ",")
        line = line.replace("98", "b")
        line = line.replace("58", ":")
        line = line.replace("10", " ")
        line = line.replace("89", "Y")
        line = line.replace("39", "'")
        line = line.replace("45", "-")
        line = line.replace("80", "P")
        line = line.replace("79", "O")
        line = line.replace("59", ";")
        line = line.replace("41", ")")
        line = line.replace("4", "\u0004")
        line = line.replace("114", "r")
        line = line.replace("75", "K")
        line = line.replace("11", "\t")
        line = line.replace("5", "\u0005")
        line = line.replace("1", "\u0001")
        line = line.replace("7", "\a")
        print (line)
    for char in list(line):
            ascii = str(ord(char)) + ","
            writeFile.write (line)

       
 


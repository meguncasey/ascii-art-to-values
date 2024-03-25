
readFile = open ("input.txt", "r")
writeFile = open ("ascii_vals.txt", "w")
EOF = False

while not EOF:
    line = readFile.readline()

    if line == "":  EOF = True
    else:
        line = line.replace("#", " ")
        line = line.replace(",", "")
        line = line.replace("35", "\u0035")
        line = line.replace("46", "\u0046")
        line = line.replace("56", "\u0056")
        line = line.replace("111", "\u0111")
        line = line.replace("100", "\u0100")
        line = line.replace("34", '\u0034')
        line = line.replace("96", "\u0096")
        line = line.replace("44", "\u0044")
        line = line.replace("98", "\u0098")
        line = line.replace("58", "\u0058")
        line = line.replace("10", "\u0010")
        line = line.replace("89", "\u0089")
        line = line.replace("39", "\u0039")
        line = line.replace("45", "\u0045")
        line = line.replace("80", "\u0080")
        line = line.replace("79", "\u0079")
        line = line.replace("59", "\u0059")
        line = line.replace("41", "\u0041")
        line = line.replace("4", "\u0004")
        line = line.replace("114", "\u0114")
        line = line.replace("75", "\u0075")
        line = line.replace("11", "\u0011")
        line = line.replace("5", "\u0005")
        line = line.replace("1", "\u0001")
        line = line.replace("7", "\u0007")
        
        
        



        print(line)

        for char in list(line):
            ascii = str(ord(char)) + ","
            writeFile.write (ascii)


    writeFile.write("\n")
    

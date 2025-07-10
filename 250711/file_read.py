def readFile(path):
    lines = []
    with open(path, "r", encoding="UTF-8") as f:
        for line in f:
            lines.append(line)
    
    return lines


if __name__ == "__main__":
    with open("D:/Temp/Pushkin.txt", "r") as f:
        poem = f.read()
        print(poem)
        print (20 * "-")

        f.seek(0)
        lineNumber = 0
        while True:
            lineNumber += 1
            line = f.readline()
            if line == '':
                break
            print("{} : {}".format(lineNumber, line), end='')

        print (20 * "-")
        f.seek(0)
        for line in f:
            print(line, end='')

    print (20 * "-")
    lines = readFile("D:/Temp/Pushkin.txt")
    for line in lines:
        print(line, end='')


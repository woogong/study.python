from file_read import readFile

path = "D:/Temp/서시.txt"

poemLine = [
    '서시',
    '윤동주',
    '',
    '죽는 날까지 하늘을 우러러',
    '한 점 부끄럼 없기를',
    '잎새에 이는 바람에도 나는 괴로워했다',
    '별을 노래하는 마음으로',
    '모든 죽어가는 것들을 사랑해야지',
    '그리고 나에게 주어진 길을 걸어가야겠다',
    '오늘 밤에도 별이 바람에 스치운다'
]

with open(path, "w", encoding="UTF-8") as f:
    for line in poemLine:
        f.write(line + "\n")


lines = readFile(path)
lineNumber = 0
for line in lines:
    lineNumber += 1
    print("{:2} : {}".format(lineNumber, line), end='')


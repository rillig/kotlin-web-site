import re

fileName = "breaking-changes.md"
file = open(fileName, "r")
text = file.read()
file.close()

position = []
def generateNumber(original):
    global position
    length = len(re.split(r"\.", original))
    if length == len(position):
        position[len(position) - 1] += 1
    elif length > len(position):
        position += [1]
    else:
        position = position[:-1]
        position[len(position) - 1] += 1
    return "`" + ".".join(str(x) for x in position) + "`"

output = ""
cursor = 0
for m in re.finditer(r"`(\d+(?:\.\d+)*)`", text):
    output += text[cursor:m.start()]
    output += generateNumber(m.group(1))
    cursor = m.end()
output += text[cursor:len(text)]

file = open(fileName, "w")
file.write(output)
file.close()

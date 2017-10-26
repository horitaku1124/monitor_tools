line = 'ABCD EFG "abc" "edf ghi"'

cols = []
buf = ""
inDoubleQuote = False
for c in line:
    if inDoubleQuote:
        if c == "\"":
            inDoubleQuote = False
            cols.append(buf)
            buf = ""
        else:
            buf += c
        continue

    if c == " ":
        if buf != "":
            cols.append(buf)
            buf = ""
    else:
        if c == "\"":
            inDoubleQuote = True
        else:
            buf += c

if buf != "":
    cols.append(buf)


print (cols)
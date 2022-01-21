numbers_buffer = []
tokenized = []
line = '23 + 3 * (10 + 7 - 1)'
for s in line:

    if s.isdigit():
        numbers_buffer.append(s)

    elif s == "+" or s == "-" or s == "*" or s =="/" or s == "(" or s ==')' or s == "":
        if len(numbers_buffer) != 0:
            token = ""
            for i in numbers_buffer:
                token += i
            numbers_buffer.clear()
            tokenized.append(token)
        if s != '':
            tokenized.append(s)

print(tokenized)

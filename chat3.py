#熟悉清單分割法、字串可以當作清單操作
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(name)
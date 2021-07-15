#讀取檔案、寫入檔案、會用到continue、None適合用來當預設值

def read_file(filename): #讀取檔案
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip()) #把換行符號\n去掉
    return lines
def convert(lines): #要把檔案轉換為對話紀錄的形式
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen' #這邊的設計很巧妙、不同值存在同一變數
            continue #這邊的人名要continue，不用放進new字串
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + '：' + line)
    return new
def write_file(filename, lines):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main()
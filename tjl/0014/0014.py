import json, xlwt


def read_file():
    f = open('student', mode='r', encoding='utf-8')
    return f.read()
if __name__ == '__main__':
    f = read_file()
    s = json.loads(f)
    book = xlwt.Workbook()
    sheet = book.add_sheet(sheetname='test')
    for i in s:
        sheet.write(int(i),0,i)
        k=0
        for j in s[i]:
            k+=1
            sheet.write(int(i),k,j)
    book.save('test.xlsx')

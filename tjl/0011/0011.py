
'''
参考了别人的答案后，突然一下明白了，让句子去匹配词，不如让词去匹配句子
虽然我这个功能能实现，但逻辑还是比较繁琐，或许在其他地方能有用处，但总的来说还是上面的思想更好。
所以，学会简化问题是非常有帮助的

'''

def read_file():
    f = open('filtered_words.txt', mode='r')
    list_words = f.readlines()
    for i in range(len(list_words)):
        if (list_words[i][-1] == '\n'):
            list_words[i] = list_words[i][:-1]
    print(list_words)
    return list_words


def is_char_in_list(char, list_words):
    tmpdict = {}
    for i in list_words:
        k = i.find(char)
        if (k >= 0):
            tmpdict[i] = k
    return tmpdict


# 调用这个方法之前，已经能保证char是出于list中
def is_char2word_in_dict(char, tmpdict, input_str, char_index):  # char_index代表char在input str中的索引
    for i in tmpdict.keys():
        char2word = ''
        if (len(i) == 1):
            return i
        k = tmpdict[i]
        if (k > 0):
            if (char_index - k > 0):
                if (len(i) - k - 1 > 0 and len(i) - k - 1 < len(input_str) and char_index + 1 <= len(i) - k - 1):
                    char2word = input_str[char_index - k:char_index] + char + input_str[char_index + 1:len(i) - k]
                else:
                    char2word = input_str[char_index - k:char_index] + char
        else:
            if (len(i) - k - 1 > 0 and len(i) - k - 1 < len(input_str) and char_index + 1 <= len(i) - k - 1):
                char2word = char + input_str[char_index + 1:len(i) - k]
            else:
                char2word = char
        if (char2word == i):
            return i
def make_star(num):
    s=''
    for i in range(num):
        s+='*'
    return s

if __name__ == '__main__':
    list_words = read_file()
    while (True):
        s = input('输入一句话')
        if (len(s) == 0):
            break
        i_index = -1
        flag = True
        for i in s:
            i_index += 1
            tmpdict = is_char_in_list(i, list_words)
            res = is_char2word_in_dict(char=i, tmpdict=tmpdict, input_str=s, char_index=i_index)
            if (res):
                print('包含于敏感词：', res)
                print(s.replace(res,make_star(len(res))))
                flag = False
                break
        if (flag):
            print('不包含于敏感词.')

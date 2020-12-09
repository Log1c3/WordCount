import re
import sys


def CountChar(file):
    letters = 0
    space = 0
    digit = 0
    others = 0
    file = sys.argv[1]
    fp = open(file, 'r')
    string = fp.read()
    print("内容：" + string)
    fp.close()
    for c in string:
        if c.isalpha():
            letters += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        else:
            others += 1
    print("文件中有%d个英文字母，%d个数字，%d个空格，%d个其他字符" % (letters, digit, space, others))


def CountWord(file):
    file = sys.argv[1]
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    fp = open(file, 'r')
    string = fp.read()
    print("内容：\n" + string)
    fp.close()
    ls = re.split(pattern, string)
    print("单词数=%d" % --len(ls))


print("脚本名：", sys.argv[0])
for i in range(1, len(sys.argv)):
    print("参数：", i, sys.argv[i])
if sys.argv[2] == "-c" or sys.argv[2] == "-C":
    CountChar(sys.argv[1])
elif sys.argv[2] == "-w" or sys.argv[2] == "-W":
    CountWord(sys.argv[1])
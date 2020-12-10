import re
import sys


def CountChar(file):
    letters = 0
    space = 0
    digit = 0
    others = 0
    fp = open(file, 'r')
    string = fp.read()
    print("内容：" + string)
    fp.close()
    for c in string:
        if c.isalpha():#判断字母
            letters += 1
        elif c.isdigit():#判断数字
            digit += 1
        elif c.isspace():#判断空格
            space += 1
        else:#其他
            others += 1
    print("%d个英文字母\n%d个数字\n%d个空格\n%d个其他字符" % (letters, digit, space, others))


def CountWord(file):
    patter = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    #所有标点符我把它看作隔板
    fp = open(file, 'r')
    string = fp.read()
    print("内容：" + string)
    #输出读取的文本
    fp.close()
    ls = re.split(patter, string)
    #隔板将string分隔并存储在ls中
    length = len(ls)
    if string[len(string)-1] in patter:
    #如果在string的结尾或开头能匹配pattern
    # 则会在返回列表的最后一个元素或第一个元素是空字符串，所以要-1
        length -= 1
        print("单词数=", length)
    else:
        print("单词数=", length)


print("脚本名：", sys.argv[0])
for i in range(1, len(sys.argv)):
    if(i == 1):
        print("指令：\t", sys.argv[i])
    if(i == 2):
        print("文件名：", sys.argv[i])
if sys.argv[1] == "-c" or sys.argv[1] == "-C":
    CountChar(sys.argv[2])
elif sys.argv[1] == "-w" or sys.argv[1] == "-W":
    CountWord(sys.argv[2])
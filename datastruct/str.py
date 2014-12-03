# coding:utf-8
def printUnicode(s):
    if isinstance(s, unicode): 
        #s=u"中文" 
        print u"unicode字符：",s.encode('gb2312') 
    else: 
        #s="中文" 
        print u"普通字符：",s.decode('utf-8').encode('gb2312')
if __name__ == '__main__':
    #1、查找元素find index，计算出现次数count，替换replace
    #   find和index区别,前者找不到返回-1，后者找不到报错
    print "aaab".find("9") # 输出：-1
    #   print "aaab".index("9") # 抛出异常
    #   加r从右开始找
    print "aaab".rfind("a") # 输出：2
    print "aaab".rindex("a") # 输出：2
    print "aaab".count("a") # 计算出现次数， 输出：3
    print "aaab".replace("a","c",2) # 将a替换成c，替换2次，输出：ccab

    #2、去除元素 strip
    #   默认去除 \t\n，l从消除左边，r是消除右边
    s = "  a  "
    print s.strip() # 输出："a"
    print s.lstrip() # 输出："  a"
    print s.rstrip() # 输出："  a"

    #   去除字符串中含有序列的每个元素
    s = "abcdeffedbca"
    print s.strip("ab") # 输出：cdeffedbc

    #3、反转，同样也可用于列表
    s = "abcdefg"
    print s[::-1] # 输出：gfedcba

    #4、判断、测试字符串
    #4.1 是空格
    # 输出：True
    print "“ ”是否为空格:", " ".isspace(),"\n“aaa”是否为空格:","aaa".isspace()
    # 输出：False
    print "注意，空字符不为空格，“”是否为空格:", "".isspace()
    #4.2 判断开始结束
    print "abcd以ab开头吗？","abcd".startswith("ab"),"\nabcd以b开头吗？","abcd".startswith("b")
    # 输出：False
    print "abcd以cd结尾吗？","abcd".endswith("cd"),"\nabcd以c结尾吗？","abcd".endswith("c")
    # 输出：True
    print "abcd从第2个字符开始是以b开头吗？","abcd".startswith("b",1)
    # 输出：True
    print "abcd从第2个字符到第3个字符的字符串是以c结尾吗？","abcd".endswith("c",1,3)
    #4.3 是否全是字母和数字，并至少有一个字符 
    # 输出：True
    print "abcdef123是否全为数字和字母：","abcdef123".isalnum()
    # 输出：False
    print "abcdef,,123是否全为数字和字母：","abcdef,,123".isalnum()
    # 输出：False
    print "“”是否全为数字和字母,并且至少有一个字母：","".isalnum()
    #4.4 是否全为字母
    print "aaa".isalpha() # 输出：True
    print "aa1".isalpha() # 输出：False
    print "aa,".isalpha() # 输出：False
    #4.5 是否全为数字
    print "aaa".isdigit() # 输出：False
    print "221".isdigit() # 输出：True
    print "22,".isdigit() # 输出：False
    #4.6 大小写判断
    print "aaa".islower() # 输出：True
    print "AAA".islower() # 输出：False
    print "aaa".isupper() # 输出：False
    print "ABC".isupper() # 输出：True
    #4.7 是否首字母大写，其他小写
    print "ABC".istitle() # 输出：False
    print "Abc".istitle() # 输出：True
    print "123".istitle() # 输出：False

    #5、字符转换
    #大小写转换
    s = "ABC"
    print s.lower() #小写  输出：abc
    print s #原字符不变 输出：ABC
    print s.upper() #大写  输出：ABC
    print s.swapcase() #大小写互换  输出：abc
    print s.capitalize() #首字母大写  输出：Abc

    #6、比较字符串,也可以比较数字
    print cmp("aaa","bbb") # 输出：-1
    print cmp("ccc","bbb") # 输出：1
    print cmp(1,2) # 输出：-1

    #7、字符串切片
    s = "1234567890"
    print s[1] #截取第二个字符 输出：2
    print s[-1] #截取最后一个字符 输出：0
    print s[-3] #截取倒数第三个字符 输出：8
    print s[::] #可用于克隆字符串 输出：1234567890
    print s[2:] #从第三个字符开始截取 输出：34567890
    print s[:9] #从头截取到第9个字符 输出：123456789
    print s[::2] #从头截取，每取一次间隔一个字符 输出：13579
    print s[10::-1] #反向截取，输出：0987654321
    print s[-1:-11:-1] #与s[10::-1]结果相同 输出：0987654321

    #8、扫描字符串 输出1 2 3 4 5 6 7 8 9 0
    for char in s:print char,
    print
    #9、分割字符串
    print "12,34,5,678,9,0".split(",") # 输出['12', '34', '5', '678', '9', '0']
    print "   12    34  5  ".split()#默认按空格分割 输出['12', '34', '5']
    print "   12    34  5  ".split(" ")#但是不同的是，默认的方法会先strip 输出['', '', '', '12', '', '', '', '34', '', '5', '', '']

    #10、连接集合中的字符串
    print "".join(["a","b","c","d"]) # 输出abcd
    print ",".join(["a","b","c","d"]) # 输出a,b,c,d

    #11、filter 结合lambda 输出：AmanaplanacanalPanama
    # lambda即为小函数
    # filter(function,sequence) sequence可为字符串、列表、tupple ，范围经过function过滤后返回true的相应类型结果
    print filter((lambda x:x.isalnum()),"A man, a plan, a canal: Panama")

    #12、map操作
    print map((lambda x,y:x+y),[1,2,3,4],[10,20,30,40])

    #13、reduce操作 reduce(function,sequence,startNum)startNum默认为0
    print  reduce((lambda x,y:x+y),[2,3,4,5,6,7,8,9,10],1)

    #14、补齐
    print "\""+"abcde".ljust(10)+"\"" #右边补 输出: "abcde     "
    print "\""+"abcde".rjust(10)+"\"" # 输出: "     abcde"
    print "\""+"abcde".center(10)+"\"" #中间对齐  输出:"  abcde   "
    print "\""+"abcde".center(10,"-")+"\"" #用-补齐  输出:"--abcde---"

    #15、编码解码
    # s="中文" 
    # printUnicode(s) # 输出 ：普通字符： 中文
    # s=u"中文2" # 带u定义为unicode编码
    # printUnicode(s) # 输出 ：unicode字符： 中文2

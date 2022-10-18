import re

html='''
            <!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8" />
                <title></title>
                <style type="text/css">
                  #navi{
                      width:1008px;/*宽度*
                      height:60px;/*高度*/
                      border:1px solid black;/*边框实线颜色*/
                  }
                  .navListt{
                      width: 250px;
                      height: 60px;
                      border: 1px solid black
                      float: left;/*左浮动*/
                      text-align: center;/*水平居中*
                      line- height:60px;/*垂直居中线高*/
                  }
                  .navList:hover{
                      background- color:#7FF;/*背景颜色*/
                      cursor: pointer;/*鼠标变小手*/
                      color: white;/*颜色*/
                  }
                </style>
              </head>
              <body>
                <div id="nav">
                  <div
                    class="navList"
                    href="https://baike.baidu.com/item/%E6%98%A5%E8%8A%82/136876"
                  >
                    春节
                  </div>
                  <div
                    class="navList"
                    href="https://baike.baidu.com/item/%E6%B8%85%E6%98%8E%E8%8A%82/137575"
                  >
                    清明节
                  </div>
                  <div
                    class="navList"
                    href="https://baike.baidu.com/item/%E7%AB%AF%E5%8D%88%E8%8A%82/1054"
                  >
                    端午节
                  </div>
                  <div
                    class="navList"
                    href="https://baike.baidu.com/item/%E4%B8%AD%E7%A7%8B%E8%8A%82/128234"
                  >
                    中秋节
                  </div>
                </div>
              </body>
            </html>
'''
text_=re.findall("[a-zA-Z]+://[^\s]*[.com|.cn]",html)
print(text_)
'''''
re解析
re.match()
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
函数语法：
re.match(pattern, string, flags=0)
re.search()
re.search 扫描整个字符串并返回第一个成功的匹配。匹配成功re.search方法返回一个匹配的对象，否则返回None。
函数语法：
re.search(pattern, string, flags=0)
compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，re函数使用。
提前编译可减少多次正则匹配的运行时间
语法格式为：
re.compile(pattern[, flags])
re.findall()
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。
语法格式为：
re.findall(string, pos, endpos)
re.finditer
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
语法格式为：
re.finditer(pattern, string, flags=0)
re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，
它的使用形式如下：
re.split(pattern, string[, maxsplit=0, flags=0])
groups()
我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
匹配对象方法	描述
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
re.sub
Python 的re模块提供了re.sub用于替换字符串中的匹配项。
语法：
re.sub(pattern, repl, string, count=0, flags=0)
repl 参数可以是一个函数
以下实例中将字符串中的匹配的数字乘于 2：
###########re模块符号大全###########################################################################
正则表达式模式
模式字符串使用特殊的语法来表示一个正则表达式：

字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。

多数字母和数字前加一个反斜杠时会拥有不同的含义。

标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。

反斜杠本身需要使用反斜杠转义。

由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 \\t )匹配相应的特殊字符。

下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。

模式	描述
^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a|b	匹配a或b
(re)	匹配括号内的表达式，也表示一个组
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
(?> re)	匹配的独立模式，省去回溯。
\w	匹配数字字母下划线
\W	匹配非数字字母下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f]。
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9]。
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等。	匹配一个换行符。匹配一个制表符, 等
\1...\9	匹配第n个分组的内容。
\10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

注意：表中re指的是表达式而不是字面的re这两个字母

正则表达式修饰符 - 可选标志
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：

修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
正则表达式对象
re.RegexObject

re.compile() 返回 RegexObject 对象。

re.MatchObject

group() 返回被 RE 匹配的字符串。

start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置
##################################################################################
正则表达式是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。

在正则表达式中，如果直接给出字符，就是精确匹配。

使用特殊符号表示字符：用\d可以匹配一个数字，\w可以匹配一个字母或数字，例如：

'00\d'可以匹配'007'，但无法匹配'00A'；

'\d\d\d'可以匹配'010'；

'\w\w\d'可以匹配'py3'。

'.'可以匹配任意字符，所以：

'py.'可以匹配'pyc'、'py3'、'py!'等等。
要匹配变长的字符，在正则表达式中，用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符。

来看一个复杂的例子：\d{3}\s+\d{3,8}。

我们来从左到右解读一下：

\d{3}表示匹配3个数字，例如'010'；

\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；

\d{3,8}表示3-8个数字，例如'1234567'。

综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。

如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，所以，上面的正则是\d{3}\-\d{3,8}。

但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。

进阶
要做更精确地匹配，可以用[]表示范围，比如：

[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。

py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了

'''''

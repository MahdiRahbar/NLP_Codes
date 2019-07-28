import re


# Suppose we get a string called my_string
table = {1776: 48,  # 0 
         1777: 49,  # 1
         1778: 50,  # 2
         1779: 51,  # 3
         1780: 52,  # 4
         1781: 53,  # 5
         1782: 54,  # 6
         1783: 55,  # 7
         1784: 56,  # 8
         1785: 57}  # 9

string = u'The String is going to be placed here.'.translate(table)
result = ''.join([i for i in s if not i.isdigit()])


# or 

string = re.sub(r'\d+', '', my_string)

import sys
args = sys.argv

#引数の挿入
input_statement = str(args[1])
input_num = int(args[2])

words = input_statement.split()
print(words[input_num])

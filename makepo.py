#coding: UTF-8
import sys

file = open(sys.argv[1], "r")
file2 = open("output.po", "w", encoding='utf-8')

content = file.readlines()
file2.write('msgid ""\n')
file2.write('msgstr ""\n')
file2.write('"Content-Type: text/plain; charset=UTF-8\\n"\n\n')

for x in content:
	file2.write('msgid "{}"\n'.format(x[:-1]))
	file2.write('msgstr ""\n')

file.close()
file2.close()
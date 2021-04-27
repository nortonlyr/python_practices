import sys
def readfile(filename): #从文件中读出文件内容
    '''''Print a file to the standard output.'''
f = file(filename)
while True:
    line = f.readline()
if len(line) == 0:
    break
print line, # notice comma 分别输出每行内容
f.close()
# Script starts from here
if len(sys.argv) < 2:
    print 'No action specified.'
sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
# fetch sys.argv[1] but without the first two characters
if option == 'version': #当命令行参数为-- version，显示版本号
    print 'Version 1.2'
elif option == 'help': #当命令行参数为--help时，显示相关帮助内容
print '''''/ 
This program prints files to the standard output. 
Any number of files can be specified. 
Options include: 
--version : Prints the version number 
--help : Display this help'''
else:
print 'Unknown option.'
sys.exit()
else:
for filename in sys.argv[1:]: #当参数为文件名时，传入readfile，读出其内容
    readfile(filename)
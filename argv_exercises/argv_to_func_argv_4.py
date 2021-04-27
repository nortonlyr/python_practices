from sys import argv
f = open(argv[1], 'r')
print(f.read())
f.close()
import sys
a = sys.argv[0]
b = sys.argv[1]
c = sys.argv[2]
d = sys.argv[3]

# print('filename: ',a)
# print('param1: ', b)
# print('param2: ', c)
# print('param3: ', d)
print('sum of b,c,d:', int(b)+int(c)+int(d))

b = int(b)
c = int(c)
d = int(d)

def my_test_func(b, c, d):
    return (f'my_test_func result is: {b*c + c*d + d*b}')

print(my_test_func(b, c, d))

# if __name__ == '__main__':
#     my_test_func(b, c, d)
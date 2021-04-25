import sys
a = sys.argv[0]
b = sys.argv[1]
c = sys.argv[2]
d = sys.argv[3]


print('combine of b,c,d:', b + c + d)


def my_test_func(b, c, d):
    return (f'my_test_func result is: {b +" "+ c + " "+ d}')

print(my_test_func(b, c, d))

# if __name__ == '__main__':
#     my_test_func(b, c, d)
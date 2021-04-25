import sys


def func1():
    raise NameError("--func1 exception--")


def main():
    try:
        func1()
    except Exception as e:
        exc_type, exc_value, exc_trackback_obj = sys.exc_info()
        print (f'exc_type: {exc_type}')
        print (f'exc_value: {exc_value}')
        print (f'exc_trackback_obj: {exc_trackback_obj}')

if __name__ == '__main__':
    main()
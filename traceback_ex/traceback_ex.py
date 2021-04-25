def func1():
    raise Exception("--func1 exception--")

def main():
    try:
        func1()
    except Exception as e:
        print (e)


if __name__ == '__main__':
    main()

import mymodule

def print_hello(name='Masha'):
    print(mymodule.hello(name))


def main():
    name = 'Vasya'
    print_hello(name)


if __name__ == '__main__':
    main()

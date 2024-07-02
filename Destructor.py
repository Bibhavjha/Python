class employee:
    def __init__(self):
        print('constructor called')
    def __del__(self):
        print('destructor called')
e=employee()
del e
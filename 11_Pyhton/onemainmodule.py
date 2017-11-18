def func():
    print("func() is onemainmodule.py")

print ("TOP LEVEL onemainmodule.py")

if __name__ == '__main__':
    print("onemainmodule.py is being run directly")
else:
    print("onemainmodule.py has been imported")
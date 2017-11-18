import onemainmodule as one
print("TOP LEVEL MAIN NAME.PY")
one.func()

if __name__ == '__main__':
    print("MAIN NAME being run directly")
else:
    print("MAIN NAME is being imported")
import sys
if __name__ == '__main__':
    print "_".join(sys.argv[1:]).lower().replace(".", "")+".py"

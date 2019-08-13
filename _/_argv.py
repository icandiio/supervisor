import sys

if __name__ == "__main__":
    print(sys.argv)
    # sys.argv 获取命令行输入参数
    # python _argv.py a b c => ['_argv.py','a','b','c']
    # python -m _argv a c c => ['/lns/shareds/pys/github/_/_argv.py','a','b','c']

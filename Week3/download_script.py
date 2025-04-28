import webget
import sys


if __name__ == '__main__':
    arguments = sys.argv[1:]
    input_lines = sys.stdin.read().split('\n')
    files = arguments + input_lines

    for file in files:
        webget.download(file)
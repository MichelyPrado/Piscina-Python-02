import os
import sys

def verify_input():
    # se são 2 argumentos
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        sys.exit()
    # se a extensão é .template
    if sys.argv[1].endswith(".template") == False:
            print("Wrong file extension")
            sys.exit()
    # se o arquivo não está na pasta certa
    if not os.path.isfile("./" + sys.argv[1]):
            print("File not found!")
            sys.exit()

def write_html(content):
    name_html = sys.argv[1].replace(".template", ".html")
    file = open(name_html, 'w')
    file.write(content)

def read_template():
    dictionary = globals()
    
    name_arg = sys.argv[1]
    content = open(name_arg, 'r').read()
    for key, value in dictionary.items():
        sub = "".join("{" + key + "}")
        content = content.replace(sub, str(value))
    return(content)

if __name__ == '__main__':

    verify_input()
    exec(open('settings.py', 'r').read())
    content = read_template()
    write_html(content)

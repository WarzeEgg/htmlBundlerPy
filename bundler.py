import os
import time
import re
from jsmin import jsmin

#file_name = input("Enter .html file")
file_name = 'index'

with open(file_name + '.html', 'r') as f:
    new_file = f.read()

    # Find scripts
    regex = re.compile(r'<script.*? src=".*?"><\/script>')
    for match in regex.finditer(new_file):
        with open(re.findall(r'src="([^"]*)"', match.group())[0]) as js:
            code = jsmin(js.read())
            script_tag = '<script>' + code + '</script>'
            new_file = new_file.replace(match.group(), script_tag)

    regex = re.compile(r'<link rel="stylesheet" href=".*?">')
    for match in regex.finditer(new_file):
        with open(re.findall(r'href="([^"]*)"', match.group())[0]) as css:
            code = css.read().replace(' ','').replace('\n','')
            script_tag = '<style>' + code + '</style>'
            new_file = new_file.replace(match.group(), script_tag)

    print(new_file)
    with open(file_name + 'bundle.html', 'w') as out:
        out.write(new_file)
    time.sleep(5)
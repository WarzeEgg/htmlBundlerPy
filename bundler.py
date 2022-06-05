import re
import rjsmin

file_name = 'index-source'

with open(file_name + '.html', 'r') as f:
    # Read the original file
    new_file = f.read()
    new_file = new_file.replace('\t','').replace('\n','')

    # Find scripts
    regex = re.compile(r'<script.*? src=".*?"><\/script>')
    for match in regex.finditer(new_file):
        jsfile = re.findall(r'src="([^"]*)"', match.group())[0]
        if 'min' not in jsfile:
            with open(jsfile) as js:
                code = rjsmin.jsmin(js.read())
                script_tag = '<script>' + code + '</script>'
                new_file = new_file.replace(match.group(), script_tag)

    # Find stylesheets
    regex = re.compile(r'<link rel="stylesheet" href=".*?">')
    for match in regex.finditer(new_file):
        with open(re.findall(r'href="([^"]*)"', match.group())[0]) as css:
            code = css.read().replace('\n','').replace('\t','')
            script_tag = '<style>' + code + '</style>'
            new_file = new_file.replace(match.group(), script_tag)

    # Write the new file
    with open('index.html', 'w') as out:
        out.write(new_file)
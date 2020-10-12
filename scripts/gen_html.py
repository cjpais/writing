import sys
import os
import re
import subprocess
from jinja2 import Template, Environment, FileSystemLoader, select_autoescape

PANDOC_CMD = "pandoc -f commonmark_x -t html {}"
HTML_RE = re.compile(r'<[^>]+>')

jinja_env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape(['html', 'xml'])
)

# from https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def remove_html(string):
    return HTML_RE.sub('', string)

# get the file from input
in_fn = sys.argv[1]
out_fn = os.path.splitext(in_fn)[0] + ".html"

# get the title from the file
with open(in_fn, 'r') as in_f:
    for line in in_f:
        if "#" in line:
            title = remove_html(line.split("#")[-1].strip())
            break

# generate raw HTML from markdown
cmd = PANDOC_CMD.format(in_fn)
print(cmd)
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8")

# insert raw HTML into a template
template = jinja_env.get_template("base.template")
output_html = template.render({"content": result, "title": title})

# write out final HTML
with open(out_fn, 'wb') as out_f:
    out_f.write(output_html.encode("utf-8"))
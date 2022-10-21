from jinja2 import Template

name = 'Fedor'
tm = Template("Привет  {{ name }}")
msg = tm.render(name=name)

print(msg)
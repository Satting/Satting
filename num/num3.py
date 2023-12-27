from lxml import html

etree = html.etree

f = open('login.html', 'r', encoding='utf-8')
log = f.read()
et = etree.HTML(log)

res = et.xpath("/html/body/h1/text()")
print(res)
import re

from bs4 import BeautifulSoup
html_doc=""""
<html><head></head>
<body>
<a href="http://example.com/title" class="sister" id="link1">Title1</a>
<a href="http://example.com/name" class="sister" id="link2">Title2</a>
<a href="http://example.com/阿哥" class="sister" id="link3">Title3</a>
<a href="http://example.com/fdsf" class="sister" id="link4">Title4</a>
<p class="pp">法国大使馆记得发广告豆腐干大锅饭的</p>
<p class="pp2">dsjfdsjfdjsfljsdf士大夫士大夫的</p>
</body>
</html>

"""

soup=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print ('\n获取所有链接')
links=soup.find_all('a')
for link in links:
    print (link.name,link['href'],link['id'],link.get_text())
print ('\n获取单个链接')
link_node=soup.find('a',href='http://example.com/阿哥')
print (link_node.name,link_node['href'],link_node.get_text)
print ('\n正则匹配')
link_node2=soup.find('a',href=re.compile(r'ame'))
print (link_node2.name,link_node2['href'],link_node2.get_text)
print ('\nclass属性')
p_node=soup.find('p',class_='pp')
print (p_node.name,p_node.get_text)




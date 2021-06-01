from bs4 import BeautifulSoup

html = '<td id="td1" class="title">' \
       '  <div class="tit3">' \
       '    <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>' \
       '  </div>' \
       '</td>'
bs = BeautifulSoup(html, 'html.parser')
# print(bs, type(bs))
# tag = bs.a
# print(tag, type(tag))

# tag = bs.td
# print(tag['class'])  
# print(tag['id'])     
# print(tag.attrs)  

# tag = bs.find('div', attrs={'class': 'tit3'})
# print(tag)     
# tag = bs.find('div')
# print(tag)      
# tag = bs.find('td', attrs={'class': 'not_exist'})
# print(tag)    
# tag = bs.find(attrs={'title': '범죄도시'})
# print(tag)

# tag = bs.select("td div a")[0]
# print(tag)
# 
# text = tag.contents[0]
# print(text)

tag = bs.select("td")[0]
#print(tag)      # <td class="title" id="td1"> <div class="tit3"> <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a> </div></td>

# div요소를 제거
div_elements = tag.find_all("div")
for div in div_elements:
    div.extract()
    
print(tag)


# get all following Instagram accounts of current profile
# <a class="FPmhX notranslate  _0imsa " title="jenniferbllr" href="/jenniferbllr/" tabindex="0">jenniferbllr</a>

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
u_f = soup.find_all('a', {'class' : 'FPmhX'})

l_following=[]
i=0
while (i<len(u_f)):
  l_following.append(u_f[i]['href'])
  i += 1

with open('Instagram/following_jchastain.json', 'w') as outfile:
  json.dump(l_following, outfile)

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
l_ig = []
i=0
while (i<len(u_f)):
  driver.get('http://www.instagram.com'+l_following[i])
  soup = BeautifulSoup(driver.page_source, "html.parser")
  # create json
  j = {}
  j['followers'] = soup.find_all('span', {'class' : 'g47SY'})[1]['title']
  j['ig']=driver.current_url
  i += 1
  l_ig.append(j)
  print(l_ig + i)
  input()
  
with open('Instagram/ig_followers_jchastain.json', 'w') as outfile:
    json.dump(l_ig, outfile)

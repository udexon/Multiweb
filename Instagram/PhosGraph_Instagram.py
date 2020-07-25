# parse Instagram page html
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
# create json
j = {}
j['followers'] = soup.find_all('span', {'class' : 'g47SY'})[1]['title']
j['ig']=driver.current_url

# open PhosGraph POST page in new tab
windows_before = driver.current_window_handle
tab_ig = windows_before
driver.execute_script("window.open('http://phos.epizy.com/phos/post_rc.php?r=&c=')")
windows_after = driver.window_handles
tab_phos = [x for x in windows_after if x != windows_before][0]
driver.switch_to.window(tab_phos)

# enter dictionary j as json
import json
u_j=driver.find_element_by_xpath('//*[@id="json"]')
u_j.send_keys(json.dumps(j))
u_f=driver.find_element_by_name("form_json")
u_f.submit()

# HTTP GET extract number of followers from PhosGraph
import base64
import urllib
s1='https://www.instagram.com/jessicachastain/'
driver.get("http://phos.epizy.com/phos/get.php?r=data/log_fi:_c_get:_d64:_g:_av:_cx:_1_-_i:_pjs:_0_i:_jd:_followers_i:_ON_ECHO_bv:_ec:&c="+urllib.parse.quote(base64.b64encode(s1.encode())))
t_followers=driver.find_element_by_tag_name('body').get_attribute('innerHTML')

# 2020 07 21: after accept alert, set json values
driver=browser
j_u=driver.current_url
ta=driver.find_element_by_xpath('/html/body/div[31]/form/textarea')
j={}
j['url']=j_u
j['author']='alex'
j['comment']=ta.get_attribute('value')

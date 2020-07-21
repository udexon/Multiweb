# get comment from PhosGraph, append to post
driver.get("http://phos.epizy.com/phos/get.php?r=data/log_fi:_c_get:_d64:_g:_av:_cx:_1_-_i:_pjs:_0_i:_jd:_comment_i:_ON_ECHO_bv:_ec:&c="+urllib.parse.quote(base64.b64encode(s1.encode())))
t_cmt=driver.find_element_by_tag_name('body').get_attribute('innerHTML')
driver.switch_to.window(tab_comment)
driver.execute_script('A=document.getElementsByClassName("_3sf33-9rVAO_v4y0pIW_CH"); B=A[0].cloneNode(true); A[0].parentNode.insertBefore(B, A[0]); A[0].id="ph001"; C=document.getElementsByClassName("_1qeIAgB0cPwnLhDF9XSiJM"); C[0].innerText="'+ t_cmt +'";')

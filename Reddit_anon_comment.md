# Multiweb Demo: Reddit "Uncensorable" Anonymous Comments

This is a perhaps modest introduction to Multiweb, arguably the biggest breakthrough since the invention of the World Wide Web itself, built upon several incremental innovations.

Figure 1 shows a Reddit post viewed by a user without logging in. We demostrate how the anonymous user may add a new comment, as displayed in figure 2. The user keyed in the comment in a text box (textarea) with a red 'PHOS' button at the lower right corner. The comment 'July 21 1250 le quick browne foux' is inserted as the first comment after the main post.

- Figure 1
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/reddit_post_load.png" width=600>

- Figure 2
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/anon_comment_added.png" width=600>

We shall describe the detailed mechanisms of how the above was achieved, before discussing various related issues.

1. A pop-up text box (HTML textarea within a form) is added to the DOM of the HTML page, by executing the commands listed in the following file via the browser console, as shown in figure 3 and 4:

- https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/phos_comment_box.js


- Figure 3
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/popup_command_before.png" width=600>


- Figure 4
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/popup_command_after.png" width=600>


2. As shown in lines 25 to 27 in `phos_comment_box.js`, the red 'PHOS' button will trigger an `alert()` window when pressed. 

```js
S[3].className='form-container btn'
S[3].style.backgroundColor='red'
S[3].onclick=function(){alert();}
```

We use this mechanism to notify the Python Selenium function `wait_alert()` as shown in figure 5, to retrieve the text entered by the user in the pop-up box, and store it via a HTTP POST web page in a remote PhosGraph server, as shown in figure 6:

- http://phos.epizy.com/phos/post_rc.php?r=&c=

This website acts a prototype for our graph database server, hence the name PhosGraph.


- Figure 5
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/add_comment.png" width=600>

- Figure 6
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/post_phosgraph.png" width=600>

The Python Selenium code for figure 6 are given in the following files:

- https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/set_json.py
- https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/post_phosgraph.py

- Figure 7
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/get_phosgraph.png" width=600>

3. Figure 7 shows a portion of the text file used to store PhosGraph, by executing the following command as a HTTP GET request:

- http://phos.epizy.com/phos/get.php?r=data/log_fgc:_s:

The GET parameter `r=data/log_fgc:_s:` is a Phoscript command, derived from the Forth programming language, in Reverse Polish Notation. It is parsed as underscore delimited token, resulting in `data/log fgc: s:`. 

`data/log` is the log file (text file) to be opened using the command `fgc:` which is mapped to PHP `file_get_contents()`.

`s:` is a variant of Forth `.s` which displays the variables on the stack. In this case, the whole `data/log` file is stored in a string variable on the stack `$S`.

4. Finally, the commands in `insert_comment.py` were executed, as shown in figure 2, to insert the comment retrieved from PhosGraph server as the first comment of the original post.

- https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/insert_comment.py

The first line of `insert_comment.py` is a Phoscript command that essentially performs the steps explained below. As with Forth like stack machines, each step (function word) utilizes (pops) items stored on the data stack as input and pushes the result back on to the stack. 

```py
driver.get("http://phos.epizy.com/phos/get.php?
r=data/log_fi:_c_get:_d64:_g:_av:_cx:_1_-_i:_
pjs:_0_i:_jd:_comment_i:_ON_ECHO_bv:_ec:
&c="+urllib.parse.quote(base64.b64encode(s1.encode())))

data/log_fi: open data/log with file(), store in an array

c_get: obtain the value of GET variable $_GET['c'], as defined below

d64: perform base64 decode on $_GET['c']

g: run preg_grep() over array initialized by file('data/log') above

av: execute array_values() to convert the indices of preg_grep() results to 0 to N-1

cx:_1_-_i: get the last line of preg_grep() results

pjs: detect locations of multiple json(s) in the result

0_i: get the first json

jd: run json_decode()

comment_i: get 'comment' in json

ON_ECHO_bv: set ECHO to ON

ec: echo the result on stack, i.e. 'comment' in json

c="+urllib.parse.quote(base64.b64encode(s1.encode())) s1 is the link of the Reddit post, used as search key in preg_grep() above
```


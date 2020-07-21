This is a perhaps modest introduction to Multiweb, arguably the biggest breakthrough since, built upon several incremental innovations ....

Not included PhosCloud, BitTorrent type ssh tunnel and transient key cryptography + PhosGraph. Give Greeting with a Secret Phrase (GASP) article.

The http protocol itself did not mandate that a web page needs to be restricted to a single source to retrieve its contents. This practice was established ....

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

- Figure 7
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/get_phosgraph.png" width=600>

Figure 7 shows a portion of the text file used to store PhosGraph.

Compare to Twitter user retweet this Reddit post and comment &mdash; need a global universal (distributed) graph database. Nature of universal database -- does not matter who hosts it, it will be shared and become part of universal database.

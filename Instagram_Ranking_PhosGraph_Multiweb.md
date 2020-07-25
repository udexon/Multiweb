# PhosGraph Multiweb Instagram Ranking 

## Demo: Reddit "Uncensorable" Anonymous Comments

We demonstrate an almost trivial example of multiweb, where [anonymous comments can be added to Reddit posts](https://github.com/udexon/Multiweb/blob/master/Reddit_anon_comment.md) (click [here](https://github.com/udexon/Multiweb/blob/master/Reddit_anon_comment.md)), by modifying the HTML DOM locally and storing the comments on a third party graph database server. It is trivial simply because of the number of comments that can be made by one anonymous commentator. It will no longer be trivial if this mechanism can be replicated over literally billions of user devices (desktop computers and mobile devices).

The same techniques may be applied to crowd source collection of Instagram data, i.e. Instagrammers' follower count, perhaps the most sought after advertising statistics globally and locally. The difficulties in gathering such data is not unique to Instagram. Such data is either public available (e.g. Instagram profile can viewed without login) or available to individuals after login. What is lacking is a universal platform or mechanism to collect such data. Out solution is packaged as PhosGraph &mdash; a transient key (cryptography) graph database &mdash; an open graph database WITHOUT using the conventional Unix style username (hence centralized) authentication.


We will be using the same code as Figure 6 from Reddit "Uncensorable" Anonymous Comment to store the Instagram follower count via a HTTP POST web page in a remote PhosGraph server:

- http://phos.epizy.com/phos/post_rc.php?r=&c=

This website acts a prototype for our graph database server, hence the name PhosGraph.

- Figure 6 (from Reddit "Uncensorable" Anonymous Comment)
<img src="https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/post_phosgraph.png" width=600>

The Python Selenium code for figure 6 are given in the following files:

- https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/set_json.py
- https://github.com/udexon/Multiweb/blob/master/reddit_anon_comment/post_phosgraph.py

1. We adapt the code above to extract the number of followers for specific Instagram users:

- https://www.instagram.com/jessicachastain/

Interestingly, Instagram allows opening such user profile page WITHOUT user login.

The right isde of figure 1 below shows the browser console, containing the DOM element for the number of followers, highlighted in light blue. The left side of figure 1 shows the corresponding web page and number of followers, also highlighted in light blue.

- Figure 1
<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/DOM_follwer.png" width=600>


2. Figure 2: the outerHTML of the number of followers is copied.

- Figure 2
<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/copy_outerHTML.png" width=600>


3. We skip the intermedia steps and display the final step in figure 3 &mdash; obtaining the number of followers from PhosGraph server, which can be used in further operatios.

- Figure 3
<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/phosgraph_get_followers.png" width=600>


4. Figure 4 shows the continuation from step 2, where the class name in outerHTML is used in `soup.find_all()` to extract the number of followers, and store in a Python dictionary `j`.　

- Figure 4
<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/dom_json.png" width=600>

<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/tab_phos.png" width=600>

<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/post_submit.png" width=600>


<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/log_all.png" width=600>

<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/log_grep.png" width=600>

<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/log_grep_line.png" width=600>


<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/log_json_all.png" width=600>

<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/log_json_decode.png" width=600>
            

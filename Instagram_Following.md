# Extracting Number of Followers of All "Following" Accounts of an Instagram Profile

We reserve the term "User" to refer to the person logging in to Instagram. Hence the term "Profile" refers to the Instagram account that the User is currently viewing, e.g.

- https://www.instagram.com/jessicachastain/

- Figure 1
<img src="https://github.com/udexon/Multiweb/blob/master/Instagram/following_outerHTML.png" width=600>

1. Figure 1 shows the "Following" floating window on the left side and the DOM in the browser console on the right side, where the user attempts to copy the `outerHTML` of the first "following" account &mdash; `jenniferbllr`, which is show in line 2 of the following file:

- https://github.com/udexon/Multiweb/blob/master/Instagram/Instagram_Following.py

```html
<a class="FPmhX notranslate  _0imsa " title="jenniferbllr" href="/jenniferbllr/" tabindex="0">jenniferbllr</a>
```

2. We then extract all elements with the same classname "FPmhX", using lines 4 to 6 in `Instagram_Following.py`. These code were executed in Python interactive mode (`python -i`) together with `chromedriver`.

The URL of each of the "following" account is extracted and saved in `l_following` and written to file `following_jchastain.json`.

- https://github.com/udexon/Multiweb/blob/master/Instagram/following_jchastain.json


3. The User then logged out from Instagram as the following step (lines 17 to 33 in `Instagram_Following.py`) can be executed without logging in.

The number of followers of each "following" account was saved in a Python dictionary, which was in turn appended to `l_ig`, and finally written to file `ig_followers_jchastain.json`.

- https://github.com/udexon/Multiweb/blob/master/Instagram/ig_followers_jchastain.json

# PhosGraph Multiweb Instagram Ranking 

## Demo: Reddit "Uncensorable" Anonymous Comments

We demonstrate an almost trivial example of multiweb, where [anonymous comments can be added to Reddit posts](https://github.com/udexon/Multiweb/blob/master/Reddit_anon_comment.md) (click [here](https://github.com/udexon/Multiweb/blob/master/Reddit_anon_comment.md)), by modifying the HTML DOM locally and storing the comments on a third party graph database server. It is trivial simply because of the number of comments that can be made by one anonymous commentator. It will no longer be trivial if this mechanism can be replicated over literally billions of user devices (desktop computers and mobile devices).

The same techniques may be applied to crowd source collection of Instagram data, i.e. Instagrammers' follower count, perhaps the most sought after advertising statistics globally and locally. The difficulties in gathering such data is not unique to Instagram. Such data is either public available (e.g. Instagram profile can viewed without login) or available to individuals after login. What is lacking is a universal platform or mechanism to collect such data. Out solution is packaged as PhosGraph &mdash; a transient key (cryptography) graph database &mdash; an open graph database WITHOUT using the conventional Unix style username (hence centralized) authentication.


As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

Nouns:

user account, email address, username, posts, title,
content, number of views

account: id, email address, username
posts: id, title, content, number of views, account_id

accounts table:
id: serial
email address text
username text



posts table:
id: serial
title: text
content: text
view count: int
account id: int

account --> one to many --> posts



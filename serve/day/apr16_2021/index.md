# Friday, April 16, 2021

I had a random idea hit me this morning. I was watching a shaping video from
Tanner Bedheim and thought of some new art I might want to make for my
surfboards. I keep having these ideas and needed to note it down. Naturally
it went into the projects directory. But seeing that file made me see my
inspirations again. This is something I've been on about for the past
couple of days. I saw at the end of Tanner's video his instagram, which
is probably also awesome just like Matt Kinoshita's. However I don't use
Instagram a lot because it doesn't really work for me. With this said
I realized I wanted to have a feed collection. I want to organize my
feed collections however I want. If that be by domain, great. If that
be by something else, great. I just want a way to start categorizing
feeds so I can see them in one place so I can stop going fucking crazy
everytime I pick up a computer. So I can use these different platforms
to capture my interests not in one jumbled feed, but something more tailored
to really what I want to see. 

Sorry this is not very cohesive, my mind is all over the place right now
and just trying to get some things down before I start to go off.

At the end of the day I am thinking about writing a feed aggregator. 
It should handle

* YouTube
* RSS
* Twitter
* Instagram
* FB
  * Groups
  * Friends
* Podcasts

So let's get going.


Okay thinking so far a simple DB structure in SQLite.

The main queries I care about right now:

* list tags
* lists posts under a tag

I think this should be relatively simple. One thing that I hate about DB's
in general is I want to be able to have cascading data more easily.
That is a feed really implies a feed post has the same type. Or initially
that is the case, but may not be the same always. But here and now it 
would be convenient to cascade that data downwards on any query.

Structure as follows:

* Feed
* FeedPost
* Tag
* FeedTag
  * Many-to-Many: Between Feed & Tag


OH MY GOD VIM SURROUND IS SO DAMN USEFUL I NEEDED THIS
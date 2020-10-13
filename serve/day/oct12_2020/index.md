# Monday October 12th, 2020

## Weekend

Holy crap in a hat what a weekend. An absolute blast but also suuuuper tiring. But hey
gotta keep going. 

### Friday Night

* 🍻 Got beers with Yeabs. Some great conversation
* 🍻 Went to Fink's house. 
  * Had another beer
  * 🐓 They have chickens
  * Met Shep there
  * Talked with Gilchrist about Prop22 (he's a driver too and poli sci dude)
  * Etc

### Saturday

A LOT. To summarize:
* 🌅 8am wake
* 🏎 Watch f1 quali
* 🧗 Climb with Tatiana 11:15->12:45
* 🍽 Eat lunch at climbing gym
* 🧗 Go to `undisclosed location` (outside) to climb 2-5:45
  * Met Sam? Israel, Trevor, Will, Flora, Masha, Jason for the first time
* 🍷 Go to Bay's place, have dinner some wine, play Catan
* 🦞 Go dive for lobsties 8:30-9:30ish
  * With Paul, Michael, Julia
  * Go to Michael/Julia's place to cook [the crab](crab.jpeg). was delish
* 🛌 Drive home around midnight

### Sunday
* 🏎 Watch f1 race.
  * 😢 Lando with mechanical problems 
* 🚴🏽‍♂️ 10am bike ride with Cole -> 12:30
* 🧗 Climb 1:30-3 with Neha and Katie
* Watched [Valley Uprising](https://www.amazon.com/Valley-Uprising-Peter-Sarsgaard/dp/B01M3UPOWI)
* Went to Costco (need to make burritos again)
* Went to REI (needed a locking biner and better chalk)
* Watched [Meru](https://www.amazon.com/Meru-Conrad-Anker/dp/B07NVXTGN7)
* Bedtime!

## Today

We keep going. 

🌊🏊 Went for an ocean swim with Katie at 6am. From the Marine Room to the Scripps
Pier. Then a nice walk back with her.

I am thinking about a relatively long day today, but don't know how
that will end up working out. I need to cook at least one meal today. I am planning
on working more on the Vim plugin today. Hopefully can get some more basics working.
Really have no idea what I am doing.

Maybe I will write some script that builds an index page? I am really thinking about doing this. 

Need to be able to link multiple things with different 'reasons' behind them. One
link is so obviously not sufficient. 

Also really wanting something to keep track of people better. Have written this before
as well but might try to integrate it here, however maybe not served... Hmm not sure
how I want to do this because I would like to keep some of this data private and some
of it public. Need to think how this might be done.

### Quick NLP Research

Basically taking note of Spacy and NLTK. Will want to do Named Entity Recognition (NER)
in the future. However for today would like to break down .md into a tree (so you can 
make a block reference to anything in the tree (or graph)). Anyway.

### Parsing .md into a tree

I mean all I really want is to break things down into concrete block down to the 
sentence level while respecting headers. 

[Unified](https://www.unifiedjs.com) looks to have some utilities that should span
this nicely. However I am not sure I want to dive into this quite yet. It will be 
desperately needed. I am thinking about this mainly in the context of people. I want
to be able to write about people and attach people to people, but only have some of it
be public. That means being able to have very granular controls. I want to think about
this more so the tabs are going to get closed now.

### Brain

my brain is spinning (thanks coffee), but okay here are the main things to think about

* People
  * .md > tree. need this ability in ui too. 
  * What is the DB backing? This is an odd thing to have in a DB, but need to be able to cross ref. 
    * I think this raises a larger question. What all even goes into a DB?
      * schema.org?
    * Need to move to GraphDB
      * Neo4J? 
      * DGraph?
      * Grakn
      * How do you design an interoperable graph db? Has to be extremely generic...
* Index

### Index

First question is when to generate the index? For now it doesn't really matter. I think
I am just going to add it to my current watch script. Basically that means any time a
file is changed the index will be regenerated. This is so much overhead but whatever

Would like to add artifacts directly in as well, but we will see.

Okay so after taking some time to write the code I am a bit annoyed. Mostly at myself
for writing a hacky script. After this I am really finding out that I need a MUCH 
better way to work with this data how I want. I really am not sure how not to use a
DB at this point. I mean of course it is possible without, but there are many 
semantics from a DB that would be so helpful here. So the question then is
how to have a DB that works on an AST and links bidirectionally. 

This is a much bigger question and will need more thought. I don't really know exactly
what this means yet. 

For now the [index](https://www.daily.cjpais.com) will do.

### Music Industry

I mean Spotify is great and all but i feel like I am screwing artists. Also I really
wouldn't mind owning music again. Just wondering a little bit how possible it would
be to have ownership of music again. What does owning music look like? I mean
in general what does digital ownership look like?

Not sure if this is any different really, but could you essentially run a service for 
artists which allows them an easy way to distribute their music (by running servers),
but they can directly get paid for the album or song. Back to the iTunes model. I guess
the question is why did that model fail in the streaming era (well I guess a lot more
choice). But I am trying to think how you preserve choice as we have it now as well as 
provide a better service to artists. This is so not clear. 

Really I just want a distributed system where I can make micropayments to artists and
have it be transparent. They can set the price really. I wonder too what alternative
forms of radio would be created. I mean if one person bought the music do they have the
rights to rebroadcast it? I mean I can technically broadcast my spotify feed on the 
radio but I'm sure I would have someone knocking at my door eventually.

Wait this would actually be hilarious. I wonder if I could set up a radio station from my house which I could tune into from my car. That would be so good. I don't think 
there are any legal bands for me to do this though. I mean could do illegally but lol.

Basically there is a lot more thought to come, but is on the mind for sure.

### More research on .md AST

I think I've found a good set of libraries (and plugins + MOAR RESEARCH) to use for AST
generation and parsing. I think there is a lot to be done here to use it in a
meaningful way as well as with something to work with it efficiently 
(i think this will be the major challenge)

This is [unifiedjs](https://unifiedjs.com/). Specifically using remark and retext. I
really would like to explore retext more. I really like the fact that it is a 
'collective'. Love this idea and need more of it. Hope I can help to contribute to it

Not sure what I am going to do yet, but definitely need to play with it

### Life

Got dinner and a couple of beers with Katie. Lots of great conversation, but really
there is a lot more to say. 

Maybe I can share a few things. Ummmm her quantum physics? homework was fucking
gnarly as shit. Would definitely like to learn more just to understand and have
conversations. This would also be great to share with Adam S. Really would like to
start to review Quantum Country again

After discussing Prop22 with her I think my vote is drifting towards no. 
That is especially in the context of of uber/lyft aiming for self driving cars.
Is it better to support people now, and have them be reliant on these jobs when
they are obviously going to be taken away in the future? I think this is a hard
question but the reality is (as she pointed out) that people were able to survive
part time before these apps and they will be able to survive going forwards. 
Hopefully it will give the opportunity to people who do want to drive full time
to get proper benefits. I still think this is a hard decision regardless, but I am
starting to feel the vote drift towards no, which was aligned with my gut reaction.
Will still have to think more about it.

Going to try to dedicate 10min a day to RBG reading regardless of if I really want to
do it. Sometimes it just has to be done.

Of course the JMT as well, will have to really aim for this and prep for it.

Umm yeah lots more, but want to be a little careful how much to share.... But yeah
overall really great.

## Tomorrow

Man we have a lot, but there is always a lot and that's a good thing. 

10 min RBG
Quantum Country
JMT
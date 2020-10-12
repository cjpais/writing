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

🌊🏊 Went for an ocean swim with Katie 

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


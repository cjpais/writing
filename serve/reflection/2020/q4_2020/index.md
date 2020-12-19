# Q4 2020 (Sept - December)

## Into the Unknown

![Red Rock, NV. Oct 2020. First Climbing Trip](red_rock.jpeg)

Wow. What a wild 4 months. 4 months of the unknown. 

Below will be a summary of everything that I worked on or did during this time. However since this is a
reflection I'd like to tackle that up front. However it was not written until after everything was done.

There is a theme that runs through this document. It is one of play, but also one of distraction.

## Quitting Qualcomm

Yep. I quit my job without much of a plan. Initially I thought 

## An Adventure in Openness

## Finding a DB (First Week)

Since one of the big things I want to work on is private data, I was trying to figure out a good way 
to manage all of my private data. Initially my plan was to write my own DB. However, this idea was
quickly abandoned in favor of Postgres. However I didn't want to use SQL directly. I've found it effective
but always a bit of a pain. 

I'd been looking in this area for a while, and eventually it looked like GraphQL and Hasura were my
best option to augment Postgres. Once all set up I migrated my Podcast and Notes apps to use this DB
in addition to the CoreData DB they were using. 

Once this was done, I got thinking about another project. To display my financials publicly.

## Conversations
* Kristen Dave
* Kristen Dave Jon
* Weiwei
* Jon
* Austin
* Morgan
* Adam
* Shep
* Alex
* Chandler
* All climbing peeps, Caroline, Katie in particular

## RBG Passing

The death of RBG was tragic to hear, for the future of the Supreme Court, minorities (yes!
not just Women) rights, and much more. One of my friends is going to law school, and one of her
favorite classes was Constitutional Law. I asked her what her favorite RBG cases were so I could
read the opinions. I read 3 cases intending to write about each. I managed to do so just for 
Shelby County v Holder

* *Shelby County v Holder* - [[marked up pdf](../../../scotus/Shelby%20County%20v.%20Holder.md)] [[my analysis](../../../scotus/Shelby%20County%20v.%20Holder.md)]
* *Burwell v Hobby Lobby*
* *US v Virginia*

## Financials (aka. [burrito.place](https://burrito.place))

One of the more interesting things to me is the idea of transparency. 

Beyond just transparency, with this project I wanted to play around with the idea of directly selling 
my data as well as creating an exchange.

* Transparency
* Selling Data
  * Giving up Data for Discount (effectively selling your data)
* Adjusting price based on wealth. Flattening wealth inequality curve

One of the main reasons this never got finished was that my main two credit cards were not easy to 
get data from. This effectively killed the project. It was certainly possible to get my data
from CapitalOne (see my analysis), but I don't think it was worth the time to continue to engineer 
such a fragile solution. Beyond this, my Apple Card is the only other card I use, which doesn't
look like you can pull data easily from (c'mon Apple). Neither were integrated with Plaid at the time
of writing which was what I was planning on using.

While this project never quite got off the ground, I still think it is quite an interesting concept.
I would like to revisit this at some point. Wether it be for financial data, or any of my data. This
is one aspect of the technology industry I think could use some change and has lots of potential. 
# Tuesday September 22nd, 2020

### Summary

* Quick Bike (7mi)
* Wrote Grandmother
* Refined Questions for Weiwei
* Worked on [Financials](#financials) (using Plaid)
* Break
	* Ate
	* Walked to USPS
		* Sent *Never Eat Alone* to Taylor's brother
		* Sent Austin his notebook
		* Sent Granny letter
	* Ran home
	* Quick (7 min) workout, 5 pull-up, 10 push-ups, 15-squats on the minute
	* Shower
* Integrated podcast app with the main DB
* [Thought a bit about tomorrow](#tomorrow)


### <a name="financials"></a> Public Financials 

Thought about the flow for how I would like to start going about displaying my financials publically. The [GitHub Repo is here](https://github.com/cjpais/howmanyburritosleft), but it doesn't have much yet. No real programming has happened yet, just schema setup.

#### Key Ideas
The public facing version of my financials will be extremely bare-bones and stripped down. This might even be a statically rendered HTML page. If you are interested in more details on my financials I will be exposing those as well, but there might be some kind of paywall. I am not sure exactly how this is going to look yet. Probably will give anyone access if they email me <cj@cjpais.com>. If there is a paywall access will probably be in some funny tiers or something.

#### Today

Set up the basic schema for Investments and Transactions. It's all GraphQL via Hasura. Will be trying to use Apollo on the backend to play with. I'm also very curious if I can link this into my main DB via external connection in Hasura. That would be pretty awesome, though there are some things that would definitely be missing which I will need to consider or hack up. (Specifically how to add entities). Going through these DB's is interesting and helps to give me an understanding of what is existing out there. I would also like to play with a graph database. 

#### Structure I'm thinking of

Have 3 parts to the overall 'app'

* Private front end (to input credentials into DB)
* Backend
	* Runs every hour
		* Go through all accounts
			* If plaid (transaction)
				* Query plaid and update
			* Else (investment)
				* Go get the new value of investments
	* Additional tables to help fuzz data (to some extent, mostly time)
* Public Frontend (and API)
	* fully public statically generated HTML
	* Otherwise API based?
			
			
#### Notes from using Plaid API

So far the experience with the API is okay, but there's a lot of layers to go through. They really want to force you through certain paths, which forced me to rethink my own approach. This mainly had to do with login of financial institutions. It seems the best to go directly through their prebuilt front end flow ([Plaid Link](https://blog.plaid.com/plaid-link/)). Otherwise the API seems pretty nice and well documented. Definitely helped set up some of the tables I am thinking of as well. 

#### TODO

We have thought out some things and begun to flesh them out. So next steps:

* Really need to think how users are going to work in the system (especially for payment model)
* Start writing the backend code to add everything to the DB
* Start writing the public facing CSS/HTML

### Podcast Integration with DB

Oh man so many hacks but this is fun 🤪. So far my favorite is learning that in Go, [map access is not threadsafe](https://golang.org/doc/faq#atomic_maps). So what's the solution?! Just throw a mutex around it 😝. Didn't even consider where to throw the mutex, just put it around the whole func 🤦🏽‍♂️. For now this is fine, but really I will have to think about where this mutex needs to go in the future, it should be pretty clear, but the code is evolving so fast (over half the file is deprecated) that I am not too worried.

Anyway overall this was a massive success and went really fast. There were a few hiccups. Mainly with me not paying enough attention to the code. But anyway, all the podcast data from my podcast app is now going into this centralized DB.

Basically the central DB has an `entity` sitting over any row in any table. This allows any two arbitrary rows to be connected to eachother. I plan to use this in some sort of writing tool (with awesome autocomplete), to help write these faster.


### Today's Artifacts

* [Sketching on Financials](daily/Financials_sept_22.pdf)
* [Sketching on Podcast](daily/Podcast_DB_integration_sept_22.pdf)

### Interesting Things

May-li's thread: <https://twitter.com/mayli/status/1308287703268487171>

Also this: <https://twitter.com/mayli/status/1308605022276587527>

###Blah

My brain is starting to fall apart now. Definitely taking note of this and thinking of writing more as I go and making sure to take the time to do this.

### <a name="tomorrow"></a>Tomorrow

* Short bike (7mi)
* Think more about sign-up flow as well as start on HTML and CSS for user-facing
	* Sketches
	* Things I want to have (from overview to detailed views)
* Read *United States v. Virginia* @ Bay's?
* Climbing twice.. Noon and 6:45.
* Wine Wednesday
* Probably not publishing a daily tomorrow. Might come in Thursday's

### Coming Up

* Would like to write Swift API Library for ListenNotes
	* Hopefully use this to clean up my own implementation
	* Potentially add a cache here as well?
* RBG Page with Court Cases
	* Why?
	* What I don't know
* Direct flow from editing markdown to webpage without thinking at all (WITH SPELLCHECK)
	* RSS for this as well
	* Going to be called `reflect`
	* Will automatically take from my DB as well and this will serve as the `inbox` for things to process
		* Make it easier to make references and write directly about these things in the `inbox`
	* `inbox` will have inputs from:
		* cjplay
		* cjpodcast
		* twitter (if i dm myself lol)
		* strava
		* thats it for now but more as I write more
	* try to automate writing this page as much as possible. all the things a computer cannot do, but capture everything that a computer can and put it in a format that is readable.
	* automatic @ assignment for Twitter + Tweet generation?

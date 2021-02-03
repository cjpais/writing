# Tuesday, February 2, 2021

Curious to know if it would be possible to give my phone a static IP address.
Seems it would be possible if I roll my own VPN and tunnel all my traffic
through that. Then I can have the IP consistently be the machine that is
the VPN. This would mean though, that when traveling or whatever the latency
of all traffic could be a fuck load given that it is all tunneled through
the VPN.

Anyway an interesting idea. Something that may want to be explored in the
future more. I really just want to be able to talk between devices directly
even if it is connected via a cell tower. I don't want to jump to servers
you know.

Maybe the bigger thing is to bake in authentication to my stream so no one
else can hit it, even if they were to know the paths. 

## Money

I think we are going to try to get all of our big spending out of the way
this month. Any gear purchases/clothing etc. Just finalize really what
I need. If this means REI purchases this is okay. It will add to our
dividend for the coming year which should be significant.

* American Alpine Club
* Sierra Club
* Access Fund

## Day

Quickly going through..

Made some updates to the create-day plugin. This now will open the created
file in a window for VSCode. This greatly improves sanity.

Migrated my stream server to the web, it still needs authentication. 
This also means that all the apps are back online. They will need
graceful handling to log out errors and display them. This will
likely become some error handling library as I make more apps.

Got to do a lot more thinking about tags and tag systems, and more
what I specifically want. I just want to be able to intersect
and union tags. This seems like a simple thing to be able to do.
I think initially the simple design should work and ideally scale
enough. I think again some library or cache tag file might be
good to have just as an optimization or something. 

Also came up with some ideas, built on top of Linus conversation yesterday. <-- this should have context (also this is a sidebar in .md)
Specifically with regards to syncing. I think I am legitimately going
to host a git repo for myself. This will be the server (this really 
needs a backup). This makes it easy to work offline and deal with
merge conflicts. 

Apps can write into this git repo, perhaps via an API, which just
allows for add, modify, remove, commit. And can be done relatively
the same as anything else.

This also allows for easy syncronization. I think we can add some
more fancy layers on top of it if we really feel like it. Something
like RPC, WebSockets, Sockets, or something of the like.

Still really want to Colocate some server in San Diego. 
# Wednesday, February 3, 2021

Found out just now that the buffer adding didn't work :(

Will have to fix this at some point, maybe not today. Maybe tomorrow.

Got some decent work in this morning already. Got the stream authentication in.
Using basic auth even if not secure. At least will block most requests coming in.
This includes updating the iOS libraries to support this better. I think
shortly we will have to rename the server and refactor it to have some 
more level of sanity, however for now it looks to be okay.

I think we need to understand what streamable means and also create better
abstractions within the code itself to clean up the implementaion. I think
we need to remove the `config` files as well and finally use something proper.

Then after that we can start to build and reflect on the architecture of the system.
Hopefully it will be simple enough to be something relatively interesting.

I think we can also have this kind of shortcut page like linus has, but we
need to think of a way to do this effectively. I think we also will probably
turn the main website into some kind of webapp, and this should combine
some of the subdomains hopefully. 

This might be able to become something like a dashboard or a giant filter
on what I am doing. Initially it will start out as an entirely private web
app, also basic auth. Then moving onto something more complex from there
as necessary. Being able to add people into the namespace in a meaningful
and secure way.

For now we will move to working more on Meera's app Griefpal. I think
even if the features don't get done today, if we can get the backend
ready for them that will speed things up significantly. 

I think we also need to start documenting all these projects and their
current state and put them up on the website in some form. Basically
a log of what is going on and the current state with the intention
behind it.
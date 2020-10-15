# Thursday October 8th, 2020

## Prop 22

Just starting to think about this more. Seems like one of the biggest ballot measures
in California given how much money is pouring into it. Not to mention YouTube being absolutely
spammed by Yes on 22 that is almost certainly going to decide the fate of this measure

I am very skeptical of any measure that has ***184 Million Dollars*** in contributions from huge
tech companies. Unfortunately I have not done much research yet on this measure and AB5, however
before I vote I certainly will. My concern is if these companies are willing to spend this much
money, *they KNOW* they will be screwing people. They know that the cost of contributing is *CHEAPER*
than spending it on the people that make their service work. Not to mention that the drivers are 
already getting squeezed. Beyond that we know both Uber and Lyft are investing into self driving
cars, which will make people obsolete in their business model. So they are propping up an economy that
will just disappear in 5-10 years which will lead to even more dire consequences. I feel no sympathy 
for these corporations. 

Uber CEO - "We think we comply by the laws, but if the judge and the court find that we’re not... then we’ll have to essentially shut down Uber until November when the voters decide."

To me this reads despicably. You're telling me you are going to hold your drivers hostage until the
vote happens? And you will continue to hold them hostage unless the vote goes in your favor? How is 
this acceptable? No. Work within the bounds of the law and figure out something that works. You can't 
just kick and scream because you don't like something. Fuck you. You are a huge corporation. Figure 
it out. You have thousands of brilliant minds at your disposal. Use them to do better for the world
not just your shitty bottom line. Fuck your bottom line. I could give a damn about it.

Okay taking a step back and to just propose one solution. Instead of the law getting involved can we
work with an alternative business model? Can't you just set up a market where people charge their own
rates? This gives more free competition compared to this hidden algorithm and a huge company. I mean
this wouldn't even be contract work, just pure free market. I don't know if this is a good solution
either. I do believe people need insurance and all these things too that full time employees get, but
a system like this would be much more free. It's a tough thing to balance.

I recognize too that the bill itself does have some provisions that could be good for people. Again
I just have a lot of skepticism when this much money is getting thrown around if there is not a better
alternative (or if we already have a good one.. would this be AB5?).

Anyway these are just some initial thoughts on what I am thinking, but I will need to go waaaaaay
more in depth on the details of the bill as well as the implications of AB5 to vote effectively. I
will try to summarize my position as well once I've had time to flesh it out more.

Few quick notes. To change Prop 22 it will take a 7/8th majority vote. That is pretty gnarly.
Nearly unanimous. When drivers do not have someone in their car they won't be expected to be paid. Around 1/3 of their time is doing this.

Still this is tough because I understand the benefit of being able to work whenever. It will depend
what the actual text of the laws say. This is not a clear yes or no if you ask me. Initially I came off as very No on Prop 22 but the reality is right now I am undecided as I don't understand the consequences well enough to have my mind made up yet.

## CodeMirror 6 Extensions

So I am hoping to get an understanding of what is going on in the rewritten CodeMirror and it's extension framework.

I got a little bit lost while trying to go through the docs, so I figured I would just try to build an extension to help get an idea of what is going on in the system. 

I noticed that there was not any current Vim plugin so I started experimenting with how I could attempt to build one. I don't totally know what I am doing, however I do have some idea of "insert" vs. "normal" mode. I think the structure of the code has a long way to go. 

### Goal

The only goal I had was to start in "NORMAL" mode then be able to switch to "INSERT" and
back. This was not too involved, however getting it to behave properly like Vim is another story. I
think I need to continue to dig in.

### Building and Understanding

So an extension as far as I can tell is really anything. That is it is just something that is a value
or an array of such values.
I don't totally understand the implications of this, however it does make the system very nice to use
once you understand what is going on.

### References

Before going through anything you really should read [the system guide](https://codemirror.net/6/docs/guide/). This was a massive help to understand (however I didn't read it all lol, supplemented it with [this](https://marijnhaverbeke.nl/blog/extensibility.html) instead).

I took note of [fold.ts](https://github.com/codemirror/codemirror.next/blob/master/fold/src/fold.ts) and [commands.ts](https://github.com/codemirror/codemirror.next/blob/master/commands/src/commands.ts) for guidance on what I can do.

Also huge help was the [zebra stripe example](https://codemirror.net/6/examples/zebra/) and 

## Tomorrow and Other

Well I would like to continue on the Vim plugin. But I have a feeling that I will start looking more into the RPC method that Hashicorp uses. I think this pure JS implementation is good, but I would like to make the interface more generic and possibly more performant. That is I would like to treat the display of information as HTML (or some DSL on top of it), but the underlying code could be anything. Probably the DOM is one of the only things managed as part of the application. Perhaps there is some DB connection as well to provide basics.

Tomorrow morning will be climbing outside with Katie and others who I met yesterday so pretty stoked about that. Will be early and the drive is a little far, but hey it's okay. 


NEED TO SLEEP ASAP
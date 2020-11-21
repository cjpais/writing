# Friday November 20th, 2020

## Climbing

As good morning go, we climb again! Some trad leading and practice placement. Starting to get better. Feel better.
Understand what I am doing. Still a long way to go but this is good. Can't wait to practice more. Glad I did not
trad lead the ramp today, that was sketch. lol.

## It's 2PM

Yeah climbing in the morning takes a lot of time if you are not careful. It is hard for me to say no to climbing.
I don't really want to leave people with gear to clean up when I could totally clean it.

I have some things to do today, but not super defined yet. 

Mainly I think I just want to get some basic display set up for viewing routes and maybe some CSS that doesn't suck.
I don't really want to write my own so I might end up using tailwind because it doesn't look shit. However I might
try to go with something a bit more minimalist and static. Not sure yet. 

## CSS

Contenders:

* tailwindcss.com
* https://picturepan2.github.io/spectre/index.html
* https://fomantic-ui.com/
* http://getskeleton.com/
* https://bulma.io/

In reality I chose none because fuck I don't know what the design language is yet. I think this is something I want
to spend more time on. I definitely want it to have an outdoorsy feel.

For now fuck it

## App State

So one thing is when the app first loads we will want to get a bunch of information and just store this in the top
level state. That would be the gyms this particular account has access for. The walls in that gym and the current routes.
Do this so we don't need to keep fetching all the time hopefully. Not sure if Apollo will take care of this (it should)

## Gym Walls

Want to think more heavily about how gym walls are going to be structured. Need to think about it spatially which can
be quite tough. Want to know which direction and angle the walls are facing? Need to come up with some 3D representation
which can also be easily viewed. Probably need to look into how things are 3D modeled and how this can easily be 
represented in a postgres DB or some other format. Would like streaming 3D model format ideally. 


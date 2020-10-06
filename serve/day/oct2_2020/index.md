# Friday October 2nd, 2020 + the weekend

okay okay okay

got some coffee in me tryna fuck up the day now

thinking about this electron app it's so obvious this needs to be supremely modular

i am going to strip out codemirror and make it a 'component'

this allows me to do all kinds of things. hopefully can compose these components on the fly

basically am going to have 'workspaces' and 'components'

exactly the difference yet i am not sure. you can definitely embed workspaces within eachother and define actions on workspaces, however components are merely part of a workspace and can communicate with eachother in that workspace (and perhaps outside of it)

this definition is not clear yet but anyhow

## COOOL

one thing i think would be SICK. to be able to have code being written (say a python script) in one component then a terminal in another and directly be able to get the output. would also be amazing to have these scripts interact with the workspace itself (maybe this is an environment?)

environment > workspace > component

can this be nested infinitely? def is a graph so idk yet.

anyway time to PLAY

## HACKS GALORE

Honestly I'm dead right now. I can't believe how easy it is to get arbitrary code to be added to my electron app. I mean I haven't properly done it yet, but through the dev console it proves the potential. What I mean is right now I just have some basic stuff set up in electron. All it does is provides simple access to the window and then you can just paint arbitrary HTML on it. Again I can't believe this, because this should mean that it should be possible to execute arbitrary code in this env. I mean this is also hack as fuck. But it seems like it could be some real fun. 

So time to get a 'text' component built in:
This will be 'write in md' (with syntax highlighting) if focused. If not then it should render the HTML (maybe I will do this via webasm?n)

For now I want all of these to be linear (so its easy to see), then later change this to be arbitrary.

## more hacks

Basically I have no idea what I am doing. However I do have some semblance of a plugin system working. So you can help to define your own "workspaces" which are just a bunch of components composed together. More details to come as I continue to figure things out.

## Weekened

So busy, but in a good way. Just doing a summary here since I am writing this late and want to get to working on some other things

Saturday:
* 6am dive for lobsters
  * Get food/coffee with friends
  * Get dive flashlight
* Buy batteries and gear
* Go home, wash wetsuit and gear
* Attempt to fix car window getting stuck (disassembled the door and reassembled it.)
* Austin call
* Call parents
* Get food and go to BBQ
* 10pm go for another dive for lobsters

Sunday:
* Woke up late
* Brunch
* Bike to PB
* Lunch
* Bike back
* Return flashlight
* Call with swim friends
* Call with Kevin
* Call with Alex
* Make dinner
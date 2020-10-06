# Monday October 5th, 2020

## AAAAAAA
This morning was rough. Really beat from the [weekend](https://daily.cjpais.com/day/oct2_2020/https://daily.cjpais.com/day/oct2_2020/). Went for a bike ride with Alex (swam together in HS) which was good. He kicked my ass, was going fast, but was nice to chat with him. Had some nice conversation and very respectful. Cool to see where he's at and would love to try and help him in any way if I can. Will definitely need to reach back out and certainly go for some more rides.

After this ride I definitely needed some more motivation. I wasn't quite sure what, but I was listening to [Lex Fridman and Michael Malice](https://www.youtube.com/watch?v=BIk1zUy8ehU) and there is some fascinating discussion about the meaning of Anarchy here. Definitely a podcast I want to come back to and think more on. Lex so far (im about an hour through) is doing a fantastic job playing "Angel's Advocate" and taking Democracy's "side".

However even this wasn't enough to really get me going. 

Time to pick up a book! Austin ([Twitter](https://twitter.com/AustinTakeda), [YouTube](https://www.youtube.com/channel/UCcgdt0edaWlKEpUwPtXCrhg)) recommended this book a while back and I finally picked it up (after finishing some other AMAZING books). Definitely some good inspiration here, had to stop and write

## *Tribes* - Seth Godin

### FEAR

Okay so there was two "chapters" that made me stop. *The F Word* as Seth calls it and *Thinking Your Way Out of the Fear*. He acknowledges that fear is HARD. It is one of those survival things we have stuck in us. However I think in today's society we have too much fear and I certainly do. There is very little on a day to day basis that will harm me. In fact rarely ever is it the case. The mind just goes to the worst case scenario. Anyhow this topic itself resonated, but also what Seth talks about in terms of leadership. 

> It's the story of success, of drive, ***of doing something that matters***. It's an intellectual story about what the world (or your industry or your project) needs and how your insight can help make a difference.

I am not sure how to communicate this effectively, which is one of the main reasons I quit my job. Trying to understand how I can communicate myself more effectively. But in a sentence. Data ownership and expression in a way that can help connect us deeper with other people and engage in meaningful discussions. To connect "tribes". I don't think this communicates anything yet, which is why I am trying to build. I see in my head how all this data can be put to use, how I can attribute people effectively. Give back to the people that have helped me in any way. 

#### more on fear

Fear is one of those things I am highly aware of and actively try to put myself in situations that make me fearful (and actively trying to do better even at this). This weekend was definitely an exploration in that. Well went lobster diving at 10pm with some friends. The most awesome thing was that we were all terrified about this. Something about being in the ocean with just a couple lights at night is freaky. Getting in the water was no less so, but it wasn't a fear that consumes you. Eventually you just learn to be as comfortable as possible. It was awesome. Am I still scared of doing that again? Absolutely. But it won't be as bad this next time.

I guess this is also why I like climbing and lead climbing (and hopefully some trad too). The pressure of knowing you can fall 5/10/20/30 feet is terrifying but exhilarating. I am also not a big fan of heights, but this is all just mindset. Both of these things I am overcoming and it's evident in my climbing. It is still scary, but regardless. More practice and the fear will subside.

#### currently fear

I mean there are a lot of things I currently fear. But one of the biggest ones for me is meeting new people. I am not sure why because every time I meet someone it's always good. I have done a lot of thinking about this. It seems like it's down to wanting to be liked and coming off as kind. That's all. That's what I try to aim for in my life and not sure I always live up. But anyhow. Lots of work to do here, talk to more people and continue to enjoy the beauty of life.

## Exploration of VSCode Plugin Architecture

Okay VSCode is a huge codebase. I am trying to understand how they made their extension architecture. To me it is not clear yet, but I am looking to have something robust and not so hacked up like I have now. I want this before I really start moving on as it is already a pain to look at and I know it can be done much better. 

I would like to have something relatively similar. Basically a giant package repo, where .js is already 'compiled' and this can be added dynamically. I am expecting it however to interact with the DOM, however I think we are going to have a DOM manager or something. Maybe a workspace will implement something like SwiftUI to actually build a page. I am not sure yet. Fortunately this should be relatively tweakable.

### Some resources:
* <https://programmer.help/blogs/disclosure-of-vscode-technology.html>
* <https://stackoverflow.com/questions/60697207/architecture-for-an-extensible-electron-app>
* <https://code.visualstudio.com/api/working-with-extensions/bundling-extension>
  * > `// vscode extensions run in a Node.js-context`
    * does this mean they spawn node js process then use ipc to communicate with main?
* <https://code.visualstudio.com/api/get-started/extension-anatomy>
  * Activation Events... basically there is an `activate()` call that is mandatory. This func will be called when one of these events is triggered.
  * more...


#### [History of VSCode](https://www.youtube.com/watch?v=Tw8l0WzQxmY)
* Bad extensions can hurt a platform (eclipse)
* Must protect the core tool (VSCode) from misbehaving extensions (6:10)
* Importance of a "designed API". Extensions run in a separate process and communicate over RPC
  * Entire API is controlled from the VSCode side. 
  * Abstracted away from the internals. 
  * Don't see any of the internals when building an extensions.
* Everything can be done on desktop app and also web
  * This is essential as I will be publishing these. Does it get rendered out and served (static) or dynamic via node?


## other things id like

* package manager. you have one package manager, however the repos can be many
  * can directly pull from github if you like (this might require compile step however)
  * say can have primary repo, but then add secondary (user/private) repos
* extensibility, basically have extensions that don't have a hard dependency on another extension
  * this would mean they are publishing their data.

## main concerns

I think there are two main things to separate out. Basically providing an interface which allows rendering of the HTML content. (perhaps this is a function that gets executed with data? can this be done with react and vue?). Beyond just the plain HTML data I want to be able to have an underlying representation that can be shared with other modules. However they can request this information on the fly. Basically be able to inspect the types of data another component is using to render it's HTML. This is mainly to write connectors that are easily exposed.

These are some big problems and ones that will need a lot more exploration. I think for today I am okay saying this is done.

The next steps are to webpack individual modules so they can be loaded on the fly. 

## tomorrow

I am thinking about taking a little break from code, maybe go run to the park in the morning with my backpack some coffee. Write more about RBG.

Maybe wednesday is looking more like using the 'daily' workspace to actually go and publish something. Currently just have it hardcode the directory. It should create the right day if it doesn't exist then open the file into the correct parts (will need to think how I want to create components, especially if they are going to get added on the fly.. this might be something later down the line. really a text component should be composed of a lot of different things. you might write in one giant doc, but you can decompose it into many. this might be the way forward initially.)

lol maybe i will also look at atom's architecture as well
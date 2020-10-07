# Tuesday October 6th 2020

Gonna be a busy day already.. Had to take care of a few things this morning related to insurance.

Discussing the Supreme Court with Bay after lunch, then climb at 2. ~~Maybe lobster diving after.~~ Then call with Weiwei. If not lobster diving after the climb then ~~maybe~~ at night.

Was nice talking and catching up with Bay. Lot's of things going on. Man she is writing on an extremely hard topic. I am very interested to see where it goes. Basically is about how do you restructure the Supreme Court to take the politics out of it!!! This is a huge topic and very interested to see how it progresses.  

Climb was sick as always. I met Terry, who is also friends with Chris (an older trad climber who also shapes surfboards!?). Stoked on this. Hopefully go climbing outside soon.

## Plugin Architecture

Trying to look into plugin architectures in general now. I think I was diving too far off the deep end trying to grasp what VSCode is doing. 

So far:

### References
* [Patterns in Go](https://www.youtube.com/watch?v=_p7-BWCNzzc)
  * Go's `pkg/plugin`
  * RPC
    * benefit is multithreaded
* [Data Pipelines (with plugins)](https://medium.com/omarelgabrys-blog/plug-in-architecture-dec207291800)
  * Biggest things for me were. Store, Process, Consume. These are generally the 3 pieces of a core app. Need to think about each of these in context.
* [Plugin Architecture in Web Apps](https://stackoverflow.com/questions/10763006/plugin-architecture-in-web-apps-examples-or-code-snippets)
* [Create Flexible Plugin Architecture](https://stackoverflow.com/questions/2768104/how-to-create-a-flexible-plug-in-architecture)
  * > One effective way to make your application extensible is to expose its internals as a scripting language
    * See emacs
* ["Component Architecture"](https://trac.edgewall.org/wiki/TracDev/ComponentArchitecture)
* [The Plugin Pattern](http://www.iwriteiam.nl/PlugInPattern.html)
* [Eclipse Plugin Architecture](http://www.eclipse.org/articles/Article-Plug-in-architecture/plugin_architecture.html)

#### [Hashicorp Go Arch](hashicorp_go_arch.html)
I took notes on [this youtube video](https://www.youtube.com/watch?v=SRvm3zQQc1Q). It so far provided a great description of plugin arch using Golang, but ideally can be used for a lot of different languages

##### Sidenode:

[Go Proverbs](https://www.youtube.com/watch?v=PAAkCSZUG1c). some nice things about go

* the interfaces are quite small in general
  * can reimplement them yourself and this is SOOOOO nice
  * build components that can be shared
* use 0 values if you can
* don't use empty interface `interface{}` if you don't need to, dont need it as much as you think.

### Patterns
* Microkernel
* Loose Coupling
* Hollywood Principle
* Memento Pattern
* Dependency Injection
* Observer Pattern
* Mediator Pattern
* Strategy Pattern

### Other notes for moving forward

So far RPC seems like the best thing to me. I will need to go and review about RPC. Definitely have used it before when implementing a [distributed system](https://github.com/kkuo42/CSE223B-FinalProject) for school.

Might want to establish 'channels'... maybe similar to 5G.
This can also be thought of as messaging interface. Wonder how much this kind of arch can be used as well.

* broadcast channel [pbch] (host -> *) (* -> * ????)
* control channel [pdcch]
* data channel [pdsch]
* log channel [none]

### TODO READING (TOMORROW)

* CodeMirror/ProseMirror
* [Hashicorp Plugin](https://github.com/hashicorp/go-plugin)
* Microkernel pattern
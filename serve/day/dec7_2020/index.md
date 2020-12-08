# Monday December 7th, 2020

Spent most of this morning looking for places to live. Just need something cheaper to live.

I am still tired from the weekend for sure. I need to reboot my brain into doing things I
think. I certainly will need to leave better TODO's for myself (specific and small things
to accomplish on a Monday after adventure). 

Incredible weekend as it were. 

Met Dylan, Summer, Sydney, Eric. 

Good climb the first day (onsight 10b!), but had to go set up camp quickly afterwards.

Sparing some detail, but second day went to do Cat in The Hat (5.6, 6 pitches, trad) with
Rich and Summer. Got a little lost on the way to the start, had to wait a bit as we
were following another party. Ended up starting around 12. Rich led the first two pitches,
then me for the next four. Was great doing some trad, learning a lot. Lots of learn.
The whole thing was an adventure. Ended up rappelling in the dark. It was also cold.
Ended up back at the car around 9PM. Solid full day of climbing, and intense for me.
I was broken, hungry, and thirsty afterwards. Definitely type 2 fun (sucks during, but
looking back was pretty fucking sick). Amazing for my first multipitch experience.
Definitely was not expecting to lead 2/3 of the climb especially given my level
of trad experience! I was hesitant to lead a single pitch, but Rich really helped
to encourage me. Really appreciate that. Learned a lot from him and still have more
to learn I think

## This Week

Thinking about the stuff that I would like to do this week, it looks like...

* Make QR codes for Sport
  * Add in icons?
* Think more about publishing strategy and potentially writing VSCode plugin?
  * Find out a sane way to have a directory structure. Ideally plaintext
    * Or dynamically creating one?
    * Again upspin?
  * Tag precedence?
  * new file templates?
* Visualize point cloud generated from camera
  * Look at the google paper and smartphone estimated depth
    * depth from motion
  * how can we recognize arbitrary things, with fixed location
    * simplify the problem.
* Apple article


Tomorrow:

* Bike ride
* Plan where we are going to do a mushroom trip
* Apple article 
  * outline and
  * Record video
* Grocery store?
* Go tour the house at 1:30
  * Text Rich
* think about tagging and generally site generation (with dynamic URLs)
  * want a file in plain text to describe the metadata
  * .<filename>.meta
  * what does the interface in vscode look like to make it work?
    * ie multiple workspaces within the same directory
    * define workspaces adhoc
    * change workspaces (and associated tabs using kb shortcuts or button?)
    * have custom filtering rules for "directories"
      * really this starts as time
  * maybe take a step back
    * what is the basic problem to solve?
      * dont want to type the date out every single day and create new folder and file
        * this can be as basic as python doing it, or as complicated as VSCode plugin and
      * have a 'focus' mode for just todays stuff
    * would ideally like to have a more complete solution
      * if i got a new computer, I don't want to set up the same script to run
        * then a specific directory structure
        * then a server on the other end to make sure it listens
      * how can it be packaged more cleanly?
        * it's not that these pieces individually are bad, but its more the whole thing does not appear to work cleanly together as a system
        * i mean obviously a better environment would be to have an app which directly gets written in and then this publishes directly to a server with some real requests
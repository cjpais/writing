# Wednesday December 16, 2020

Okay time to get started for the day.

Thinking about what we need to do it becomes a few things pretty quickly.

* Send emails once the group is formed (guess I'm spamming myself today)
* Table for latest added users on the front page
  * This can be very simple without any sorting or business
  * Just needs to paginate (and have an API returning all people sorted)
* Unmatched users
  * a table where you can select and filter users
  * want to find a good library for this and then style. 
  * we are going to do this first


Need to do something to fix my goddamn shell. At what point do I just have a docker image which becomes
my primary and forget about everything else. Seems like so much overhead but yeah. I don't want
to have a lot of dependencies when using a computer. It should just work and continue to work in any
state.

Great. So nearly everything is done. I am able to send emails and have both tables functional.
Ended up using `react-table` which is a great library, provided you don't mind not programming
in typescript for a bit. For the most part this is okay, but irked me a little initially.
Best to just use `.jsx` in the future to avoid any hassle.

Since basically everything is done I went back to look at what still needed to be done.
That is one thing in particular.

Delaying sending out emails until Meera has actually clicked the button to send it.
This would also need some functionality to add people to the groups as well. This
does not seem so easy, so will leave it off for now. The delaying part can easily 
be done, so that one I can add no worries. The next one I am not sure a sufficient
interface off the top of my head which is making me think best not to for now.

Anyway, that will likely be a task for tomorrow, but may try to tackle tonight.
Should just be creating a new endpoint to get the groups which don't have emails
sent for them. Then on top of that another endpoint which takes the group id
and actually sends the email. This is something that can be added to the dashboard
as well

So for tomorrow:

Morning:
  * Fix multiple input bug, make sure columns appear correct to sort (going into DB)
    * fix: strip spacing
  * add pending groups to the dashboard
    * pending groups endpoint

If we go fast can finish (by 12):
  * replicate the group page for pending, but add additional button to send the email out to the group
    * endpoint to send the email once good
  * change grouping logic
    * if the email has not been sent yet, then group the people, but allow more to be added through the algo
    * group can only be formed once

After that may want to think about:
  * Partial match
    * Have Meera be able to see good potential candidates for the group
    * I think this can wait if the above functionality works.
  * Review Jon's comments, and do some rewriting.
  * Sport QRs and test prints
  * Get basic tailwind css project running to move everything over to.
    * then think about CI pipeline, for rockaholic.
    * or visit other CSS frameworks, to make sure I don't go insane using CSS
  * begin working on sign on and approval flow
    * roles
    * think about discord/teamspeak and role based access. i have one account but can have different permissions on each 'server'. Same should go here.

3 month reflection, just the outline

* financials
* daily's (started a week after)
* reflect
* new home page
* dawn patrol group and outdoor climbing
* plugin arch
* climbing gym app
* meera griefpal
* outdoor climbing ar
  * photogrammetry research
* lobster diving
* katie and mild depression
* rbg passing and analysis of court cases
* van research
  * van finding script
* red rock
  * oct
  * dec
* j tree
  * paul
  * backpacking
* valley of the moon
* first trad
* first multipitch
* thanksgiving
  * climb with luis, kaiti, dean
* visiting home
  * climb with cousin, dean, friend
* first time driving off road?!
  * now i want a 4x4
* reviewing markdown editors

from all of this what have i learned
* looking for love, trying my best to give it, to strangers
* need to stay focused on one thing and keep to it
  * ive gotten a lot of knowledge in a lot of areas, but not finished a lot of projects 
* i love to climb, but if i do it too much i have issues
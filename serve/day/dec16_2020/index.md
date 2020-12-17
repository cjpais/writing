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

So for tomorrow (finish in the morning):

* 
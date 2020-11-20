# Thursday November 19th, 2020

Writing again after Jon mentioned it would be nice to get updates. Will definitely write then. 

Perhaps it will become weekly as suggested but probably daily for now is fine unless I'm going on trips and stuff.

There's been a lot going on, basically all thinking about van and climbing right now.

## Today

Climbed a bunch. Harder stuff than normal, you can track my climbs outside (most of them) on [Mountain Project](https://www.mountainproject.com/user/200283598/cj-pais)

Got lunch with Morgan

Got a bunch of gear from Backcountry
  * CAMS!!!!!!!!!!!!!!!!!!
  * Boots
  * Carabiners (lots.)

Working with React and Apollo

Want to make sure things are loading from GraphQL when the Component is mounted/rendered.

## React

Working with Apollo is pretty great so far (am i getting ahead of myself?)

### Climbing Gym Web App

Basically thinking about the structure. Don't think the user should be able to edit routes unless they are logged into a gym. 
Most of the time you will only be logged into one gym at a time. You could be a setter who is setting at multiple gyms however.
Being a setter should give you 'permissions' to edit this kind of information. This can also be done by desk staff or really 
anyone really. However they might not be able to add 'walls'.

Thinking quickly of permissions:

* Admin (Owner)
* Staff (Desk Staff)
  * Maybe what they are trained to do (give belay certification, etc.)
* 

Want to think about how this DB can be explored from the non-gym side and how that will impact the gym experience. 
For example want to provide this service to every gym for free, but this implies a listing that will go into the 
climber app too. Because of this we definitely want to verify physical locations, but not sure how that can be done
yet. This is something to think more about in the future. For now we want to get more UI working...

Specifica
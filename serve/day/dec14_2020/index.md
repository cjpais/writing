# Monday December 14, 2020

Been mostly working on griefpal today. Just migrating everything to a new system (previous was a hacky ass script, needs to be updated now).
Running a Google App Engine script when someone submits the form. This then hits a web server and adds it to a DB.

That is what I have done this morning.

1. App Engine -> POST to Server
2. Golang Server to receive
3. Set up SQLite DB

Now will set up a couple endpoints. Then it will be to import the test data into the db and actually send emails out.
If that is done today I would be stoked. That just leaves tomorrow to actually build a front end.

Okay so looks like we will have a few things for tomorrow. Looks like this could take 3 days. Will have to see 
what tomorrow looks like. I think it's very possible to have the SQL done in a few minutes in the morning ideally.
After that at the bare minimum we will have the endpoint up. From there we can take the css we are using on the 
rock climbing dashboard and clean it up a bit, maybe a drop shadow to the right or something. 

It will probably be a very empty dashboard, but that is fine. Maybe can show the most recent sign ups.

Anyway was able to finish up the sql endpoints, might need to make some more tomorrow, but this is okay for today.
Learned a bit about SQL as well. It's been a while since I've had to craft queries, almost always used an ORM
before but really crafted them today. It's an odd way to think. I understand it, and I know it must be possible
but it's not always immediately intuitive the best way to make the query. Seems like there are a lot of ways
to do things 'wrong' and have performance be impacted massively.

Already wrote for tomorrow but here it is again:

* spin up react app
* simple dashboard
  * home
    * shows number of unmatched people (and a link to the unmatched tab)
    * shows the total number of people signed up
    * shows a list of the 10 latest sign ups
  * unmatched
    * just a simple table for now
      * checkboxes in the table to manually assign group
      * simple filtering at the top of the table
  * groups
    * show the groups in some simple bubbles or something
* start sending out test emails

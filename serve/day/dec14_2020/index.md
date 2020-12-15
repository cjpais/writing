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
Forgot to include the date in the DB, but can easily add this.
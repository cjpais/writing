# Monday December 14, 2020

Been mostly working on griefpal today. Just migrating everything to a new system (previous was a hacky ass script, needs to be updated now).
Running a Google App Engine script when someone submits the form. This then hits a web server and adds it to a DB.

That is what I have done this morning.

1. App Engine -> POST to Server
2. Golang Server to receive
3. Set up SQLite DB

Now will set up a couple endpoints. Then it will be to import the test data into the db and actually send emails out.
If that is done today I would be stoked. That just leaves tomorrow to actually build a front end.
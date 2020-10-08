# Wednesday October 7, 2020


## Upspin

Okay fuck it after watching a few videos I'm going to try to use upspin again. It looks kind of dead at this point but I still love the idea behind it. A 'global namespace'

Maybe a few more words would be helpful. The concept is in some way to bring data back to the person who created it. Everything you create is under your namespace unless you are explicitly working under someone else's. You can give very granular permissions to everything in the namespace as well. Everything is also very secure and encrypted by default. I really recommend reading more about the project <https://upspin.io/>.  Upspin has 4 main components from how I understand

1. Key Server
  * Hold's the public keys for everyone who registers with the system  
2. Directory Server
  * For a particular user this server will help locate specific files
3. Store Server
  * Actually serves the files for a particular user (finds the hash of a file)
4. Client
  * ME!! Trying to access files or whatever.

Perhaps this is all not needed with IPFS, however maybe really IPFS needs a layer on top of it to have a private namespace? Perhaps this is something that is possible. I am mostly looking to use Upspin so I can have `me` actually write a bunch of files into it. Then different `servers` which have certain permissions to actually serve files. Eventually this would mean signing people up into upspin itself and they would get served files based on their permissions.

### Installing and Setting Upspin Up

#### 1. Getting Upspin User

Install upspin
```
go get upspin.io/cmd/...
go get augie.upspin.io/cmd/upspin-ui
```

Launch upspin-ui

Run `upspin-ui`

Register email. Make sure store private key safely.

#### 2. Deploy Upspin Server

I am setting up my own server. This will be the store and directory servers.

Run `upspin setupdomain -domain=<yourdomain>`

This will create keys. You will also need to add a TXT record to the domain you own

You also want to make sure you add an A record for `upspin.<yourdomain>` which points to your store/dir servers.

Make sure you download upspin cmd line tools again on your server 

`go get upspin.io/cmd/...`

I run multiple servers on the server I will be running upspin so I need to change the defaults. It will try to serve on port 80 and 443. I want to serve on ports not exposed outwardly, then use `nginx` to expose.

Added `upspin.conf` to my `/etc/nginx/sites-available` dir and symlinked it to `/etc/nginx/sites-enabled`

Create upspin user on server

```
server# useradd -m upspin
server# su upspin
server% cd $HOME
server% mkdir .ssh
server% chmod 0700 .ssh
server% cat > .ssh/authorized_keys
(Paste your SSH public key here and type Control-D and Enter)
server% chmod 0600 .ssh/authorized_keys
server% mkdir -p upspin/letsencrypt
```

On local machine build `upspinserver` then scp to remote

```
local$ GOOS=linux GOARCH=amd64 go build -o $HOME/upspinserver upspin.io/cmd/upspinserver
local$ scp upspinserver upspin@<your server>:upspinserver
```

Since upspin is being served behind a reverse proxy I am doing 

`./upspinserver -insecure -http :port`

I am not sure this is the best thing to do. However I am serving still via https.

Finally actually set up the server

`upspin setupserver -domain=cjpais.com -host=upspin.cjpais.com`

#### 3. Misc

So I played around with this just a bit and there are a few things that you might also want to do.

One big thing would be `upspinfs`. Basically this allows you to FUSE mount upspin. That means you can treat this remote server as if it is a local disk on your hard drive. I ***LOVE*** THIS CONCEPT.  

One of the first things I did was to clone my [writing repo](https://github.com/cjpais/writing) which is how this site is ultimately served. What this means. I do all my work in upspin and without even committing to git I can serve the new files <3

This also totally means that you don't need git/github at all. Which is great, however it's nice for revisioning things. 

The first is on the client side (my mac). This is to edit your config at `$HOME/upspin/config` to serve a cacheserver. This dramatically improves the performance of `upspinfs`

#### 4. Welp

So running into some fundamental issues with Upspin. Can't create "Access" files. After using the cache *everything* broke. On all systems.

I actually tried to spin up a GCP instance to see if it was a problem with my server's latency or something. Appears not to be. I mean I was able to clone a git repo successfully, but sharing with another upspin user was fucked. I am guessing the system in general is not maintained very well any more. Unfortunately had to find this out the hard way. I think some people are still using it, but I need something a little more reliable i think. Maybe I will come back to it to dissect what is going on, but probably need to move forward in other directions. 

Maybe SSHFS would be better in this case. LOL JK ITS PERFORMANCE IS TERRIBAD. Basically my whole FS crashed on MacOS.

### Resources 
Reading and watching about [upspin](https://upspin.io/) to refresh myself.

#### ["State of Upspin"](https://www.youtube.com/watch?v=ixjV6zoIXfQ)

Mostly going over the basics of how Upspin works. A good introduction in general. Very short.

#### [Rob Pike's Overview](https://www.youtube.com/watch?v=ENLWEfi0Tkg)

## Code Mirror 6

Only got a few minutes to really start diving into the docs. I think the entry point I need to look at more is `Configuration.resolve`. Fortunately the CodeMirror code so far is readable. I think there is a lot I have to understand yet, and lots of playing around to really get at what's going on. Should be interesting to see further.


## Life

Needed to end things a bit earlier today, also had a late start because of a late night yesterday. Overall was still really good, finding effective time to eat is hard. However I am watching youtube videos related to what I am doing now instead of random tv which is very helpful. Keeps me in the zone. However I also need to go for walks as well, but this takes discipline. Getting up early and going to get the day started up real fast. 

ANYWAY

back to life

Ended early to go get dinner with Cole, Colleen, Michael, Julia, Christina, and Paul. Got Dirty Birds which was nice. A bit full cuz I ate at 3. Unfortunately/fortunately had some miscommunication with Tatiana and the climbing reservation was cancelled. However, I still went. As I walked in I asked a dude washing his hands if he needed a partner. He said I could join with his partner. I was stoked. So I met Steven and Katie both really fun people to climb with and people who like to go a lot. This is the best thing ever. I AM STOKED. Apparently they have a couple groups of people who climb IN THE MORNING! DAWN PATROL. IM STOKED AGAIN. AND OUTDOORS. FUCK YES. FUCK YES. anyway im about it

I need to get a bike ride in real quick too. Probably just fuck around a little.

## Tomorrow 

I think going over CodeMirror 6 more to understand how it is working. Maybe play around with the Vim plugin and perhaps try to maintain?

Probably dedicate some time to also going over hashicorp plugin again, really just beating this into my brain. Maybe friday or monday I will start implementing some sort of plugin system based on top of these two arch i am seeing. I am thinking of going the rpc way to have really arbitrary execution. I mean I would like to write things in Go basically. There is definitely a sacrifice of portability. Some of these things can actually run over the web too. So then it becomes a question of API. These are big things to think about. I think CodeMirror has an interesting extensibility model and this should serve as some inspiration. I think this is how I want 'extensions' working with eachother. Something that is very easily extensible. 

I also would very much like to contribute to Athens
Other things on my mind of course are podcast transcription

OH TWO NEW THINGS

* Be able to live stream this (aka am I typing? am I connected to this session?)
* Put audio in markdown? Would like to be able to embed video and audio throughout the day. Need an easy way to capture it and import.
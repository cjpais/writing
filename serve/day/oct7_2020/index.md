# Wednesday October 7, 2020


## Upspin

Okay fuck it after watching a few videos I'm going to try to use upspin again. It looks kind of dead at this point but I still love the idea behind it. A 'global namespace'

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


### Resources 
Reading and watching about [upspin](https://upspin.io/) to refresh myself.

#### ["State of Upspin"](https://www.youtube.com/watch?v=ixjV6zoIXfQ)

Mostly going over the basics of how Upspin works. A good introduction in general. Very short.

#### [Rob Pike's Overview](https://www.youtube.com/watch?v=ENLWEfi0Tkg)



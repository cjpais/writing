# Monday, May 17, 2021

Thinking about decentralizing my own compute infrastructure using existing technologies today.

Some of this may go into some more mainstream things (that I've not used before), something
like AWS Lambda or Cloudflare Workers.

Ideally mostly things backed by IPFS.

## Websites

### cjpais.com

This was a relatively simple deploy. However I moved all of my 

### daily.cjpais.com

This one requires more thought. Right now it is served from a Go webserver
and updated periodically on commit. Fortunately all of this could be 
migrated to IPFS relatively easily since it is all static content.

I decided to use Fleek for this and it seems to work? One problem
for me is the amount of build minutes is quite high.. Especially
since this is just a static website. I'm not actually building
anything so it should just be serving static files. It is also
worth noting that their CDN seems quite slow. Or at the very
least a lot slower than Pinata and Cloudflare.

I think I still might write a GitHub Action for this but
for the time being this will work I guess. Something to think
about tho for sure.

### stream.cjpais.com

Now this is an interesting one. The stream is more complicated
than these static sites I am serving. It has an API on the backend
which I do want to deploy to something like AWS. However, it's also
worth noting that ultimately here I am still just serving a file.

I am not sure what I want to do with this. Do I want to strip the Go
service down? How easy would it be to translate to AWS Lambda? How
can I modify a file on IPFS using it? 

The problem with using something like a serverless technique is I've
been building on very simple OS concepts which seem to not exist
anymore, or not quite the same.


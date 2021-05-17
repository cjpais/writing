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
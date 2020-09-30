# Tuesday September 29^th^, 2020

## Summary

* Bike Miramar Lake
* Read 2 Ch's *Understanding Comics* - Scott McCloud
* Financials

## *Understanding Comics*

## Financials

### Script Troubles

So I left my script running over night and unfortunately I got logged out at some point. Bummed about this. I think there might be a cookie rotation they do to really ensure. I might have to respond properly to these requests to update the cookie I have stored. May need to dig deeper into the login flow instead of trying to hijack an existing session.

Digging through the Capital One Login I see a few things. It looks like when the form is submitted they generate an encrypted username and password. There is also another Base64 encoded payload with some fakable params. I am not sure all the things they are generating in that. 

I dug through the code just a little bit and saw some public keys that looked like they are used to encrypt the username and password, however it didn't look super deterministic. It seems there might be some other injection there to help rotate the encryption or something.. I am really not sure here. I notice they are also generating JS which gets sent to the client, I'm wondering if this has something to do with it. 


#### Public Keys
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzIRgyU/g0W9Xiuv1ZUU8
8y/msQmyjTB4jaCDW5g6CxMQuiyavpPNpcqm3X2Cu6JV3XnvpzOplI0CmTHr3Wwz
HRtwc0xFiDUu5hqcI9bXlcI1wMpUqDemCOg4ya7v03ONFEqErXNuvPFebQ5bwTds
sOv619TNjP/oxUGrVXIHl7B8ai9o6/w2IF+OF/a3UpVCIjiqVSqizQXu/xdsSsqw
N+mBCR2vBGeJzabCJNmUE284/f15R08KWCyAr0QF1r8ih1MwqOVjFrcmoevWS09v
1y9tAB6ksnmL1511mewxpa3J6Nn9u4KvBYtfkwopy42HOlQvMEmJBBtleKYkE5u8
sQIDAQAB
-----END PUBLIC KEY-----
```




``` 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiwcxZqZy5tgQiWuI6e0r
zoBelUXEuxtNLeCqFChS4peivGH0IP+QDnp2tOKQ2dA3sT8qu5YdOXhOc5RXC1Kq
P/Bbhvk0/R4m5UgPtq8YQcpbrC39GLyIWSEpGgDq7adjBa3cDoQdtkG3AfYVP6rK
FpKpMZZi0/MzUf+FMLnydqDez2pHAXzZTefq4OaUukBiKum764z7hEtNmxHQd4LN
hxcz6CHDlPyuWRYkDQt6S1iPCFnT0VZTjaEFTyUIMFDFFT1FhBVW+D9CIaLu/WAC
Az4QKEilsYZGOn7+vMhozKz2yzVFzRQI/r+WvnBzVFaY4BbbJd37dFzggpsUf+ze
9wIDAQAB
-----END PUBLIC KEY-----
```

For now I am going to let another experiment run (logging what cookies it wants me to set). In the meantime will start to refactor and see what I can do. 

Also if I do try to go for this login method I will probably do this with a headless browser or something, then hijack the cookie and use it.

So over 4 hours still logged in. This is good, but need to catch any failures.

7 hours and still in...

### Refactor

The refactor into a `CapitalOne` client was super smooth. Stupid easy and makes the code readable.

While refactoring more things I realized that it might be good to separate all this into a library. I think I will call this `hyperverse`. This is something that will need more thought, so I am continuing to work on the existing code base then decide how it should be split later.

Hmmm so even that is going to need more thinking. I do not want to over-abstract right now. I can think of a few ways but we just need to start writing the code. For now I have just set up the structs that will ultimately be sent out in the GraphQL queries.

#### [Notes]()

## Speeding up Daily Generation

Yesterday I had a lot of problems with generating this page. Well mostly that it was really slow and painful. Today I am starting to write some SW which should ease the pain before I start figuring out really what I want.

### Issues with the old workflow
Previously the workflow was

1. Write .md
2. Generate .html
	* Don't forget to include CSS/Container styling
3. Git commit (on local)
4. Git pull (on webserver)

We basically want to automate all these steps except 3. 3 is basically me 'publishing' so I am fine to keep this manual. I might later automate this, but for now I will keep it under my control. (the automation would be on save go `git commit`)

### Automation Time!

#### Fixing pain between markdown and html

First thing is when I save a .md file to trigger html generation so I don't have to think.
I normally would do this with `inotifywatch` on linux, but I write on my Mac. Looks like there is a similar tool called `fswatch`. I will use this instead

`brew install fswatch`

After installation I needed to think about what I want the trigger to be. I am thinking any .md file which is modified. 

This ended up being a bit more of a pain than I expected. `fswatch` doesn't quite behave as I would expect it to. Specifically `-i` & `-I` is for inclusive regex. However by default EVERYTHING(!!) is included. This means you filter out everything with `-e .*` then include back what you want with `-i *.md`

Ultimately my command/script ended up as:

```
fswatch -xnr -e ".*" -i ".md" ../serve/day | while read file event; do
  python3 gen_html.py $file
done
```

Basically what this does is look for any `.md` files that have changed in the dir `../serve/day` recursively. If a file has changed, then `gen_html.py` will be ran with the filename.

`gen_html.py` is a little script that does a few things

1. Gets the `title` of the markdown file
2. Generates html using `pandoc`
3. Inserts this generated html into a template
4. Writes out the final html output

lol this is basically dead simple static site generation

Anyway this helps to alleviate the pain between 1 & 2. This is great. The number of [button clicks was too damn high](https://cdn.theatlantic.com/thumbor/KPisRFSKxm2kRRbtiobDJWgKq8M=/0x217:3358x2106/720x405/media/img/upload/wire/2014/08/26/AP101018137899/original.jpg)

#### Fixing pain between commit (on local) and pull (on webserver)

Okay so now that we have this html we want to make sure the webserver gets it. (i guess i could host on github, but whatever for now we will do this. maybe later move to github just so other people can deploy easier. at least this is a good local webserver 😋. some of the reason I am not sure about moving it to github is that I might not use git forever. right now it is convienient, but not sure if that's really what I want.)

To do this I am going to use [git hooks](https://githooks.com/). When I `git commit` something I am going to send a ping to the webserver to tell it to pull down the latest commit.



## Questions

### Is it possible to have a spreadsheet view of a GraphQL DB?

What I mean is it would be pretty convienient to have some times. Then apply formulas directly on top. But also have it linked to all my other data. Even for some data input this would be suuuuuper nice. Like right now I have to manually input a bunch of data for my investments.

```
query GetPlaidInstitutions {
  financial_institutions(where: {financial_plaid_items: {id: {_is_null: false}}}) {
    id
    logo
    name
    plaid_insitution_id
  }
}
```
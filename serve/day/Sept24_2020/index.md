# Thursday September 24th, 2020

## Summary

* Called Austin.
	* Set up habits (working towards wig)
	 	1. call one new person per week
		2. publish these 'daily' at least 4 times a week
* Fixed minor bugs in the podcast app 
* Started working on burrito.place (my financial data)
* Quickly working on more mind mapping all notes w/Jon

## Quick Podcast Update

* Make sure new episodes are being updated to DB when they are added into the app
* Make sure bookmarks are added when a user adds a bookmark to the podcast
* Make sure the app doesn't crash [stream.cjpais.com](https://stream.cjpais.com) (lol)

## [burrito.place](https://burrito.place) (aka my financial data)

### Color Scheme

Decided to go for a [CMYK Color scheme](https://coolors.co/eeff77-ee77ff-77eeff-000000-ffffff) - Reminds me a lot of printer colors. Thought it was fun and maybe retroish. Maybe just plain ugly, but I think it's cool. I was just playing around with 3 digit color codes starting at `#fff` and changing a couple of numbers. After I found a color I liked (`#ef7` was the first one) I just took all the permutations of the 3 characters and picked the ones I liked. Likely this is going to get expanded when I need to make graphs.

|Color Code|Color Name|Sample|
|---|---|---|
|`#7ef`|cyan|![](cyan.png)|
|`#e7f`|magenta|![](magenta.png)|
|`#ef7`|yellow|![](yellow.png)|
|`#fff`|white|![](white.png)|
|`#000`|black|![](black.png)|

### Raining Emoji Background

For displaying my financials I thought it'd be fun to spruce it up with some flying emojis in the background 😄. You can see the effect I am going for at [burrito.place](https://burrito.place). I ended up using [tsParticles](https://github.com/matteobruni/tsparticles) which is a JavaScript library which seems to handle this kind of thing quite nicely. It allows you to specify images for the particles as well. I used the [Twitter Emojis from iconify](https://iconify.design/icon-sets/twemoji/). The performance seems acceptable to me. However I can tell it is tough on machines. My MBP always spins up the fans real fast. I am guessing there is some GPU rendering or something that is not entirely optimized. 

Before ending up on this library I tried a few approaches. Initially I tried to use pure CSS since I thought it would be a performance advantage. It definitely is possible to get it to work, but I thought the performance was bad. In particular I saw a lot of frames skipping. The code to accomplish it was also quite ugly. Once I realized how ugly it was going to be, realized JS was probably going to be the way. So next I tried JS, and found [someone doing something very similar](https://codepen.io/robertheiser/pen/NXrqXa). At first I thought this was perfect. But I played with the code for a bit and realized man the performance was not so good once the page started to rollover. So I ditched this too. However I kind of like this javascript one still, its's almost more fun and means there is not code dependency. I might end up switching back to this. Let me know what you think.

#### Experiments

Here are some of the experiments I ran, let me know if you like any of these better than what is on [burrito.place](https://burrito.place)

* **[Final Product](https://burrito.place)** (using [tsParticles](https://github.com/matteobruni/tsparticles))
* **[Background Repeat CSS Experiment](css_repeat.html)** (based on: <https://codepen.io/saransh/pen/BKJun> & <https://css-tricks.com/parallax-background-css3/>)
* **[Manually Animated CSS](manual_css.html)** (based on: <https://github.com/AdamXweb/FlyinEmoji/>)
* **[Naive Javascript](naive_js.html)** (customized code based on: <https://codepen.io/robertheiser/pen/NXrqXa>)

##### tsParticle Config
```
 {                                                                                                                      
  fpsLimit: 60,                                                                                                                                        
  detectRetina: true,                                                                                                                                  
  particles: {                                                                                                                                         
    move: {                                                                                                                                            
      enable: true                                                                                                                                     
    },                                                                                                                                                 
    number: {                                                                                                                                          
      value: 100                                                                                                                                       
    },                                                                                                                                                 
    size: {                                                                                                                                            
      random: {                                                                                                                                        
        enable: true,                                                                                                                                  
        minimumValue: 10                                                                                                                               
      },                                                                                                                                               
      value: 30                                                                                                                                        
    },                                                                                                                                                 
    shape: {                                                                                                                                           
      options: {                                                                                                                                       
        images: [{                                                                                                                                     
          src: 'https://api.iconify.design/twemoji:burrito.svg',                                                                                       
          width: 100,                                                                                                                                  
          height: 100                                                                                                                                  
        },                                                                                                                                             
        {                                                                                                                                              
          src: 'https://api.iconify.design/twemoji:taco.svg',                                                                                          
          width: 100,                                                                                                                                  
          height: 100                                                                                                                                  
        }                                                                                                                                              
        ]                                                                                                                                              
      },                                                                                                                                               
      type: "image"                                                                                                                                    
    }                                                                                                                                                  
  }                                                                                                                                                    
}
```

## Other

### How to get daily notes onto a webserver without thinking

* Attempted to use SSHFS + FUSE to Mount Remote Filesystem on MacOS
	* Quickly ran into some kernel issues on Big Sur. I think I need to update my Mac and dig deeper.

I did more thinking on this and for now I am shelving the idea. Instead I will just use git and GitHub Actions. However this seems super overkill. But I think it should work okay. 


## Tomorrow

* Go for Miramar Lake ride
* Migrate AWS server to new cheaper server
	* Ensure stream and utils still work fine until I transition that to DB
* Set up GitHub Action to ping my server to update
* Read *United States v. Virginia* in hammock
* Write scripts to import financial information into DB
	* Would like to have all accounts being scraped by the end of the day
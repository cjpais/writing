# Impact of Apple's M1 on the Semiconductor Industry

Apple's M1 Changes Everything
  * This title then begs the question, what is the state of the industry now (before M1)
  * What is the state after the M1. What has been shaken up
Gamechanger

Title's in the form of questions?

transformative change?

Apple has shifted the balance of power with the release of the M1 powered Macs.
Apple by releasing these M1 Macs is just begging for a response from the rest of the industry.


analyze the consumer space and the server space

Will be focusing just on how Apple's decision to release ARM based Mac's will force the rest 
of the industry to respond. I will not be digging into why Apple would move to ARM. 
That discussion will be saved for a future article.

Apple's release of ARM powered Mac's is flipping the industry on it's head. The 
sheer amount of press around this release is quite telling. [The buzz on Twitter,
HN, has been continuous](https://www.singhkays.com/blog/apple-silicon-m1-black-magic/). 

At this point we know they are ***fast*** with incredible battery life to boot. 

These are fantastic things and these two factors will be the driving force for huge 
change in the industry. Consumer space and corporate space alike.

Did Apple force the industry's hand to transition to ARM?

## Heterogeneous compute
https://erik-engheim.medium.com/why-is-apples-m1-chip-so-fast-3262b158cba2
  excellently written and want something similar to this, but maybe more opinion. 
  opinion rooted in fact. or rather just opening up the room for discussion

  probably want some pictures or something instead of pure text otherwise peoples brains will
  probably turn off or something since people arent good at having attention span (neither am i)

Nvidia can compete

## Consumer Side

For the consumer side of things I think it's quite simple. 
[People are *stoked*](https://www.singhkays.com/blog/apple-silicon-m1-black-magic/#battery-life-is-insane) 
to have a laptop that can last multiple days on battery.

This alone seems like it will drive the rest of the consumer market to follow Apple.

Given that other Windows laptops with ARM CPU's have been released, why is it only
now that it's a big deal? The Surface Pro X has great battery life too

  * apparently it serves a "small group of people" which Apple's laptops definitely do not
  * apple serves everyone, people dont have much choice once their lineup goes all arm
    * which it certainly will

I feel like this is something like Apple dropping the headphone jack. At first
the whole industry and consumers are bewildered by the move. Then sure enough
the rest of the smartphone industry follows Apple and drops the headphone
jack. Apple proved to the rest of the industry that you could remove the headphone
jack, provide a better user experience, and ultimately make more money off consumers.


How do Microsoft, Intel, AMD, Qualcomm, NVidia respond to such a performant chip in 
a $700 package?

## Will ARM completely take over the industry?

This seems unlikely in the near term. There is such a massive amount of code running on x86
machines that probably won't be deprecated for a long time. 

There may be a transition in ISA in the consumer space for sure, but the server space is a
much much longer game to play. 

ARM based 

What if Microsoft doesn't respond? 

It seems to me this is quite unlikely. 


Microsoft has been working with Qualcomm for years to have Windows on ARM. Laptops
like the Surface Pro X have been released, but haven't gained anywhere near the
traction that the M1 powered Mac's have. 

One of the problems with the Surface Pro X is the price. Who is going to pay $1500
for a laptop that might not run your apps and has no cult following? 

Within a very short period of time it's become clear that Apple is able to get extraordinary performance
and battery life out of these new M1 powered Mac's. To have a laptop that can last 2/3 of a day 
is mindboggling today, but soon enough this will be seen as abysmal battery life. 

## Server Side

It's strange to talk about servers and Apple in the same sentence. It seems very very unlikely that
Apple will jump back into the server space. However, we are not talking about Apple in the server
space. We are talking about how Apple's impact on the consumer space will drive the server space
to change.

The driving force behind change in the server world will be dominated by change in the consumer space.
[As Linus Torvalds recognizes](https://www.realworldtech.com/forum/?threadid=183440&curpostid=183486),
 people don't want to develop at home on x86 and then deploy on ARM.
It doesn't make any sense. With Apple moving towards ARM, it only makes sense that some of the server
market will start moving towards ARM as well. Especially as more and more developers move their
home systems to something ARM based. 

[MacOS computers represent approximately 27.5% of the machines developers use](https://insights.stackoverflow.com/survey/2020#technology-developers-primary-operating-systems). 
This is a significant
number. This large number will motivate people to cross compile their software if they weren't already.




## How does the industry respond?

What will happen if this is the case? How do Intel and AMD respond. Where does this leave other semiconductor manufactures, notably Nvidia and Qualcomm?

If you can accept the assumptions made about the spaces, now we can go ahead and analyze some
of the main players in the semiconductor industry who will be directly affected by the
release of the M1 Macs in the next couple of years.

To refresh what we've learned since the release is this.

## Quantifying 

Unfortunately this chart does a pretty terrible job of
telling really what is going on. 

| CPU | TDP | Measured Power (at adapter) |
|---|---|---|
| Apple M1 | ~22W[^m1_anand_power] | 27.2W[^m1_nbcheck_power] |
| AMD Ryzen 4800U | 15W (configurable to 25W)[^4800u_amd_power] | 49.5W[^4800u_nbcheck_power] |
| AMD Ryzen 4900HS | 35W[^4900hs_amd_power] | 105W [^4900hs_nbcheck_power][^4900hs_test_gpu] |
| Intel 1065G7 | 15W (configurable to 25W)[^1065g7_intel_power] | 35W[^1065g7_nbcheck_power] |

| CPU	| TDP	| Max Power | Raw ST PERF | ST Perf/Watt	| Raw MT Perf |	MT Perf/Watt |
|---|---|---|---|---|---|---|
| Apple M1 | ~22W	| 31W | 28.85 | 0.9306451613 |	38.71 |	1.248709677 |
| AMD Ryzen 4800U	| 15W | 34.39W |	25.14 |	0.7310264612 | 28.25 | 0.8214597267 |
| Intel 1185G7 | 28W | 51.92W | 21.52 | 0.4144838213	| 25.87 |	0.4982665639 |
| AMD Ryzen 5800X |	105W | 140.1W | 47.89 | 0.3418272662	| 52.1 | 0.3718772305 |
| Intel 10900K | 125W	| 251.6W	| 47.35	| 0.1881955485 | 48.59 | 0.1931240064 |

### Singlethreaded performance equaling desktop CPU's.



Power Usage:
* Jury is still out (will wait for notebookcheck.net)]
  * Good comparison point https://www.notebookcheck.net/The-Ryzen-7-4800U-is-an-Absolute-Monster-Lenovo-Yoga-Slim-7-14-Laptop-Review.456068.0.html
* Uses half the power of the 4800U which is 15W TDP (default, configurable to 25)
  * https://www.notebookcheck.net/AMD-Ryzen-7-4800U-Laptop-Processor-Benchmarks-and-Specs.449937.0.html (49.5W)
  * https://www.notebookcheck.net/Apple-M1-Processor-Benchmarks-and-Specs.503613.0.html (27.2W)
  * Getting 36% better battery life, with 49.9Wh vs 61Wh
    * Lenovo has 22% larger battery, so it appears this approximates the raw power consumption seen.
* Uses a quarter of the power of a Ryzen 4900HS (35W TDP, 105W Measured)
* GPU consuming about 10 Watts when fully loaded
  * https://www.anandtech.com/show/16252/mac-mini-apple-m1-tested/3

My guess is the M1 powered laptops really come into a class of their own when you are 
doing intense tasks on the battery. There have been some benchmarks that seem to validate
this. The combination of power efficiency and speed means a lot more can be done on the
laptop.

CPU Speed:
* Single-Threaded
* Multi-Threaded

GPU:
* GPU in MBA competes with discrete GPUs
  * Radeon Pro 560X, Nvidia MX350
  * https://www.notebookcheck.net/Apple-MacBook-Air-2020-M1-Benchmarks-Should-you-get-7-or-8-GPU-cores.506105.0.html
  * 

* Power comparison
  * Power compared to package power
    * The fact that Apple is able to achieve this in a total device power consumption of 5W including the SoC, DRAM, and regulators, versus +21W (1185G7) and 49W (5950X) package power figures, without DRAM or regulation, is absolutely mind-blowing.
      * https://www.anandtech.com/show/16226/apple-silicon-m1-a14-deep-dive/4
* Performance comparison
  * Single threaded performance rivals desktop CPU's. Mind blowing.
    * https://www.anandtech.com/show/16226/apple-silicon-m1-a14-deep-dive/4
  * 

## Why has ARM been struggling in the server space and how apple is going to change this

Well in the server space there seems to be little incentive to swap over to ARM especially
given the huge hassle of changing ISA's. Clearly this is not simple and that's why Apple
has spent so much time to provide tools to get people swapped over cleanly.

That is the beauty of what they've done. According to the stackoverflow developer survey, about 27.5%
of developers use Apple systems. As we see a huge developer population move to ARM based Mac's
surely the tooling will have to support ARM very well. 

This is massive and will force a rethink of the server space. Even Linus didn't believe this was 
going to happen anytime soon

> Some people think that "the cloud" means that the instruction set doesn't matter. Develop at home, deploy in the cloud.
> 
>That's bullshit. If you develop on x86, then you're going to want to deploy on x86, because you'll be able to run what you test "at home" (and by "at home" I don't mean literally in your home, but in your work environment).
>
> Which means that you'll happily pay a bit more for x86 cloud hosting, simply because it matches what you can test on your own local setup, and the errors you get will translate better.
>
>
>Which in turn means that cloud providers will end up making more money from their x86 side, which means that they'll prioritize it, and any ARM offerings will be secondary and probably relegated to the mindless dregs (maybe front-end, maybe just static html, that kind of stuff).
>
>Guys, do you really not understand why x86 took over the server market?
>
>It wasn't just all price. It was literally this "develop at home" issue. Thousands of small companies ended up having random small internal workloads where it was easy to just get a random whitebox PC and run some silly small thing on it yourself. Then as the workload expanded, it became a "real server". And then once that thing expanded, suddenly it made a whole lot of sense to let somebody else manage the hardware and hosting, and the cloud took over.


https://www.realworldtech.com/forum/?threadid=183440&curpostid=183486

ARM is already crushing x86 in the server space, but is probably highly underutilized.
https://www.anandtech.com/show/15578/cloud-clash-amazon-graviton2-arm-against-intel-and-amd/9

I would guess that Amazon is making boatloads on these CPU's when compared to their
Intel and AMD counterparts, due to the lower power consumption.

Thinking about the future of the server space it seems quite clear the benefits of moving to ARM.
Some of the biggest problems in the server space are power and cooling. Given the constraints
that ARM CPU's have traditionally been in, they can fill this niche quite well. 

It will take some time to see how much less power A

From the perspective of someone operating a datacenter, why would you not want to move to ARM
if the software support is there and the customers are too? As a benefit you can squeeze over
2x the compute in the same area while keeping the same thermal and power envelope.

Apple has shown
the performance of an ARM based CPU can compete with the big boys in desktop environments. 

## My Interpretation in Context of the Questions


Opposition:

* Begs the question, why do servers not currently use low power CPU's?
  * What do the workloads look like?
  * How can we compare an m1 webserver?
* How can the m1 compete with desktop CPU's then get crushed by laptop CPU's?
* ARM compatibility on Linux? How good is it and will Apple's transition actually help here?

Why the industry might want to move to ARM anyway. Or why there might be a push.


## LOTS OF COMPETITION IN THE SEMICONDUCTOR INDUSTRY

Hard to say who will do well and who wont, but here's my predictions

## AMD

Looks like AMD still has a winner on its hands with the Zen3 arch. Very efficient 
and very fast. Doesn't look like they are going to go away any time soon unless
they falter on their next microarchs.

The good think for AMD is it looks like they can compete with Apple in terms of 
performance per watt, or at least be relatively close to the benchmark set by
Apple. However this is very short term thinking. I imagine the progression of
ARM based microarchitectures are going to improve much more rapidly in terms
of performance per watt. However this is based on pure speculation rather than facts
or information.

They have put some ARM based CPU's into the market according to:
https://www.anandtech.com/show/15575/amperes-altra-80-core-n1-soc-for-hyperscalers-against-rome-and-xeon
Opteron A1100 series in 2017.

This clearly was not a big success

Recently purchased Xilinx. I am not quite sure what to think about this now.

"Intel has stagnated itself out of the market, and has lost a major customer today. AMD has shown lots of progress lately, however it’ll be incredibly hard to catch up to Apple’s power efficiency. If Apple’s performance trajectory continues at this pace, the x86 performance crown might never be regained."

## Intel

At this moment Intel is in a tough spot. AMD has been starting to dominate Intel in the CPU
space and seems to extending their lead with the Zen 3 microarchitecture. Beyond this
they have been struggling to shrink their process nodes. Now they have lost Apple
as a customer, and at the same time Apple is putting pressure on Intel and the entirety of the
x86 space by threatening the server market.

Of course Intel is an interesting company that does a massive amount of R&D which cannot be discounted.


## Qualcomm

From QC perspective there is a huge opportunity with Apple moving to ARM.
People see the performance and battery life they can get from a MBA. 
Beyond this Qualcomm has the value add of being able to add a modem
for always connected PC's. It is very dependent if people even want this
in the first place. The cost of 4G/5G service is much more $/GB, however
you don't ever have to worry about wifi. I use my phone without worries
much of these days and would be very nice to do the same for my computer.

Has a ways to catch up with Apple
https://www.anandtech.com/show/16226/apple-silicon-m1-a14-deep-dive/3

![](https://images.anandtech.com/doci/16226/spec2006_A14.png)


Looking at this picture we can clearly see that with the same amount of energy
used (Joules) Apple nearly doubles Qualcomm's performance.

![](https://images.anandtech.com/graphs/graph16226/119329.png)

Apple has clearly been playing a different game than Qualcomm. A
response is very warranted. Could not be so good for QC.

## Nvidia

Nvidia is in the most interesting spot out of all the major semiconductor
manufacturers. They are already breaking into the server space with their GPU's.
They trying to purchase ARM Holdings. They have also been making ARM based CPU's
for some time with their Tegra line (however they have not seen much consumer success).

AI Accelerators. NVLink. Highly integrated SOC

NVLink with the CPU????

Jensen-Huang has specifically mentioned the like.
https://www.tomshardware.com/news/jensen-huang-hints-at-nvidia-branded-arm-cpus

Remember NVidia is not new to building ARM processors. They have been doing so since
the original Tegra APX 2500 in 2008. They have not been the most high profile SOC's
out there (given the mobile space is mostly dominated by Qualcomm/Samsung/Huawei).
However the Nintendo Switch runs based on a Tegra X1 SOC.

It's possible for Nvidia to come up with an extremely powerful and low power solution
that could compete with Apple in a huge way. They have the GPU/TPU prowess and
with bringing ARM on board could really be a force to be reckoned with in the consumer
and server space.

The consumer space could benefit immensely from a deeply integrated CPU/GPU/GPGPU combo, leading
to incredible performance and very low power. This could be perfect for the next generation
of gaming laptops, or perhaps even better VR headsets or other AR devices.

One big stumbling block potential for NVidia is if they continue to remain very 
proprietary with their drivers and software. Most of the server industry runs on 
Linux, so deep support in Linux would be ideal for them.

The best case scenario for Nvidia is to completely dominate the server and consumer
space with their own CPU/GPU/AI Accelerator combos.

## Amazon

Amazon is ahead of the game. They have had ARM based EC2 instances for some time.
Beyond that [it's been proven they offer massive amounts of compute per $](https://www.anandtech.com/show/15578/cloud-clash-amazon-graviton2-arm-against-intel-and-amd/9).

I'd imagine that Amazon is making money hand over fist 

It will take a while for the rest of the industry to catch up, but as more and more
developers start building docker images for ARM, I suspect more and more ARM servers
will be desired. 

## Samsung and TSMC?


## New Players

* [Ampere](https://en.wikipedia.org/wiki/Ampere_Computing)
  * Nvidia is partnering with them as well. GPU-accelerated ARM servers partnership too......
* Nuvia
* Marvell?

## INTERCONNECTS?????!!!

You would imagine companies like Mellanox and Infiband could stand to do extremely well here.
If programs increasingly are becoming multithreaded and there are more CPU's/Servers, you will
need increasingly high performance interconnects. Anyhow this industry is not even close to going
away any time soon. This is just another small boost to them. I don't know enough about the specifics
to really get into more detail. 

## What about RISC-V??

## CPU's used by AWS

* C4 - E5-2666 (v3 and v4)
* C5n - Intel Platinum (3ghz)
* C5a - AMD EPYC 7002
* C5
  * Custom based on Cascade Lake
  * Xeon Platinum 8000
* M5
  * Platinum 8175M

LOL HOLY SHIT DIDNT THINK ABOUT THIS: "This might be one reason why Apples does so well in browser benchmarks (JavaScript numbers are floating-point doubles)." - https://www.anandtech.com/show/16226/apple-silicon-m1-a14-deep-dive/2 


[^m1_nbcheck_power]: https://www.notebookcheck.net/Apple-M1-Processor-Benchmarks-and-Specs.503613.0.html
[^m1_anand_power]: https://www.anandtech.com/show/16252/mac-mini-apple-m1-tested
[^4800u_amd_power]: https://www.amd.com/en/products/apu/amd-ryzen-7-4800u
[^4900hs_amd_power]: https://www.amd.com/en/products/apu/amd-ryzen-9-4900hs 
[^4800u_nbcheck_power]: https://www.notebookcheck.net/AMD-Ryzen-7-4800U-Laptop-Processor-Benchmarks-and-Specs.449937.0.html
[^4900hs_nbcheck_power]: https://www.notebookcheck.net/AMD-Ryzen-9-4900HS-Processor-Benchmarks-and-Specs.454860.0.html
[^4900hs_test_gpu]: Power was measured at the wall adapter as far as I can tell including the GPU (RTX 2060) which would increase overall power consumption
[^1065g7_nbcheck_power]: https://www.notebookcheck.net/Intel-Core-i7-1065G7-Laptop-Processor-Ice-Lake.423851.0.html
[^1065g7_intel_power]: https://ark.intel.com/content/www/us/en/ark/products/196597/intel-core-i7-1065g7-processor-8m-cache-up-to-3-90-ghz.html
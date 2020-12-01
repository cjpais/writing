# Impact of Apple's M1 on the Semiconductor Industry

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

## Consumer Side

For the consumer side of things I think it's quite simple. 
[People are *stoked*](https://www.singhkays.com/blog/apple-silicon-m1-black-magic/#battery-life-is-insane) 
to have a laptop that can last the whole day on battery and more.

This alone seems like it will drive the rest of the consumer market to follow Apple.


Given that other Windows laptops with ARM CPU's have been released, why is it only
now that it's a big deal?

I feel like this is something like Apple dropping the headphone jack. At first
the whole industry and consumers are bewildered by the move. Then sure enough
the rest of the smartphone industry follows Apple and drops the headphone
jack. Apple proved to the rest of the industry that you could remove the headphone
jack, provide a better user experience, and ultimately make more money off consumers.

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
* Performance comparison

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

They have put some ARM based CPU's into the market according to:
https://www.anandtech.com/show/15575/amperes-altra-80-core-n1-soc-for-hyperscalers-against-rome-and-xeon

## Intel

Intel. Intel has some work to do.

## Qualcomm

From QC perspective there is a huge opportunity with Apple moving to ARM.
People see the performance and battery life they can get from a MBA. 
Beyond this Qualcomm has the value add of being able to add a modem
for always connected PC's. It is very dependent if people even want this
in the first place. The cost of 4G/5G service is much more $/GB, however
you don't ever have to worry about wifi. I use my phone without worries
much of these days and would be very nice to do the same for my computer.

## Nvidia

Nvidia I think has the most interesting spot out of all the major semiconductor
manufacturers. They are already breaking into the server space with their GPU's.
They also recently purchased ARM Holdings and have been making ARM based CPU's
for some time with their Tegra line (however they have not seen much consumer success).
This potentially leaves Nvidia in a very nice position to bene

NVLink with the CPU????

## Amazon

We have started to see the shift already and Amazon is on top of it. They have 

It will take a while for the rest of the industry to catch up, but as more and more
developers start building docker images for ARM, I suspect more and more ARM servers
will be desired. 


## New Players

* [Ampere](https://en.wikipedia.org/wiki/Ampere_Computing)
  * Nvidia is partnering with them as well. GPU-accelerated ARM servers partnership too......
* Nuvia

## INTERCONNECTS?????!!!

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


[^m1_nbcheck_power]: https://www.notebookcheck.net/Apple-M1-Processor-Benchmarks-and-Specs.503613.0.html
[^m1_anand_power]: https://www.anandtech.com/show/16252/mac-mini-apple-m1-tested
[^4800u_amd_power]: https://www.amd.com/en/products/apu/amd-ryzen-7-4800u
[^4900hs_amd_power]: https://www.amd.com/en/products/apu/amd-ryzen-9-4900hs 
[^4800u_nbcheck_power]: https://www.notebookcheck.net/AMD-Ryzen-7-4800U-Laptop-Processor-Benchmarks-and-Specs.449937.0.html
[^4900hs_nbcheck_power]: https://www.notebookcheck.net/AMD-Ryzen-9-4900HS-Processor-Benchmarks-and-Specs.454860.0.html
[^4900hs_test_gpu]: Power was measured at the wall adapter as far as I can tell including the GPU (RTX 2060) which would increase overall power consumption
[^1065g7_nbcheck_power]: https://www.notebookcheck.net/Intel-Core-i7-1065G7-Laptop-Processor-Ice-Lake.423851.0.html
[^1065g7_intel_power]: https://ark.intel.com/content/www/us/en/ark/products/196597/intel-core-i7-1065g7-processor-8m-cache-up-to-3-90-ghz.html
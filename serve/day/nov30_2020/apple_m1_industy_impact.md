# Apple's M1 Impact on the Semiconductor Industry

Apple has shifted the balance of power with the release of the M1 powered Macs.

The name of the game in the CPU space has been performance per watt
for many years now. And Apple just changed the equation.



## The fall of x86?

Will Apple's transition to ARM force the hand on the rest of the industry to do the same?
What will happen if this is the case? How do Intel and AMD respond. Where does this leave other semiconductor manufactures, notably Nvidia and Qualcomm?

Apple's release of ARM powered Mac's is flipping the industry on it's head. The 
sheer amount of press around this release is quite telling. [The buzz on Twitter,
HN, has been continuous](https://www.singhkays.com/blog/apple-silicon-m1-black-magic/). 

At this point we know they are ***fast*** with incredible battery life to boot. 

These are fantastic things and these two factors will be the driving force for huge 
change in the industry. Consumer space and corporate space alike.

To refresh what we've learned since the release is this.

## What has Apple done?

Apple is delivering exceptional performance at a third of the power of their competitors. 

## Why others will follow

Given history (iPhone, iPad, Airpods, Removing Headphone Jack) 
it seems like a given to assume the rest of the industry will 
follow Apple in incorporating ARM processors in their .

##

## Quantifying 

Unfortunately this chart does a pretty terrible job of
telling really what is going on. 

| CPU | TDP | Measured Power (at adapter) |
|---|---|---|
| Apple M1 | ~22W[^m1_anand_power] | 27.2W[^m1_nbcheck_power] |
| AMD Ryzen 4800U | 15W (configurable to 25W)[^4800u_amd_power] | 49.5W[^4800u_nbcheck_power] |
| AMD Ryzen 4900HS | 35W[^4900hs_amd_power] | 105W [^4900hs_nbcheck_power][^4900hs_test_gpu] |
| Intel 1065G7 | 15W | 35W[^1065g7_nbcheck_power] |

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
laptio.

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

3x density.

ARM is already crushing in the server space, but is probably highly underutilized.
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
[^1065G7_nbcheck_power]: https://www.notebookcheck.net/Intel-Core-i7-1065G7-Laptop-Processor-Ice-Lake.423851.0.html
[^9]:
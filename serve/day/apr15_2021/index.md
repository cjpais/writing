# Thursday, April 15, 2021

![my view for the day](sick-setup.jpeg)

One thing I just noticed. I've had ideas and let
them go by without doing anything about them.
Well in particular GitCoin, I think this
is something I'd been talking about for years
when I first learned of Ethereum. However I had
it in the context of a much larger system. 
Maybe this is something to think about. 
Don't need to think about the whole system
all of the time. Sometimes you can take a piece
and execute directly on that. Maybe this is less
elegant (and I think it is) but ultimately the 
results can be achieved. Is that such a bad
thing? I think not. So then I think the question
is for me. What is my most specific idea? 
Probably the LTE network. If possible to deploy
it really could be a boon. Maybe I really should
look into doing it at small scale and see what 
can be done. Regardless of the why. I think
it gives individuals more power and I think
that is good. 

Anyhow. Read a couple of papers this morning.

* [zkSnarks in a Nutshell](http://chriseth.github.io/notes/articles/zksnarks/zksnarks.pdf)
* [A Flexible Design for Funding Public Goods (Quadratic Funding)](https://arxiv.org/pdf/1809.06421.pdf)

# zksnarks

So I am struggling to fully understand this.
I have the mathematical background to understand
but I think I will need to dive in deep with a
real world example to actually understand.
All the theory in the world is nice, but I
need a practical example. I think some
things can be assumed. For example Homomorphic
encryption. This can easily be explained and
assumed since we know it works.

I think generally the idea is sound, but I
don't fully understand what the proof
is actually useful for. Why do I want to 
prove that a computation is valid? Beyond
this, what does this statement even mean?
That is was computed correctly? So I don't
need to know what it was, but know it was
valid? Hmmm...

# Quadratic Funding

This is an idea which I think is interesting.
Especially when using the [calculator
on the website](https://wtfisqf.com). Basically
it distributes money based more on the number
of people contributing rather than the amount
of money each individual contributes. 

It has two pretty intense assumptions if you 
ask me.

1. That every individual is recognizable in the system
2. Resources between individuals are equitably distributed

Both of these assumptions seem to be super key.
If you don't have 1, then you can easily spoof
the entire system. Just create a ton of accounts
which contribute a small amount, and you get a
much larger amount. Basically 1 implies some
universal identity system. This is controversial
in and of itself. Something I am curious about
but realize the flaws.

Regarding 2, it is spoken about in the context 
of what QF is trying to achieve. That it wants
to maximize "dollar equivalent value". I think
of this as providing the most value to
individuals given the input. However this could
be an inaccurate summary. It is my intuition.
So basically if you don't have an equitable
distribution to begin with, then the results
that you might get are going to be inequitable.
Garbage in Garbage out. Guess this is nothing
new, but points out this is a problem to be
solved. What are the ways we can reduce this gap?

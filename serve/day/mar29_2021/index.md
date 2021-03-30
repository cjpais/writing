# Monday, March 29, 2021

So far an interesting day. Tried to get some surfboard shaping space at 
Maketory. Will have to see if this works out, there is a shipping container
that could be a good space perhaps for even two people. Will have to see. 
Hopefully the price is good.

On another note, started working with GWR (Geographically Weighted Regression)
to analyze expected AirBnB prices in Berlin. This eventually will be targeted
for estimating rent prices across San Diego. However I will say it seems like
the expected price as outputted by the regression is quite off. 

From what I can tell it is giving almost all weight to the geographically
close neighbors, but not taking into account the other important features.
I am not quite sure how to correct for this yet. This is something I would
like to discuss with Kevin and see if he has any insight that I do not. I 
am also curious if I can naively do some kind of ensemble technique and see
if that helps or not. 

I have a feeling I will have to spend a lot more time with the data to get
something meaningful out of it. I was hoping the machine learning techniques
would reduce the search space dramatically. I think that it should, but I 
don't have the right insight into the problem or the space yet to really
grasp.

I am thinking about taking a break from this problem and instead moving
to finish up the Elixir challenges on 1729.com. At the worst I learn 
more about Elixir and the best case I also win $100 of BTC.

Hmmm okay.

Well Elixir is proving to be more challenging than expected. 
Doing the Diffe-Hellman key exchange was trivial once I understood
the syntax for dealing with `Binaries`.

Basically a `Binary` is something in the format `<<>>`. Every element
within the braces will be a uint8. So you might get `<<124, 213, 20, 42>>`.
This would be a `Binary` containing 4 bytes. 

Suppose I wanted to interpret this as two uint16's. I can do the following.
```
iex(1)> <<i1::integer-unsigned-size(16), i2::integer-unsigned-size(16)>> = <<124, 213, 20, 42>>
<<124, 213, 20, 42>>

iex(2)> i1
31957

iex(3)> i2
5162
```

Similarly I could interpret this as an int32

```
iex(4)> <<i1::integer-size(32)>> = <<124, 213, 20, 42>>
<<124, 213, 20, 42>>

iex(5)> i1
2094339114
```

Dealing with multiprocessing is much more challenging for me. I am not quite
caught up with all the techniques in general. Plus I am still relatively
unfamiliar with the syntax which is making it even more challenging.
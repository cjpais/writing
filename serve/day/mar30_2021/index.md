# Tuesday, March 30, 2021

Day started out a little slow, but quickly ramped up for me. Waking up this
morning was a bit challenging. Slept in an extra 30 min.

Got tea/smoothie/coffee with Kristen and Dave. Some great convo this morning,
will probably be writing more about it on [buzzard.life](https://buzzard.life)

Also went back to Fink's house to work on the surfboard more. Was good to catch
up with him. I worked mostly on getting the surface of the board ready for hot
coating. Using solarez to patch what I needed before doing the final coat.
I am still unsure if the board is going to be watertight. The fin boxes
are pretty trash on the board and not sure how I am going to fix them 
at this point (without spending a lot of time). I think it's possible to
continue to patch them with solarez, but I am not sure if it will be worth
it or not.

When I got home I wanted to finish up the Elixir stuff left off from last night.
Was really struggling with concurrency. Mostly because I wasn't sure how to map
my mental model of what I wanted to achieve into Elixir. When searching more about
concurrency, I quickly found the Exercism blog post with the solution. However I 
didn't like the model they chose to work with. They merged all the texts into 
one list then got the characters and split them into working groups.

This is fine and definitely works. But for some reason this method feels like 
cheating to me. I definitely did not want to use this method. I wanted to 
concurrently process each text individually. I feel that this makes more 
intuitive sense when reading the problem statement. Perhaps it is not
the most efficient, but as a newbie, both to concurrency and Elixir
it seemed the most obvious way to go. 

To go this way initially I wanted a worker pool. This would try to ensure
that workers were being used to capacity. I think in the solution above 
due to how they used `ceil` there could be an under-utilization of workers.
Sometimes with workers not even being assigned. That also didn't seem to fit
the problem statement very well.

I tried to build my own pool but that was too heavy of a solution. The good
thing about the blog post was it mentioned `Task.async_stream`. This was
a great fit for the solution I was looking for still. However I still needed
to limit the workers. Fortunately it has `:maximum_concurrency` as an option.
That made it rather easy to make sure I had the correct number of workers
(and hopefully maximally utilize them). I am not sure the underlying scheduling
algorithm, but assume it to be more optimal than the blog solution.

With this figured out it was mainly a challenge to use `Enum.reduce` to actually
merge the maps being returned asynchronously. After lots of documentation reading
and experimenting in `iex` I had a better grasp of what was going on. 

Pattern matching is still somewhat unintuitive for me. I am not quite sure when
to use it when programming in Elixir, however I think I would need to use the 
language more to really take advantage of it.

Overall a better learning day than yesterday. Really just needed something of
a break and food in my system to work effectively. Turns out doing 10 hour
stints is not always sustainable when you are learning about something new.

Anyway, maybe at some point I will write that pooling mechanism I would want.

Looking forward to tomorrow. Cheers
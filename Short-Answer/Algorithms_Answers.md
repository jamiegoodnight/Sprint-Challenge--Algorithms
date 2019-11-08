#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

<!-- Initial commit -->

## Exercise I

a) Feels straightforward (???), but as the triple question marks indicate, I'm not very smart so maybe I'm being tricked!

But I'm inclined to say if we're looping n times—n is unknown and dynamic and it's linear time—the complexity is o(n).

b) Nested loops imply an EXPONENTIAL increase in complexity, so I'm thinking n(n^2) time complexity here.

c) Similar to a, except instead of our integer being n, it's bunnies! Therefore, o(n).

## Exercise II

I'm thinking we could try solving this a couple different ways. It really depends on other information the question doesn't give us.

We might try something like adding all floors to a list and looping over the list,checking to see if egg_break==true for that floor. When we find the first floor where egg_break is true, we return that floor—the floor where the egg "doesn't get broken if dropped off a floor less than" that. This would be o(n) time. We could also try a binary search (o(log n)) by splitting n and checking if an egg breaks in one half of n or the other and so on.

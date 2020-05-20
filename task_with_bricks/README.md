# task-with-bricks

We want to make a row of bricks that is exactly n inches long. We have a small bricks (1 inch each) and b big ones (5 inches each).
Return true if it is possible to build the row by choosing from the given bricks, false otherwise.
Code Limit
Less than 38 characters.
Example
For a = 3, b = 1 and n = 8, the answer is true.
It's possible to take 1 big brick and 3 small ones.
For a = 3, b = 1 and n = 9, the answer is false.
There're not enough bricks to create a row of length 9.
For a = 2, b = 3 and n = 9, the answer is false.
There's no way to make a row of length 9.
makeBricks=(a,b,n)=>

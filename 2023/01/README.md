# Day 01

First ever program written in Go.  
It's certainly less convenient than python for iterating over an array, retrieving the last item in an array, etc.

Interesting how the convention is for errors to be passed as the last item in a tuple and you are expected to do something with it, or you can choose to explicitly, immediately return `nil, error` to "raise" the exception higher.

Also interesting is the requirement to declaring a variable - either as a singular variable declaration, or as a compound declaration/assignment using the walrus operator `:=`.


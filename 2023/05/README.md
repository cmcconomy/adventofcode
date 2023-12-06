# Day 05

Again this was a confusing problem.
I ran into a new issue - discovering that in Golang, when I thought I was generating a new pointer like so:

``` go
var val []int

for {
    val = []int{}
    ptr = &val
}
```

In fact the pointer remained the same at all times.  
You actually have to use `:=` to generate a new object and thus a new pointer. Nice to know!

Anyhow.. got part 1 going; part 2 takes far too long to approach naively like I tried.
I would have to rewrite the logic to pay attention to ranges as a shortcut instead of exhaustively running each value... which I don't want to do right now.

So this is pending part 2.
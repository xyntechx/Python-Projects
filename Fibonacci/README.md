# Fibonacci
I wrote `fibonacci.py` because I was once again plagued with boredom and in need of some vanilla Python coding. Having said that, `fibonacci.py` currently contains 3 functions: `build_fib_recursive(n)`, `build_fib_iterative(n)`, and `find_index(n)`.

## 📚 Building the Fibonacci Sequence Recursively
To do so, call the `build_fib_recursive(n)` function, where `n` is the number of elements in the sequence. The function thus utilises recursion to return a Fibonacci sequence of n elements.

> Note: Technically, for the Fibonacci sequence to be valid, n >= 2. However, for the purposes of this function, n can take all positive integers.

## 🔁 Building the Fibonacci Sequence Iteratively
To do so, call the `build_fib_iterative(n)` function, where `n` is the number of elements in the sequence. The function thus utilises iteration to return a Fibonacci sequence of n elements. As a side note, `build_fib_iterative(n)` is more time-efficient than `build_fib_recursive(n)`.

> See Note in **Building the Fibonacci Sequence Recursively**

## 🔎 Finding the Index of an Element in the Fibonacci Sequence
To do so, call the `find_index(n)` function, where `n` is the integer whose index in the Fibonacci sequence is to be found. The function will return the index of `n` (0-indexed) in the Fibonacci sequence. Do note that `n` may or may not be in the sequence and thus the function will return a 404 message in this case.

> `find_index(n)` does not integrate `build_fib_recursive(n)` nor `build_fib_iterative(n)`, but it can easily do so with some minor tweaks!

## 👋 Parting Words
Hopefully, you have enjoyed looking at and studying `fibonacci.py`! It was a great change of pace for me coding this as I, at the time of writing this, have been investing a lot of my time doing Web Development and Computer Vision models. Frankly, `fibonacci.py` contains quite a short (and simple) program, but I love it nonetheless. All in all, happy coding!
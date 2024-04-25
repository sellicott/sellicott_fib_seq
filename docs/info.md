<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

The project takes in the index of Fibonacci number to generate (`n=0` -> 1, `n=1` -> 1,...).
Where `n` is an 8-bit unsigned integer on the `n[7:0]` pins. To start generating the sequence `start_stb` should be asserted for one clock cycle.
While the module is working, the `busy` signal will be asserted. After the `busy` signal falls to `0`, the Nth Fibonacci number is available on `fib[7:0]` pins

![gds_render](gds_render.png)
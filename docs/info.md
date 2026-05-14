<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works
An 8-bit up counter increments its value by 1 on every clock pulse and resets to 0 when rst_n is low.
## How to test
Apply clock pulses, keep ena high, release reset (rst_n = 1), and observe the count on uo_out[7:0].
## External hardware
No external hardware required.

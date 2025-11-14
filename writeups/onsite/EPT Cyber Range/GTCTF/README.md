# EPT Cyber Range
**Authors:** tmolberg and nordbo

## Challenge
Once again the dreaded EPT Cyber Range had returned for it's third year. And third times the charm right?? right?!?

note: I did not solve the challange (get 3 rounds) but I got 2, and was so close..

### Challange Description
```
We're back for a third year! This time it's all about bitwise operations. You get the flag after two rounds, but more important; you and two team mates get a coin if you place in the top 3!

GL HF aimers!

Still the best Cyber Range in Norway!
```

### Process

This is the third time Cyber Range has been included as one of the tasks. The concept is fairly simple: You scan your badge, get in the queue and wait for your turn. When it is your turn, you get a calculation you have to do with some quick mental math, and then you have supply the answer by hitting the corresponding targets representing the 8 bit binary answer. Hitting a wrong bit, you loose. If all the correct bits are hit, you move on to the next round.
![Target](target.png)

Mental calculations have never been my strong suit, and after a few tries the other years, I concluded that this was reserved for superhumans that dreams in hexadecimal. Nevertheless I had a look at this years setup. 
At first glance it looked intimidating. XOR two hexadecimal numbers. For example 0x93^0x3b = 0xA8 = 10101000. And then shoot the corresponding targets with a less then reliable foam ball gun. All in less than 30(?) seconds. To complicate things, the target sometimes registered hit on two targets at the same time, resulting in a loss.

A good strategy which would help a lot in this task is to have another team mate help by loading another gun while you shoot, or to do some parallel brain processing.

#### Calculation

For those not familiar with binary and hex it is the representation of numbers with base 2 and 16, while our normal decimal number system uses base 10 (numbers 0 to 9 used). In binary, since we have only have 0 and 1, we got a lot of carry over when adding numbers. 
As illustrated in the table below for decimal numbers 0->16. As we learned in primary school, leading zeroes does not add anything. But it makes it easier to see the pattern. When we get to 10 in decimal, we get a 1 carrying over and start counting from 0 again. That is what we do in binary and hexadecimal as well. Only in binary we get it every 2 numbers. In hexadecimal we have added the letters A to F to get us 16 "numbers", in that way we don't have to carry over until 16. That is also why it is so useful to use hex to display binary numbers, since  8 bit (a byte) can be shortened down to a 2 digit hex (the numbers we need to do calculations on in the task). The prefix 0x is often used before hexadecimal numbers to tell that it is a hex-number. 
|decimal|binary| hex|
|-------|------|----|
|0000|0000|0000| 
|0001|0001|0001|
|0002|0010|0002|
|0003|0011|0003|
|0004|0100|0004|
|0005|0101|0005|
|0006|0110|0006|
|0007|0111|0007|
|0008|1000|0008|
|0009|1001|0009|
|0010|1010|000A|
|0011|1011|000B|
|0012|1100|000C|
|0013|1101|000D|
|0014|1110|000E|
|0015|1111|000F|
|0016|10000|0010|
|....|....|.....|
|0255|11111111|00FF|

Alright, now that we got a basic understanding of how these numers work, we need to look at the operation bitwise XOR ( ^ -symbol). XOR is short of exclusive or) and is a logic operation, resulting in true if one of the inputs are true, but not if both are.
As shown in the table below.
XOR
|bit 1| bit 2| XOR |
|---|---|---|
|0 | 0 | 0 |
|0 | 1 | 1 |
|1 | 0 | 1 |
|1 | 1 | 0 |

With bitwise XOR we just put the two binary numbers on top of each other and compares bit by bit, by using the logic shown in the table. As an example we can take the example task 0x93^0x3b.
|hex | bin |
|---- | ---- |
|0x93 = | 10010011 |
|0x3b = | 00111011 |
|XOR   |  |
|A8  = | 10101000 |

If we glance back at our first table, we see a nice pattern here. The first hex digit represent the first 4 bits in the binary number (A = 1010) and the last represent the last 4 (8 =1000). And it easier to remember 16 combinations, than 256..

That was my strategy when I loaded up the gun, ready to enter the battlefield of the mind.
Some combinations are easier to remember 8 = 1000, A = 1010 F = 1111 4 = 0100 and so on, but doing the calculations, and hitting the targets within the time frame was quite difficult. The gun could store quite a few soft balls, but too many and the gun would jam. It was also a bit variation in ball stiffness and gun power which made aiming and hitting the correct target harder. Quite a few times I used 4 or 5 balls, just to start the challange. Having a teammate loading another gun so you don't have to use the precious time to load during the challange may prove critical. 

My strategy for solving. Taking the most significant bit (first digit) of the two hex numbers, converting them to binary, do bitwise xor and shoot the first targets (7,6,5,4) corresponding to 1's, and then do the least significant bit (last digit in the hex numbers).
|target|7|6|5|4|#|3|2|1|0|
|---|---|---|---|---|---|---|---|---|---|
|binary|1|0|1|0|#|1|0|0|0|
|hit|X||X||#|X||||


After trying for quite a while, with minimal queue, I decied to go chase other white whales, happy that I managed to clear 2 rounds, and knowing I did the correct calculations for 3 rounds a couple of times but missed the targets.

![soclose](soclose.png)

If you did clear 3 rounds, the flag would be submitted, and the task registred as complete.

Final scoreboard, with the record of 12! rounds cleared ⭐
![Scoreboard](scoreboard.png)

# DNA Function

I came across this project on www.codewars.com.

Some backround info on DNA:
DNA is made up of two strands, which join together using Bases and then twist around each other forming the well known Helix shape of DNA. Imagine a ladder split in two down the middle, this is how the strands appear when they are not joined. 

Now there are four bases; adenine (A), thymine (T), cytosine (C) and guanine (G). And only some join; A joins with T, C joins with G.
We can characterise strands of DNA just by the sequence of bases along this strand e.g ACGATCGATC.
And the complimentary to this would be TGCTAGCTAG, meaning these two strands could potentially join and coil forming a piece of DNA.

The idea here is to write a function, so that when given two DNA sequences, the function will return True if the sequences are complimentary and False if not.

Due to the asymmetry of the DNA, every DNA strand has a direction associated with it. The two strands of the double helix run in opposite directions to each other, which we refer to as the 'up-down' and the 'down-up' directions.

# LCZero-Tools
Tools for working with the  LCZero project

## LCZero Hybrid Nets

Brain experiment #31415926
May 15, 2018: I have completed the surgery, the patient is soon to wake up from her slumber. I will plug her into the client software... IT'S ALIVE!!!

The experiment consisted of taking two LCZ nets and just transplanting the weight values from one to the other. In this case the first transplant involved copying the Value Head + Conv of LCZ ID237 into LCZ ID296.
After testing, the hybrid 237Val-296Pol was considerably stronger than both *parent* nets, surprisingly proving this kind of brain surgery was possible. 

## Policy Head (1 node) Test Results

`
Score of lczero ID296 vs lczero ID237: 85 - 41 - 74 [0.610]
Elo difference: 77.71 +/- 38.72

200 of 200 games finished.

Score of lczero Hybrid237_296 vs lczero ID237: 91 - 36 - 73 [0.637]
Elo difference: 98.07 +/- 39.11

200 of 200 games finished.

Score of lczero Hybrid237_296 vs lczero ID296: 69 - 68 - 63 [0.502]
Elo difference: 1.74 +/- 39.97

200 of 200 games finished.
`

### Tournament Results: LCZero nets 1knodes plus Stockfish9 100knodes

`   
   # PLAYER            :  RATING  POINTS  PLAYED   (%)    W    D    L  D(%)
   1 SF9 100kn         :    79.3    65.5      96    68   49   33   14    34
   2 Hybrid 237_296 1kn:     0.0    52.0      96    54   31   42   23    44
   3 237 1kn           :   -74.2    39.0      96    41   21   36   39    38
   4 296 1kn           :   -94.7    35.5      96    37   19   33   44    34

   Hybrid 237_296 1kn  0.0 :     96 (+31,=42,-23),  54.2 %

   vs.                   :  games (  +,  =,  -),   (%) :    Diff
   SF9 100kn             :     32 (  5, 13, 14),  35.9 :   -79.3
   237 1kn               :     32 ( 11, 16,  5),  59.4 :   +74.2
   296 1kn               :     32 ( 15, 13,  4),  67.2 :   +94.7
`

### Download some hybrid nets for testing

**237Val-296Pol**
https://drive.google.com/file/d/1-mR7utYALJ3y1nTq0yxiUwcequnqFwba/view?usp=sharing

**237Val-302Pol**  *(via Francis on discord)* 
https://drive.google.com/file/d/1C0ucCHi3gnh73CLTJyHlUpMrzXgI8SF-/view?usp=sharing

## LC Brain Surgeon

This is a simple Python script that will take two nets and interpolate their Residual, Policy and Value nets independently using a linear interpolation value. This is more abitious and complex than the simple transplantation of the original experiment, and has not yet been tested out.

Have fun!

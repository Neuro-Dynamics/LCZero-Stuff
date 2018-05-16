# LCZero-Tools
Tools for working with the  LCZero project

# LCZero Hybrid Nets

Brain experiment #31415926
May 15, 2018: The surgery has been completed, the patient is soon to wake up from her slumber. I will plug her into the client software... IT'S ALIVE!!!

The experiment consisted of taking two LCZ nets and just transplant the weight values from one to the other. In our case the first transplant involved copying the Value Head + Conv of LCZ ID237 into LCZ ID296.
After testing, the hybrid 237Val-296Pol was stronger than either net, surprisingly proving this kind of brain surgery was possible. 

## Download some hybrid nets for testing

**237Val-296Pol**
https://drive.google.com/file/d/1-mR7utYALJ3y1nTq0yxiUwcequnqFwba/view?usp=sharing

**237Val-302Pol**  *(via Francis on discord)* 
https://drive.google.com/file/d/1C0ucCHi3gnh73CLTJyHlUpMrzXgI8SF-/view?usp=sharing

# LC Brain Surgeon

This is a simple Python script that will take two nets and interpolate their Residual, Policy and Value nets independently using a linear interpolation value. This is more abitious and complex than the simple transplantation of the original experiment, and has not yet been tested out.

Have fun!

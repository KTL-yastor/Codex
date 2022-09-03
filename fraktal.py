

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot(h,w, maxit=20):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2            # who is diverging
        div_now = diverge & (divtime==maxit)  # who is diverging now
        divtime[div_now] = i                  # note when
        z[diverge] = 2                        # avoid diverging too much

    return divtime

def updatefig():
    global mandel
    mandel = mandelbrot(400,400, 20)
    im.set_array(mandel)
    return im,

fig = plt.figure()
mandel = mandelbrot(400,400, 20)
im = plt.imshow(mandel, cmap='hot', interpolation='nearest')

ani = animation.FuncAnimation(fig, updatefig, interval=5, blit=True)
plt.show()
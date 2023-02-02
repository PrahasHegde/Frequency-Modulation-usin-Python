#FM MODULATION

#vm = amplitude of mssg signal
#vc = amplitude of carrier signal
#fm = modulating frequency
#fc = carrier frequency
#mf1, mf2, mf3 = modulating frequency


import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftshift, ifft, ifftshift


def values(vm, vc, fm, fc, mf1, mf2, mf3):
    fs = 2000
    dt = 1/fs
    t = np.arange(0, 2, dt)
    n = np.size(t)
    df = fs/n
    f = np.arange(-fs/2, fs/2, df)


    #plot 1(FM mssg signal 1)
    m1 = vm*np.sin(2*np.pi*fc*t + mf1*np.sin(2*np.pi*fm*t))
    plt.figure(1)
    plt.subplot(2, 1, 1)
    plt.plot(t, m1)
    plt.title("FM mssg signal 1")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    

    #plot 2(FM mssg signal 1 spectrum)
    m1_spec = fftshift(fft(m1))
    plt.figure(1)
    plt.subplot(2, 1, 2)
    plt.plot(f, abs(m1_spec))
    plt.title("FM mssg signal 1 spectrum(mf = 2)")
    plt.xlabel("frequency")
    plt.ylabel("amplitude")
    
    #plot 3(FM mssg signal 2)
    m2 = vm*np.sin(2*np.pi*fc*t + mf2*np.sin(2*np.pi*fm*t))
    plt.figure(2)
    plt.subplot(2, 1, 1)
    plt.plot(t, m2)
    plt.title("FM mssg signal 2")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    

    #plot 4(FM signal 2 spectrum)
    m2_spec = fftshift(fft(m2))
    plt.figure(2)
    plt.subplot(2, 1, 2)
    plt.plot(t, abs(m2_spec))
    plt.title("FM mssg signal 2 spec(mf = 4)")
    plt.xlabel("frequency")
    plt.ylabel("amplitude")
    

    #plot 5(FM signal 3)
    m3 =  vm*np.sin(2*np.pi*fc*t + mf3*np.sin(2*np.pi*fm*t))
    plt.figure(3)
    plt.subplot(2, 1, 1)
    plt.plot(t, m3)
    plt.title("FM mssg signal 3")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    
    #plot 6(FM signal 3 spectrum)
    m3_spec = fftshift(fft(m3))
    plt.figure(3)
    plt.subplot(2, 1, 2)
    plt.plot(t, abs(m3_spec))
    plt.title("FM mssg signal 3 spec(mf = 6)")
    plt.xlabel("frequency")
    plt.ylabel("amplitude")
    plt.show()
    


    
values(5, 15, 10, 50, 2, 4, 6)    
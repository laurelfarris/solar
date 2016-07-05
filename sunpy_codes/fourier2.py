import numpy as np
import math
# from modules import signif_conf

# (Reorder these in the order they appear in the code)
def fourier2(Flux, Delt,
             pad=None, rad=None, norm=None, signif=None, display=None):

    #  ;subtract the mean
    Flux = np.array(Flux)
    newflux = Flux - Flux.mean()
    N = len(newflux)

    base2 = int(np.log(N)/np.log(2)) + 1
    if not pad and (N != 2.**(base2-1)):
        np.append(newflux, np.array(long(2)**(base2)-N, dtype=float))
        '''
        print ("Padded " + str(N) + " data points with " +
               str(long(2)**(base2) - N) + " zeros.")
        print ("**RECOMMEND checking against fourier spectrum of non padded "
               "time series**")
        '''

    #  ;end of padding
    N = len(newflux)  # Redundant?

    #  ;make the frequency array
    Freq = np.arange((N/2)+1) / (N*Delt)

    # ;the -1 ensures a forward FFT
    #   np.fft.ifft does the inverse FT, so -1 is not needed in python.
    # ;the fourier transform is the of the form a(w) + ib(w)
    #   the input array for np.fft.fft can be complex.
    V = np.fft.fft(newflux)

    Power = 2*(abs(V)**2)

    #  ;calculate amplitude
    Amplitude = 2*(abs(V))

    #  ;do not use the zero-eth element -it will just be equal to the mean
    #  ;which has been set to zero anyway
    Freq = (Freq[1:]).flatten
    Power = (Power[1:N/2]).flatten
    Amplitude = (Amplitude[1:N/2]).flatten

    #  ;Calculate the the phase for each frequency. In simple terms this is just
    #  ;arctan( b(w)/a(w) )
    imag = V.imag
    amp = V.real
    imag = imag[1:N/2]
    amp = amp[1:N/2]
    #  Redundant variables here... reduce to 2 lines instead of 4

    Phase = np.arctan2(amp, imag)  # returns phase (array) in radians
    #  ;gives phase between -pi and pi
    #  ;convert to degrees by default
    if not rad:
        Phase = np.degrees(Phase)

    sig_lvl = 0.  # What's the point of this? Defined 5 lines down...
    if signif:
        conf = signif
    else:
        conf = 0.95
    #sig_lvl = signif_conf(newflux, conf)

    if norm:
        var = np.var(newflux)
        power = power * (N/var)
        sig_lvl = sig_lvl * (N/var)
        print "White noise has an expectation value of 1"

    if sig_lvl != 0 and display:
        print ("Confidence level at " +
               str(int(conf*100)) +
               " is: " +
               str(sig_lvl))

    if display:
        plt.plot(Freq, Power)
        plt.plot(Freq, Power, '.')
        plt.show()

    # ;the final output is then an array containing the power and phase at each
    # ;frequency
    # Probably could have used any of the four arrays to define the size of Result
    Result = np.zeros(Power.size, 4)
    Result[:,0] = Freq
    Result[:,1] = Power
    Result[:,2] = Phase
    Result[:,3] = Amplitude
    print "Result[:,0] is frequency"
    print "Result[:,1] is the power spectrum"
    print "Result[:,2] is the phase"

    return Result

f = np.array([1, 3, 4, 5, 3, 2, 6, 4, 3, 4, 1])
blah = fourier2(f, 1)

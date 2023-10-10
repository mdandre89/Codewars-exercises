import numpy
def clean_mean(sample, cutoff):  
    sample = sorted(sample)
    while True:
        m = numpy.mean(sample)
        std = numpy.std(sample)
        if sample[-1] > m + std*cutoff:
            sample = sample[:-1]
        elif sample[0] < m - std*cutoff:
            sample = sample[1:]
        else:
            break
    return round(numpy.mean(sample),2)
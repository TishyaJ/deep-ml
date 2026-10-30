import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    result = dict()
    d = list(data)
    n = len(d)
    #to find median and percentiles, we will use quickselect which asks algorithm to find kth smallest element in the list
    def quickselect(arr,k):
        if len(arr) == 1:
            return arr[0]
        pivot = arr[len(arr)//2]
        l = [x for x in arr if x<pivot]
        mid = [x for x in arr if x==pivot]
        r = [x for x in arr if x>pivot]

        if k<len(l):
            return quickselect(l,k)
        elif k<len(l) + len(mid):
            return int(mid[0])
        else:
            return quickselect(r,k-len(l)-len(mid))
    def percentile(p):
        #using nearest rank method with quickselect
        idx = (p/100)*(n-1)
        lower = int(idx)
        upper = min(lower+1, n-1) #to check against last element
        vallow = quickselect(d, lower)
        valup = quickselect(d, upper)
        weight = idx-lower
        return float(vallow+(valup-vallow)*weight)

    mean = sum(d)/n 
    '''
    if n%2!=0:
        median = float(quickselect(list(d), n//2))
    else:
        m1 = quickselect(list(d), (n-1)//2)
        m2 = quickselect(list(d), n//2)
        median = float((m1+m2)/2)
    '''
    median =percentile(50)
    counts = {}
    ssr =0
    for x in d:
        counts[x] = counts.get(x,0)+1
        # ^--- if we don't find count of the first occurence we initialise it with 0
        ssr += (x-mean)**2
    mode = max(counts, key = counts.get)
    variance = ssr/n 
    std_dev = np.sqrt(variance)

    q1 = percentile(25)
    q3 = percentile(75)

    iqr = q3-q1 

    result = {
        'mean': mean,
        'median': median,
        'mode':mode,
        'variance':variance,
        'standard_deviation': std_dev,
        '25th_percentile': q1,
        '50th_percentile': median,
        '75th_percentile': q3,
        'interquartile_range': iqr
    } 
    return result
import math

def comb(a:int, b:int)->float:
    def fact(n:int)-> int:
        if n==0 or n==1:
            return 1
        result = 1
        for i in range(2,n+1):
            result*=i 
        return result
    num = fact(a)
    denom = (fact(a-b))* fact(b)
    return num//denom

def binomial_probability(n: int, k: int, p: float) -> float:
    """
    Calculate the probability of exactly k successes in n Bernoulli trials.
    
    Args:
        n: Total number of trials
        k: Number of successes
        p: Probability of success on each trial
    
    Returns:
        Probability of k successes
    """
    #first we vhoose the trials where success is there
    choice = comb(n,k)
    psucess = p**k
    pfail = (1-p)**(n-k)

    return choice*psucess*pfail
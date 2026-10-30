def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: list of N lists, each containing K candidate outputs.
        scores: list of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """
    selected = []
    for candlist, scorelist in zip(candidates, scores):
        #we r inside individual prompt's candidates and scores lists
        #first traverse scores for each prompt's candidate and find the highest one's index
        #idx = max(range(len(scoreslist)), key = lambda i: scoreslist[i])
        idx=0
        highest = scorelist[0]
        for i in range(1, len(scorelist)):
            if scorelist[i]>highest:
                highest = scorelist[i]
                idx=i
        selected.append(candlist[idx])
    return selected
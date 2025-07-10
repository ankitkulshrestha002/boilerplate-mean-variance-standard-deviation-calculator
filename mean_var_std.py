import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(list)
    b = a.reshape((3,3))

    mean_a1 = np.mean(b,axis = 0)
    mean_a2 = np.mean(b,axis = 1)
    mean_flat = np.mean(a)

    variance_a1 = np.var(b,axis=0)
    variance_a2 = np.var(b,axis=1)
    variance_flat = np.var(a)

    std_a1 = np.std(b,axis=0)
    std_a2 = np.std(b,axis=1)
    std_flat = np.std(a)

    max_a1 = np.max(b,axis=0)
    max_a2 = np.max(b,axis=1)
    max_flat = np.max(a)

    min_a1 = np.min(b,axis=0)
    min_a2 = np.min(b,axis=1)
    min_flat = np.min(a)

    sum_a1 = np.sum(b,axis=0)
    sum_a2 = np.sum(b,axis=1)
    sum_flat = np.sum(a)

    calculations={'mean': [mean_a1.tolist(),mean_a2.tolist(),mean_flat],
    'variance': [variance_a1.tolist(),variance_a2.tolist(),variance_flat],
    'standard deviation': [std_a1.tolist(),std_a2.tolist(),std_flat],
    'max': [max_a1.tolist(),max_a2.tolist(),max_flat],
    'min': [min_a1.tolist(),min_a2.tolist(),min_flat],
    'sum': [sum_a1.tolist(),sum_a2.tolist(),sum_flat],
    }



    return calculations
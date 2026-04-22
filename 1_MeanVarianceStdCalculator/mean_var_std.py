import numpy as np

def cal_mean(arr):
    return [
        np.mean(arr, axis=0).tolist(),
        np.mean(arr, axis=1).tolist(),
        np.mean(arr).item()
    ]

def cal_var(arr):
    return [
        np.var(arr, axis=0).tolist(),
        np.var(arr, axis=1).tolist(),
        np.var(arr).item()
    ]

def cal_std(arr):
    return [
        np.std(arr, axis=0).tolist(),
        np.std(arr, axis=1).tolist(),
        np.std(arr).item()
    ]

def cal_max(arr):
    return [
        np.max(arr, axis=0).tolist(),
        np.max(arr, axis=1).tolist(),
        np.max(arr).item()
    ]

def cal_min(arr):
    return [
        np.min(arr, axis=0).tolist(),
        np.min(arr, axis=1).tolist(),
        np.min(arr).item()
    ]

def cal_sum(arr):
    return [
        np.sum(arr, axis=0).tolist(),
        np.sum(arr, axis=1).tolist(),
        np.sum(arr).item()
    ]


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations = dict()
    arr = np.array(list).reshape(3, 3)
    # print(arr)
    calculations["mean"] = cal_mean(arr)
    calculations['variance'] = cal_var(arr)
    calculations['standard deviation'] = cal_std(arr)
    calculations['max'] = cal_max(arr)
    calculations['min'] = cal_min(arr)
    calculations['sum'] = cal_sum(arr)
    return calculations
#!/usr/bin/env python
# encoding: utf-8

import sys
import numpy as np

def computeLoss(arr_base, arr_pred):
    if arr_base.shape != arr_pred.shape:
        raise IndexError("arr_base shape is not same with arr_pred")

    sum_arr = arr_base + arr_pred
    sub_arr = np.abs(arr_base - arr_pred)
    div_arr = sub_arr / sum_arr
    sum_all_vals = div_arr.sum()
    return sum_all_vals / (arr_base.shape[0] * arr_base.shape[1])

def load2Array(filepath):
    arr = np.genfromtxt(filepath, delimiter=',')
    return arr[:, 1:] # del the shopid

def main():
    if len(sys.argv) != 3:
        print ("Usage: python metric.py [base_file] [pred_file]")
        sys.exit(-1)

    arr_base = load2Array(sys.argv[1])
    arr_pred = load2Array(sys.argv[2])
    print (computeLoss(arr_base, arr_pred))

if __name__ == "__main__":
    main()

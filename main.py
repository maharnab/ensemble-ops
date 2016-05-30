# -*- coding: utf-8 -*-
"""
Created on Sat Apr 02 13:28:53 2016

@author: rNov
"""

import numpy as np
from itertools import groupby

mat = np.loadtxt("new_input.txt")
n = len(mat[1,:])
mata = mat[:, n-2]
matd = np.empty([0, n], float)

def grp_fun(): 
    global matd   
    m = []
    j1 =[0,]
    
    for n1 in mata:
        m1 = np.floor(n1)
        m = np.append(m, m1)
    
    matb = mat.copy()
    matb[:, n-2] = m
    
    for i, j in groupby(matb[:, n-2]):
        j = list(j)
        jj = len(j)
        j1.append(jj)
        
    j2 = np.cumsum(j1)    
    j3 = np.insert(j2, len(j2), 0)
    matdd = np.empty([0, n], float)
   
    for ii, k in enumerate(j3):
#        i2 = ii+1
        mat_bg = mat[j3[ii-1]:j3[ii], :]
        a = 5       
        c = len(mat_bg) % a

        matc = np.empty([0, n], float)
        for p in range(0, len(mat_bg)-c, a):
            mat_sm = (mat_bg[p:p+a,:])
            row_dd = np.around(np.median(mat_sm, axis=0), decimals=5)
            row_d = np.transpose(row_dd[:, None])           
            matc = np.append(matc, row_d, axis=0)        
            
#--------gives small group, big group & big_median groups-------------           
#            np.savetxt("small_grp%d+%d.txt" % (ii,p), mat_sm, '%.5f') 
#        np.savetxt("big_grp%d.txt" % i2, mat_bg, '%.5f') 
#        np.savetxt("big_grp_median%d.txt" % i2, matc, '%.5f')       
       
        matdd = np.append(matdd, matc, axis=0)   
        
#--------gives median matrix with date and temperature in the end-----
#        np.savetxt("median_matx.txt", matdd, '%.5f')
    
    mat_temp = np.empty([len(matdd), 0], float)
    mat_temp = matdd[:,[n-2, n-1]] 
    
#--------gives only date and temperature------------------------------   
    np.savetxt("mat_temp.txt", mat_temp, '%.5f')   
    
    matd = np.delete(matdd, [n-1, n-2], 1)
    
#--------gives main matrix 'matd' for ensemble ops--------------------
    np.savetxt("matd.txt", matd, '%.5f')

    return matd
                 
def math_fun(matd):
    global matc_col_avg, sd
    matc_row_avg = np.around(np.mean(matd, axis=1), decimals=5)
    matc_col_avg = np.around(np.mean(matd, axis=0), decimals=5)
    matdd = np.around((matd - matc_row_avg[:, None]), decimals=5) 
    matd_col_avg = np.around(np.mean(matdd, axis=0), decimals=5)
    matg = np.around((matdd - matd_col_avg[None, :]), decimals=5) 
    matg_sq = np.around(np.square(matg), decimals=5)
    matv_col_avg = np.around(np.mean(matg_sq, axis=0), decimals=5)
    sd = np.around(np.sqrt(matv_col_avg), decimals=5)
    return (matc_col_avg, sd)
 
def print_fun():
    np.savetxt("sd.txt", sd, '%.5f')   
    for index, (item1, item2) in enumerate(zip(matc_col_avg, sd)):
        print '%02d' % (index + 1), '\t', item1, '\t', item2

    print '\n'  
    return

grp_fun()
#math_fun(matd)
#print_fun()

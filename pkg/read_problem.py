import csv
import math as m
from random import uniform as unif

def read_problem(path):
    # locations
    xy_customers = list(csv.reader(
        open(path + '/xy_customers.csv'),delimiter=';',
        quoting=csv.QUOTE_NONNUMERIC))

    xy_icps = list(csv.reader(
        open(path + '/xy_icps.csv'),delimiter=';',
        quoting=csv.QUOTE_NONNUMERIC))

    xy_crcs = list(csv.reader(
        open(path + '/xy_crcs.csv'),delimiter=';',
        quoting=csv.QUOTE_NONNUMERIC))

    xy_pc = [100.0,60.0]

    # product return
    q = list(csv.reader(
        open(path + '/U.csv'),delimiter=' ',
        quoting=csv.QUOTE_NONNUMERIC))
    
    return xy_customers, xy_icps, xy_crcs, xy_pc, q

def extract_problem(xy_customers, xy_icps, xy_crcs, xy_pc, q):
    
    # index
    I = len(xy_customers)
    J = len(xy_icps)
    C = len(xy_crcs)
    B = len(xy_crcs)
    K = 3
    V = 3
    
    xy_c_j = xy_crcs+xy_icps
    
    # distance cost
    W = [[m.sqrt((cus[0]-icp[0])**2 + (cus[1]-icp[1])**2) for icp in xy_icps] for cus in xy_customers]
    Dcj = [[m.sqrt((c[0]-j[0])**2 + (c[1]-j[1])**2) for c in xy_crcs] for j in xy_icps ]
    DcUj = [[m.sqrt((c[0]-j[0])**2 + (c[1]-j[1])**2) for c in xy_c_j] for j in xy_c_j ]
    Dc = [m.sqrt((xy_pc[0]-crc[0])**2 + (xy_pc[1]-crc[1])**2) for crc in xy_crcs]
    
    # collected product
    U = []
    for i in range(I):
        U.append(q[0][i] + q[1][i] + q[2][i])
    
    # fixed setup cost
    FCT = [100 for i in range(J)]
    FCR = [200 for i in range(C)]
    FCV = [300 for i in range(B)]
    
    return I,J,C,B,K,V,W,DcUj,Dcj,Dc,FCV,FCT,FCR,U
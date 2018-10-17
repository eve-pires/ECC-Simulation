'''' Mode k = 1, for rate 1/7
'''
import numpy as np

def bsc_k1(p_value): #OK
    L_max = 1000
    L = 0
    k1 = 1
    G_k1 = np.array([ 1, 1, 1, 1, 1, 1, 1])
    p = p_value
	#start condition
    error = 0  
    partial_err = 0

    while L <= L_max:
		#digital souce
        u = np.random.randint(2, size = k1)

		#codification
        v = u * G_k1

		#channel
        e = np.where((np.random.randint(2, size = k1)-0.5+p) >= 0.5, 1, 0)
        r = np.where(v+e >= 1, 1, 0)

		#error
        partial_err = round(abs(sum(r-v)/7))
        error = error + partial_err

        L = L + 1 #decrement loops
    P_error = error/(k1*L) 
    return P_error

def bsc_k4(p_value):
    L_max = 1000
    L = 0
    k4 = 4
    G_k4 = np.array([[1,1,0,1,0,0,0], 
                    [0,1,1,0,1,0,0], 
                    [1,1,1,0,0,1,0], 
                    [1,0,1,0,0,0,1]])

    H_k4 = np.array([[1,0,0,1,0,1,1], 
                    [0,1,0,1,1,1,0], 
                    [0,0,1,0,1,1,1]])

    u_hmg = np.array([[0,0,0,0], [1,0,0,0],
                     [0,1,0,0], [1,1,0,0],
                     [0,0,1,0], [1,0,1,0],
                     [0,1,1,0], [1,1,1,0],
                     [0,0,0,1], [1,0,0,1],
                     [0,1,0,1], [1,1,0,1],
                     [0,0,1,1], [1,0,11],
                     [0,1,1,1], [1,1,1,1]])

    v_hmg = np.array([[0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0],
                      [0, 1, 1, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0, 0],
                      [1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1, 0],
                      [1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0],
                      [1, 0, 1, 0, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1],
                      [1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 1, 0, 1],
                      [0, 1, 0, 0, 0, 1, 1], [1, 0, 0, 1, 0, 1, 1],
                      [0, 0, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]])
    p = p_value
    distance_hmg = []
    index = 0
    min_dist = 0
    min_dist_index = 0
    error = 0  
    partial_err = 0

    while L <= L_max:
		#digital souce
        u = np.random.randint(2, size = k4)

		#codification
        v = np.where(np.dot(u, G_k4) >=1, 1, 0)

		#channel
        e = np.where((np.random.randint(2, size = 7)-0.5+p) >= 0.5, 1, 0)
        r = np.where(v+e >= 1, 1, 0)

		#error: Hamming Distance Method
        while index <= 15:
            distance_hmg.append(sum(r-v_hmg[index]))
            index = index+ 1

        min_dist = min(distance_hmg)
        min_dist_index = np.where(min_dist == min(distance_hmg))
        decoded = u_hmg[min_dist_index]

        partial_err = sum(abs(sum(list(decoded) - u)/7))
        if partial_err > 0:
            error = error + 4

        L = L + 1 #decrement loops

    P_error = error /(k4*L) 
    return P_error


def bsc_k7(p_value):
    k7 = 7
    L_max = 1000
    L = 0
    p = p_value
    error = 0
    partial_err = 0

    while L <= L_max:
		#digital souce
        u = np.random.randint(2, size = k7)

		#codification = NONE
        v = u

		#channel
        e = np.where((np.random.randint(2, size = 7)-0.5+p) >= 0.5, 1, 0)
        r = np.where(v+e >= 1, 1, 0)

		#error
        partial_err = round(abs(sum(r-v)/7))
        error = error + partial_err

        L = L + 1 #decrement loops
	
    P_error = error /(k7*L) 
    return P_error

def main():
    probability = [0.05, 0.1, 0.2, 0.3]
    err_k1=[]
    err_k4=[]
    err_k7=[]

    print('>> rate 1/7:')
    for p in probability:
        err_k1.append(bsc_k1(p))
    print("erro: ", err_k1)
    print('     done!')
    
    print('>> rate 4/7: ')
    for p in probability:
        err_k4.append(bsc_k4(p))
    print("erro: ", err_k4)
    print('     done!')

    print('>> rate 7/7:')
    for p in probability:
        err_k7.append(bsc_k7(p))
    print("erro: ", err_k7)
    print('     done!')


if __name__=='__main__':
	main()
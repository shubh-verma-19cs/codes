from array import array
import numpy as np
import time

def read_input(input):
    """ Both inputs are stored in the input.txt file """
    array = np.loadtxt(input,dtype='i',delimiter=' ')
    #Seperate array
    array_first,array_second = np.split(array,2,axis=0)
    return array_first, array_second 

def save_ouput(output):
    output_array = np.savetxt("output.txt",output,delimiter=' ')

def divide_and_conquer(array_first,array_second):
    n = len(array_first)
    if n == 1:
        return array_first * array_second
    else:
        a11 = array_first[:int(len(array_first)/2),:int(len(array_first)/2)]
        a12 = array_first[:int(len(array_first)/2),int(len(array_first)/2):]
        a21 = array_first[int(len(array_first)/2):,:int(len(array_first)/2)]
        a22 = array_first[int(len(array_first)/2):,int(len(array_first)/2):]

        b11 = array_second[:int(len(array_second)/2),:int(len(array_second)/2)]
        b12 = array_second[:int(len(array_second)/2),int(len(array_second)/2):]
        b21 = array_second[int(len(array_second)/2):,:int(len(array_second)/2)]
        b22 = array_second[int(len(array_second)/2):,int(len(array_second)/2):]

        c11 = divide_and_conquer(a11,b11) + divide_and_conquer(a12,b21)
        c12 = divide_and_conquer(a11,b12) + divide_and_conquer(a12,b22)
        c21 = divide_and_conquer(a21,b11) + divide_and_conquer(a22,b21)
        c22 = divide_and_conquer(a21,b12) + divide_and_conquer(a22,b22)

        result = np.zeros((n,n))
        result[:int(len(result)/2),:int(len(result)/2)] = c11
        result[:int(len(result)/2),int(len(result)/2):] = c12
        result[int(len(result)/2):,:int(len(result)/2)] = c21
        result[int(len(result)/2):,int(len(result)/2):] = c22
        #print("Divide and Conquer")
    return result





if __name__ == "__main__":
    # array_first,array_second = read_input('./input.txt')
    array_first = [[1,3,5,6],[1,8,6,3],[7,8,1,0],[8,4,2,10]]
    array_second = [[5,-2,6,1],[-7,-10,9,3],[4,2,5,3],[7,1,-4,10]]
    output = divide_and_conquer(array_first,array_second)
    save_ouput(output)
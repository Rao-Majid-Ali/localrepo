import numpy as np
import time

# size = 1_000_000
# py_list = list(range(size))
# start = time.time()
# sq_list = [i**2 for i in py_list]
# end = time.time()
# print(f"python list time = {end-start} seconds")

# np_arr = np.array(py_list)
# start = time.time()
# #vcectorization
# sq_arr = np_arr ** 2
# end = time.time()
# print(f"python list time = {end-start} seconds")

# #Memory
# import sys
# print(f"python list size = {sys.getsizeof(py_list) * len(py_list) } bytes")
# print(f"python np_arr size = {np_arr.nbytes} bytes")


# creating array from lists
# list1 = [1,2,3,4,5,"prime"]
# arr = np.array(list1)
# print(arr,type(arr),arr.dtype,arr.shape)

# _2D_list = [[1,2,3],[4,5,6],[6,7,8],[9,10,11]]
# _2D_arr = np.array(_2D_list)
# print(_2D_arr, _2D_arr.shape)


#create arr from functions
# arr1 = np.zeros((3,4)) #pefil
# print(arr1, arr1.shape)

# arr2 = np.zeros((2,3), dtype = "int64")#pefil with int size is 64 bytes
# print(arr2, arr2.shape)

# arr3 = np.ones((2,3), dtype = "int64")#pefil with (1) int size is 64 bytes
# print(arr3, arr3.shape)

# arr4 = np.full((2,3),100, dtype = "int64")#pefil with any val
# print(arr4, arr4.shape)

# arr5 = np.eye(5, dtype = "int64")#indentity matrix is created
# print(arr5, arr5.shape)

# arr6 = np.arange(0,10,2)#like a range funtion takes 3 parameters and create n to n-1 with incr
# print(arr6, arr6.shape)

# arr7 = np.linspace(1,100,4)#evenly spaced array last like(4) is size of array 
# print(arr7, arr7.shape)


# array properties
# arr = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0],[7,8,9,0]])
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.ndim)
# float_arr = arr.astype(np.float64)
# print(float_arr," ",float_arr.dtype)


#Operation on arrays

#reshaping array
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr,arr.shape)

# reshaped = arr.reshape((3,2)) # only possible when same numbers of elemnets in both
# print(reshaped,reshaped.shape)

# flattened = arr.flatten() #convert 2D array in to 1D
# print(flattened,flattened.shape)


# # indexing
# # arr = np.array([1,2,3,4,5])
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr[0][1]) # we can also write it as [0,1]
# print(arr[1,2])

#fancy indexing
# arr = np.array([1,2,3,4,5])
# idx = [0,1,3]
# print(arr[idx])

# #boolean indexing
# arr = np.array([1,2,3,4,5])
# print(arr[arr > 2])
# print(arr[arr%2 == 0])
# print(arr[arr%2 != 0])


# slicing the array
# arr = np.array([1,2,3,4,5])
# arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(arr1[2:3]) #[start:end:step]
# print(arr[1:4:2])
# print(arr[1:])
# print(arr[:4])
# print(arr[::])
# print(arr[::2])


#copy in list vs view in array
# num_list = [1,2,3,4,5]
# sub_list = num_list[1:3]
# print(sub_list)
# sub_list[0] = 200
# print(sub_list)
# print(num_list)

# num_arr = np.array([1,2,3,4,5])
# sub_arr = num_arr[1:3]
# print(sub_arr)
# sub_arr[0] = 200
# print(sub_arr)
# print(num_arr)


# 3D arrays

# arr3D = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]]) # 2 * 3 * 2
# print(arr3D,arr3D.shape,arr3D.size)

# #indexing in 3D
# print(arr3D[0,1,1]) # to print 4
# print(arr3D[1,2,0]) # 11

# slicing in 3D array as  [layers start: end,row start: end , elements start : end]
# print(arr3D[:,0,:]) # first row from both the layers
# print(arr3D[:,:,0]) # first column from both the layers
# print(arr3D[1:,1,:2]) 
# print(arr3D[:,1,:2])

# arr3D[:,0,:] = 99 # manipulate the data
# print(arr3D)


# #Vectorization
# in python list whenn we do any operation we use loop but in arrays we have 
# vectorization that operation can be perforn as single whole

# arr = np.array([1,2,3,4,5])
# arr1 = np.array([5,6,7,8,9])
# print(arr**2)
# print(arr+10)
# print(arr+arr1)


# # Broadcasting
# it is useful or make poosible when we perform Math operation between arry/vectors and vectors
# or the  two unequal arrys
#rules for brosadcasting  two dimensions are compatible when 
# 1. they re equal or
# 2. one of them is 1            like (3,2) and (5,2) not posible but (3,2) & (1,2) possible

# arr = np.array([1,2,3,4,5])
# arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# arr5 = np.array([[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10]] )
# arr6 = arr1+arr5  # Error because (2,5) & (3,5)
# arr2 = arr + 5
# arr3 = arr1 + 5
# print(arr.shape)
# print(arr1.shape)

# # print(arr + arr1) # they are compatible because arr is 1*5 & arr1 is 2*5  in this 5 & 5 match & 1&2 does not but there is 1 at one side
# print(arr2)
# print(arr3)



#Vector Normalization
#normalizing an array means transforming its values so they fit into specific scale or range
#used for incresaing performance of our ML , its has many types and formulas
#one type is Standard normalizing or (Z score arr-mean/std deviation)

# arr = np.array([[1,2],[3,4]])
# mean = np.mean(arr)
# std = np.std(arr) # standard deviation
# print(mean)
# print(std)
# normalized_arr = (arr-mean)/std
# print(normalized_arr) # standard normalizaion give us array whose mean = 0 & std-div = close to 1 



#Numpy Mathematical functions
#aggregation functions
# arr = np.array([[1,2,3,4,5,6]])
# print(np.sum(arr))
# print(np.prod(arr))
# print(np.min(arr))
# print(np.argmin(arr)) # gives the index where is the min value
# print(np.max(arr))
# print(np.argmax(arr)) # gives the index where is the max value
# print(np.mean(arr))
# print(np.std(arr))  # sqrt((sigma(val-max)**2)/N)
# print(np.median(arr)) #gives the middle value
# print(np.var(arr)) #sigma((val-mean)**2)/N   square of std

# # power functions
# arr = np.array([[1,2,3,4,5,6]])
# print(np.square(arr))
# print(np.sqrt(arr))
# print(np.pow(arr,3))

#log & exponential functions
# arr = np.array([[1,2,3,4,5,6]])
# print(np.log(arr)) # natural log or base e
# print(np.log10(arr))
# print(np.log2(arr))
# print(np.exp(arr))

# #rounding values
# print(np.round(3.4)) # round of to near val
# print(np.ceil(3.4)) # round up to  val
# print(np.floor(3.4)) # round down to  val
# print(np.trunc(33.9)) # for only fractional part


# # some extras+
# arr = np.array([[1,2,-3,4,-5,-6,5,6]])
# print(np.unique(arr)) # only unique values
# print(np.sort(arr))
# print(np.abs(arr)) #its makes the negative values to positives

## we also have trignometric , matrix 
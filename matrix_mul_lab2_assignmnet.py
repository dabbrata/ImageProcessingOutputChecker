import cv2
import matplotlib.pyplot as plt
import numpy as np 
from IPython.core.pylabtools import figsize
from scipy import signal
#additional library for toeplitz matrix
import scipy.linalg as sl

img = cv2.imread(r"C:\Users\WIN\Desktop\image_lab\Lena.jpg")
initimg = img.copy()

plt.figure()
plt.imshow(img[:,:,::-1])
plt.title('Input image')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ig=img.copy()
img = cv2.resize(img, (128,128))



kernel = np.array(([0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]),
                  np.float32)

I_row_num, I_col_num = img.shape
F_row_num, F_col_num = kernel.shape


output_row_num = I_row_num + F_row_num - 1
output_col_num = I_col_num + F_col_num - 1
output_shape = output_row_num, output_col_num
print(output_row_num, output_col_num)

F_zero_padded = np.pad(kernel, ((output_row_num-F_row_num, 0),
                                (0,output_col_num-F_col_num)),
                       'constant', constant_values = 0)
print(F_zero_padded)
print(F_zero_padded.shape)

#using additional library for toeplitz matrix
toeplitz_list = []
for i in range(F_zero_padded.shape[0]-1, -1,-1):#iterating from last row to first (as our image will be flipped upside down)
  c = F_zero_padded[i,:];#taking the i'th row 
  r = np.r_[c[0], np.zeros(I_col_num-1)] #concatening two array quickly (Translates slice objects to concatenation along the first axis)
  toeplitz_m = sl.toeplitz(c,r)#createing toeplitz matrices for each row
  toeplitz_list.append(toeplitz_m)
  
  c = range(1, F_zero_padded.shape[0]+1)
  
  
r = np.r_[c[0], np.zeros(img.shape[0]-1, dtype=int)]#number of column in this symbolic doubly blocked toeplitz should be equal to the number of row in the input signal
doubly_indices = sl.toeplitz(c,r)
print(doubly_indices)

#shape of one of those small toeplitz matrices
h = toeplitz_list[0].shape[0]*doubly_indices.shape[0]
w = toeplitz_list[0].shape[1]*doubly_indices.shape[1]
doubly_blocked_shape = [h, w]
doubly_blocked = np.zeros(doubly_blocked_shape)



#tile the toeplitz matrix
b_h, b_w = toeplitz_list[0].shape
for i in range(doubly_indices.shape[0]):
  for j in range(doubly_indices.shape[1]):
    start_i = i*b_h
    start_j = j*b_w
    end_i = start_i+b_h
    end_j = start_j + b_w
    doubly_blocked[start_i: end_i, start_j: end_j]=toeplitz_list[doubly_indices[i,j]-1]
print(doubly_blocked)



#input matrix to vector
def matrix_to_vector(input):
  input_h, input_w = input.shape
  output_vector = np.zeros(input_h*input_w, dtype=np.float32)
  #flip the input matrix upside down to start from the last row
  input = np.flipud(input)
  for i, row in enumerate(input):
    st = i*input_w
    nd = st+input_w
    output_vector[st:nd]=row
  return output_vector

# print(img)
# print(matrix_to_vector(img))

#get result of the convolution by matrix multiplication
vectorized_input = matrix_to_vector(img)
print(doubly_blocked.shape)
print(vectorized_input.shape)
print(vectorized_input)
result_vector = np.matmul(doubly_blocked, vectorized_input)
print("result: ", result_vector)

#vector_to_matrix
def vector_to_matrix(input, output_shape):
  output_h, output_w = output_shape
  output = np.zeros(output_shape, dtype=np.float32)
  for i in range(output_h):
    st = i*output_w
    nd = st+output_w
    output[i,:] = input[st:nd]
  #flipping again downup
  output = np.flipud(output)
  return output
out = vector_to_matrix(result_vector,  output_shape)

out = out/255

     

out = cv2.cvtColor(out,cv2.COLOR_BGR2RGB) 



# Two subplots, unpack the axes array immediately
f, axis = plt.subplots(3, 2, figsize=(20,20))

axis[0,0].imshow(initimg[:,:,::-1])
axis[0,0].set_title('Input RGB')
plt.figure()
plt.imshow(initimg[:,:,::-1])
plt.title("Input RGB")



axis[0,1].imshow(ig,'gray')
axis[0,1].set_title('Input Gray')
plt.figure()
plt.imshow(ig,'gray')
plt.title("Input Gray")


axis[1,0].imshow(img,'gray')
axis[1,0].set_title('Resized Gray(as input)')
plt.figure()
plt.imshow(img,'gray')
plt.title("Resized Gray(as input)")


axis[1,1].imshow(out,'gray')
axis[1,1].set_title('Output(Using matrix_multiplication)')
plt.figure()
plt.imshow(out,'gray')
plt.title("Output(Using matrix_multiplication)")

result1 = signal.convolve2d(img, kernel, "full")/255
result1 = cv2.cvtColor(result1, cv2.COLOR_BGR2RGB)
axis[2,0].imshow(result1,'gray')
axis[2,0].set_title('Using Convolve2d')
plt.figure()
plt.imshow(result1,'gray')
plt.title("Using Convolve2d")


result2 = cv2.filter2D(img, -1, kernel)
result2 = cv2.cvtColor(result2, cv2.COLOR_BGR2RGB)
axis[2,1].imshow(result2,'gray')
axis[2,1].set_title('Using filter2D')
plt.figure()
plt.imshow(result2,'gray')
plt.title("Using filter2D")
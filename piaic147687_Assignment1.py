{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "NgUeapcvmIRh"
   },
   "source": [
    "# **Assignment For Numpy**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yhr3JicwnA-4"
   },
   "source": [
    "Difficulty Level **Beginner**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hVPqDJ1SnKSh"
   },
   "source": [
    "1. Import the numpy package under the name np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "SePu31zKmgS-"
   },
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "d0gO81krnL7g"
   },
   "source": [
    "2. Create a null vector of size 10 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "2s6o2JPgnSBr"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "null_vector = np.zeros(10, dtype = \"int\")\n",
    "null_vector"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BJTMK03fnS1w"
   },
   "source": [
    "3. Create a vector with values ranging from 10 to 49"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "qRXxXuWdnj1M"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,\n",
       "       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,\n",
       "       44, 45, 46, 47, 48, 49])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "vect= np.arange(10,50)\n",
    "vect"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "n63lzg5Onkcn"
   },
   "source": [
    "4. Find the shape of previous array in question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "1FueBdqPn_q7"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(40,)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.shape(vect)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "AzMlQj1MoAVe"
   },
   "source": [
    "5. Print the type of the previous array in question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "AO9PYmdWoE1L"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "numpy.ndarray"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(vect)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0qaKS13Yon-U"
   },
   "source": [
    "6. Print the numpy version and the configuration\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "T3wY24e1oorh"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.19.2\n",
      "blas_mkl_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\include']\n",
      "blas_opt_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\include']\n",
      "lapack_mkl_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\include']\n",
      "lapack_opt_info:\n",
      "    libraries = ['mkl_rt']\n",
      "    library_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\lib']\n",
      "    define_macros = [('SCIPY_MKL_H', None), ('HAVE_CBLAS', None)]\n",
      "    include_dirs = ['C:/Users/Rafay/anaconda3\\\\Library\\\\include']\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(np.__version__)\n",
    "print(np.show_config())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZyUUiQf5oyvE"
   },
   "source": [
    "7. Print the dimension of the array in question 3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "pLXfuIqIo0vq"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(vect.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JYVMuFrqpBdV"
   },
   "source": [
    "8. Create a boolean array with all the True values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "3apZsISzpFKR"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ True,  True],\n",
       "       [ True,  True]])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "boolarray = np.ones((2,2), dtype = \"bool\")\n",
    "boolarray"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "4zbBooWZpPBU"
   },
   "source": [
    "9. Create a two dimensional array\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "id": "KfPQEiVIpdTo"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 1, 2],\n",
       "       [3, 4, 5]])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2array = np.arange(6).reshape(2,3)\n",
    "d2array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "do9wPAFbpqC7"
   },
   "source": [
    "10. Create a three dimensional array\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "id": "ZCO_q-KZqAeW"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 0,  1,  2],\n",
       "        [ 3,  4,  5],\n",
       "        [ 6,  7,  8],\n",
       "        [ 9, 10, 11]],\n",
       "\n",
       "       [[12, 13, 14],\n",
       "        [15, 16, 17],\n",
       "        [18, 19, 20],\n",
       "        [21, 22, 23]]])"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d3array = np.arange(24).reshape(2,4,3)\n",
    "d3array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a4iysJ87qEeb"
   },
   "source": [
    "Difficulty Level **Easy**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DehgqszSqjY6"
   },
   "source": [
    "11. Reverse a vector (first element becomes last)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "id": "tfevmc4VqkWu"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "original vector [0 1 2 3 4]\n",
      "Reversed vector [4 3 2 1 0]\n"
     ]
    }
   ],
   "source": [
    "vect1 = np.arange(5)\n",
    "print(\"original vector\", vect1)\n",
    "reverse_vector = np.flipud(vect1)\n",
    "print(\"Reversed vector\", reverse_vector)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yoATXS-qqk_q"
   },
   "source": [
    "12. Create a null vector of size 10 but the fifth value which is 1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "id": "AheZ32Owqpte"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "null_vector = np.zeros(10,dtype=\"int\")\n",
    "null_vector[4] = 1\n",
    "null_vector"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "RZRzOBbFsY0w"
   },
   "source": [
    "13. Create a 3x3 identity matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "id": "va2ou0BHsvEj"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 0 0]\n",
      " [0 1 0]\n",
      " [0 0 1]]\n",
      "The dimension of above identity matrix is 2\n",
      "[[[1 0 0]\n",
      "  [0 1 0]\n",
      "  [0 0 1]]]\n",
      "The dimension of three dimension identity matrix is 3\n"
     ]
    }
   ],
   "source": [
    "I3matrix = np.identity(3, dtype=int)\n",
    "print(I3matrix)\n",
    "print(\"The dimension of above identity matrix is\",I3matrix.ndim)\n",
    "d3matrix = I3matrix.reshape(1,3,3)\n",
    "print(d3matrix)\n",
    "print(\"The dimension of three dimension identity matrix is\",d3matrix.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "lnN5drkUs6o2"
   },
   "source": [
    "14. arr = np.array([1, 2, 3, 4, 5]) \n",
    "\n",
    "---\n",
    "\n",
    " Convert the data type of the given array from int to float "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "id": "59EIQt6otKUB"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1. 2. 3. 4. 5.]\n"
     ]
    }
   ],
   "source": [
    "float_array = np.array([1,2,3,4,5], dtype=\"float\")\n",
    "print(float_array)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fSL2AKJetTes"
   },
   "source": [
    "15. arr1 =          np.array([[1., 2., 3.],\n",
    "\n",
    "                    [4., 5., 6.]])  \n",
    "                      \n",
    "    arr2 = np.array([[0., 4., 1.],\n",
    "     \n",
    "                   [7., 2., 12.]])\n",
    "\n",
    "---\n",
    "\n",
    "\n",
    "Multiply arr1 with arr2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "id": "7VDXgRQDuJNV"
   },
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-50-18a670a29e46>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m            [7., 2., 12.]])\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mres\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0marr1\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0marr2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mres\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)"
     ]
    }
   ],
   "source": [
    "arr1 = np.array([[1., 2., 3.],\n",
    "\n",
    "            [4., 5., 6.]])  \n",
    "arr2 = np.array([[0., 4., 1.],\n",
    "\n",
    "           [7., 2., 12.]])\n",
    "res = arr1.dot(arr2)\n",
    "print(res)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a8yJ438-uKni"
   },
   "source": [
    "16. arr1 = np.array([[1., 2., 3.],\n",
    "                    [4., 5., 6.]]) \n",
    "                    \n",
    "    arr2 = np.array([[0., 4., 1.], \n",
    "                    [7., 2., 12.]])\n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "Make an array by comparing both the arrays provided above"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "id": "3MPDaAlYueF3"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "arr1 = np.array([[1., 2., 3.],\n",
    "\n",
    "            [4., 5., 6.]]) \n",
    "arr2 = np.array([[0., 4., 1.],\n",
    "\n",
    "            [7., 2., 12.]])\n",
    "ndarray = arr1 == arr2\n",
    "newarray = ndarray.all()\n",
    "print(newarray)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "3xiD0eJluewk"
   },
   "source": [
    "17. Extract all odd numbers from arr with values(0-9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "id": "J_qbt_EuvM7l"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The array is [0 1 2 3 4 5 6 7 8 9]\n",
      "Odd numbers are [1 3 5 7 9]\n"
     ]
    }
   ],
   "source": [
    "array = np.arange(10)\n",
    "print(\"The array is\",array)\n",
    "odd_array = array[1:10:2]\n",
    "print(\"Odd numbers are\",odd_array)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "zpg5cyLsvPoZ"
   },
   "source": [
    "18. Replace all odd numbers to -1 from previous array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "id": "rXUV1-ULvQdd"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The array is [0 1 2 3 4 5 6 7 8 9]\n",
      "Odd numbers are [1 3 5 7 9]\n",
      "Replaced odd numbers with -1 [-1 -1 -1 -1 -1]\n",
      "The original array becomes now [ 0 -1  2 -1  4 -1  6 -1  8 -1]\n"
     ]
    }
   ],
   "source": [
    "array = np.arange(10)\n",
    "print(\"The array is\",array)\n",
    "odd_array = array[1:10:2]\n",
    "print(\"Odd numbers are\",odd_array)\n",
    "odd_array[0:5] = -1\n",
    "print(\"Replaced odd numbers with -1\",odd_array)\n",
    "print(\"The original array becomes now\",array)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "FWpHTWTDvjvi"
   },
   "source": [
    "19. arr = np.arange(10)\n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "Replace the values of indexes 5,6,7 and 8 to **12**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "id": "ensZ3lqwvlSb"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  1  2  3  4 12 12 12 12  9]\n"
     ]
    }
   ],
   "source": [
    "arr = np.arange(10)\n",
    "arr[5:9] =12\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ib-vBffAv0zy"
   },
   "source": [
    "20. Create a 2d array with 1 on the border and 0 inside"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "id": "RmzcjNYrwDrM"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 1 1]\n",
      " [1 0 1]\n",
      " [1 1 1]]\n"
     ]
    }
   ],
   "source": [
    "d2array = np.array([[1, 1, 1],[1,0, 1],[1,1,1]])\n",
    "print(d2array)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "E1diIFSEwEmh"
   },
   "source": [
    "Difficulty Level **Medium**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eGLZmNb_wKb4"
   },
   "source": [
    "21. arr2d = np.array([[1, 2, 3],\n",
    "\n",
    "                    [4, 5, 6], \n",
    "\n",
    "                    [7, 8, 9]])\n",
    "\n",
    "---\n",
    "\n",
    "Replace the value 5 to 12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {
    "id": "VdUnsUOZwJFz"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  2,  3],\n",
       "       [ 4, 12,  6],\n",
       "       [ 7,  8,  9]])"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr2d = np.array([[1, 2, 3],\n",
    "\n",
    "            [4, 5, 6], \n",
    "\n",
    "            [7, 8, 9]])\n",
    "arr2d[1,1] = 12\n",
    "arr2d"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "TEbFhlPZxaKO"
   },
   "source": [
    "22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])\n",
    "\n",
    "---\n",
    "Convert all the values of 1st array to 64\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "id": "eYzephU8xmsg"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 1  2  3]\n",
      "  [ 4  5  6]]\n",
      "\n",
      " [[ 7  8  9]\n",
      "  [10 11 12]]]\n",
      "============================\n",
      "[[[64 64 64]\n",
      "  [64 64 64]]\n",
      "\n",
      " [[ 7  8  9]\n",
      "  [10 11 12]]]\n"
     ]
    }
   ],
   "source": [
    "arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])\n",
    "print(arr3d) \n",
    "print(\"============================\")\n",
    "arr3d[0] =64\n",
    "print(arr3d)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "vZj0Ndvnx6f0"
   },
   "source": [
    "23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {
    "id": "pM4e9YfdyHSv"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "d2array =np.arange(10).reshape(2,5)\n",
    "\n",
    "print(d2array[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "C3dkW0lZyVps"
   },
   "source": [
    "24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {
    "id": "IrrzK2xgygqV"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2 3 4]\n",
      " [5 6 7 8 9]]\n",
      "The 2nd value from 2nd 1-D array  is 6 :  [[6]]\n"
     ]
    }
   ],
   "source": [
    "d2array =np.arange(10).reshape(2,5)\n",
    "print(d2array)\n",
    "print(\"The 2nd value from 2nd 1-D array  is 6 : \",d2array[1:,1:2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "G3dLwOO9yyrE"
   },
   "source": [
    "25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "id": "5Bx4fqsLyqGD"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 1 2 3 4]\n",
      " [5 6 7 8 9]]\n",
      "[[2]\n",
      " [7]]\n"
     ]
    }
   ],
   "source": [
    "d2array =np.arange(10).reshape(2,5)\n",
    "print(d2array)\n",
    "print(d2array[0:2,2:3])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "CQ9YST5jy0IL"
   },
   "source": [
    "26. Create a 10x10 array with random values and find the minimum and maximum values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "id": "lhJPugjQzG6W"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Array:\n",
      "[[0.79621655 0.68616972 0.23930232 0.79864204 0.67189044 0.46018476\n",
      "  0.53060466 0.46240954 0.96185422 0.42006399]\n",
      " [0.73601845 0.04963688 0.22770468 0.93580443 0.19324351 0.98291563\n",
      "  0.00760036 0.86230473 0.8421181  0.31503371]\n",
      " [0.16003911 0.85413622 0.37786357 0.46959632 0.07098304 0.17511669\n",
      "  0.63090842 0.6620201  0.75855828 0.42215295]\n",
      " [0.04803918 0.40074709 0.16332959 0.17850643 0.0319966  0.4605457\n",
      "  0.84075551 0.08039615 0.1681122  0.98313495]\n",
      " [0.64612151 0.4257284  0.76512465 0.2424692  0.86907494 0.39246054\n",
      "  0.1556014  0.83967224 0.74840072 0.71111813]\n",
      " [0.85826906 0.95836091 0.06594532 0.4334133  0.25993577 0.84835816\n",
      "  0.60017243 0.03854214 0.7452855  0.94082279]\n",
      " [0.9846353  0.8667901  0.79249251 0.76615346 0.67409234 0.58717076\n",
      "  0.77221544 0.37883204 0.00554228 0.92062828]\n",
      " [0.13310565 0.21856402 0.80931414 0.49420948 0.39477199 0.80059464\n",
      "  0.23170119 0.08922974 0.85865266 0.54635659]\n",
      " [0.58147655 0.2345543  0.97561475 0.00446442 0.42559794 0.15255535\n",
      "  0.88009407 0.99033466 0.51295448 0.90412392]\n",
      " [0.68317682 0.56124096 0.13596018 0.63539514 0.06727995 0.57192191\n",
      "  0.40429731 0.02733025 0.53789346 0.99486163]]\n",
      "Minimum and Maximum Values:\n",
      "0.004464418457857722 0.9948616326823846\n"
     ]
    }
   ],
   "source": [
    "x = np.random.random((10,10))\n",
    "print(\"Original Array:\")\n",
    "print(x) \n",
    "xmin, xmax = x.min(), x.max()\n",
    "print(\"Minimum and Maximum Values:\")\n",
    "print(xmin, xmax)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cAgDt6KazHk6"
   },
   "source": [
    "27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "---\n",
    "Find the common items between a and b\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "id": "kBXZanxIzs_F"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2 4]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,2,3,2,3,4,3,4,5,6]) \n",
    "b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "common_items = np.intersect1d(a,b)\n",
    "print(common_items)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "lF9IzWOAztpD"
   },
   "source": [
    "28. a = np.array([1,2,3,2,3,4,3,4,5,6])\n",
    "b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "\n",
    "---\n",
    "Find the positions where elements of a and b match\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {
    "id": "JR-mHQLH0HY_"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The common items are: [2 4]\n",
      "The  positions where elements of a and b match : [[1]\n",
      " [3]\n",
      " [5]\n",
      " [7]]\n"
     ]
    }
   ],
   "source": [
    " a= np.array([1,2,3,2,3,4,3,4,5,6])\n",
    "b = np.array([7,2,10,2,7,4,9,4,9,8])\n",
    "common_items = np.intersect1d(a,b)\n",
    "print(\"The common items are:\",common_items)\n",
    "print(\"The  positions where elements of a and b match :\",np.argwhere(a==b))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "mMDiefpH0H1x"
   },
   "source": [
    "29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)\n",
    "\n",
    "---\n",
    "Find all the values from array **data** where the values from array **names** are not equal to **Will**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "gfc1Lpf81ZSR"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Bob' 'Joe' 'Will' 'Bob' 'Will' 'Joe' 'Joe']\n",
      "[[ 0.44285334  0.36629046 -0.50809913 -1.21045203]\n",
      " [-0.56523595 -0.77715438  0.19541988 -0.27063348]\n",
      " [-0.86176421 -0.52545571  2.40465475 -0.8810829 ]\n",
      " [-0.01833457  0.48648263  0.58305352  1.21725781]\n",
      " [ 0.66205103  0.68755371  2.22108099 -0.81321689]\n",
      " [-0.16078105 -2.89259937  0.48648189 -0.40461735]\n",
      " [-0.74338923 -1.24829942  0.17175308  0.71704824]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[ 0.44285334,  0.36629046, -0.50809913, -1.21045203],\n",
       "       [-0.56523595, -0.77715438,  0.19541988, -0.27063348],\n",
       "       [-0.01833457,  0.48648263,  0.58305352,  1.21725781],\n",
       "       [-0.16078105, -2.89259937,  0.48648189, -0.40461735],\n",
       "       [-0.74338923, -1.24829942,  0.17175308,  0.71704824]])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) \n",
    "data = np.random.randn(7, 4)\n",
    "print(names)\n",
    "print(data)\n",
    "data[names != \"Will\"]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "52zEjDMf1aXS"
   },
   "source": [
    "30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)\n",
    "\n",
    "---\n",
    "Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "8RYG0kLO1mHw"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ True False False  True False False False]\n",
      "[[-0.61001728  1.29690989  0.54898212  0.38311296]\n",
      " [-1.62446931  0.23957964  0.86224643  0.84830595]]\n"
     ]
    }
   ],
   "source": [
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) \n",
    "data = np.random.randn(7, 4)\n",
    "compare = (names != \"Will\") & (names != \"Joe\")\n",
    "print(compare)\n",
    "print(data[compare])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Q7hjf2bd2dCY"
   },
   "source": [
    "Difficulty Level **Hard**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "b48g7aRA2jVM"
   },
   "source": [
    "31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "id": "EbwfSCrW2f9_"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1.5,  2.5,  3.5],\n",
       "       [ 4.5,  5.5,  6.5],\n",
       "       [ 7.5,  8.5,  9.5],\n",
       "       [10.5, 11.5, 12.5],\n",
       "       [13.5, 14.5, 15.5]])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d2array=np.arange(1.5,16.5).reshape(5,3)\n",
    "d2array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ei_nDHtO3qBk"
   },
   "source": [
    "32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "id": "phOxVpBM4M6D"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[ 1.5,  2.5,  3.5,  4.5],\n",
       "        [ 5.5,  6.5,  7.5,  8.5]],\n",
       "\n",
       "       [[ 9.5, 10.5, 11.5, 12.5],\n",
       "        [13.5, 14.5, 15.5, 16.5]]])"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d3array=np.arange(1.5,17.5).reshape(2,2,4)\n",
    "d3array"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "uyiQaMjA4d_x"
   },
   "source": [
    "33. Swap axes of the array you created in Question 32"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "id": "w2m9p8064VtR"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[[ 1  2  3  4]\n",
      "  [ 5  6  7  8]]\n",
      "\n",
      " [[ 9 10 11 12]\n",
      "  [13 14 15 16]]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[[ 1,  5],\n",
       "        [ 2,  6],\n",
       "        [ 3,  7],\n",
       "        [ 4,  8]],\n",
       "\n",
       "       [[ 9, 13],\n",
       "        [10, 14],\n",
       "        [11, 15],\n",
       "        [12, 16]]])"
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d3array=np.arange(1,17).reshape(2,2,4)\n",
    "print(d3array)\n",
    "c= np.swapaxes(d3array,1,2)\n",
    "c"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "2dlU_yUR4mVZ"
   },
   "source": [
    "34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "id": "tmBabEJ-5JgB"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.         1.         1.41421356 1.73205081 2.         2.23606798\n",
      " 2.44948974 2.64575131 2.82842712 3.        ]\n"
     ]
    }
   ],
   "source": [
    "arr= np.arange(10)\n",
    "sqrt_1 = np.sqrt(arr)\n",
    "print(sqrt_1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SNAM4dpu5RKA"
   },
   "source": [
    "35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "id": "3pxebU2b5q9Z"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3 6]\n"
     ]
    }
   ],
   "source": [
    "arr1 =np.array([1, 2, 3])\n",
    "arr2 =np.array([4,5,6])\n",
    "a = np.amax(arr1)\n",
    "b= np.amax(arr2)\n",
    "max_array = np.array([a,b])\n",
    "print(max_array)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fz_bpqm28qmD"
   },
   "source": [
    "36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])\n",
    "\n",
    "---\n",
    "Find the unique names and sort them out!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "id": "hiSNMgcY87Ey"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Bob' 'Joe' 'Will']\n"
     ]
    }
   ],
   "source": [
    "names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])\n",
    "u = np.unique(names)\n",
    "print(u)\n",
    "                 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dguMNzob870H"
   },
   "source": [
    "37. a = np.array([1,2,3,4,5])\n",
    "b = np.array([5,6,7,8,9])\n",
    "\n",
    "---\n",
    "From array a remove all items present in array b\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "id": "eCNJXPvK9IAr"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a =  [1 2 3 4]\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1,2,3,4,5]) \n",
    "b = np.array([5,6,7,8,9])\n",
    "\n",
    "result = np.setdiff1d(a, b)\n",
    "print(\"a = \",result)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "gz4Dvd4b_Akh"
   },
   "source": [
    "38.  Following is the input NumPy array delete column two and insert following new column in its place.\n",
    "\n",
    "---\n",
    "sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) \n",
    "\n",
    "\n",
    "---\n",
    "\n",
    "newColumn = numpy.array([[10,10,10]])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "id": "lLWAJWJJ_I3d"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[34 43 73]\n",
      " [82 22 12]\n",
      " [53 94 66]]\n",
      "[[34 73]\n",
      " [82 12]\n",
      " [53 66]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[34, 10, 73],\n",
       "       [82, 10, 12],\n",
       "       [53, 10, 66]])"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x= np.array([[34, 43,73],[82, 22, 12],[53, 94, 66]])\n",
    "print(x)\n",
    "x=np.delete(x,1,1)\n",
    "print(x)\n",
    "np.insert(x,1,10, axis =1)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1lIfmbQt_J_W"
   },
   "source": [
    "39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])\n",
    "\n",
    "\n",
    "---\n",
    "Find the dot product of the above two matrix\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {
    "id": "fV2-vXcR_vmu"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 28.  64.]\n",
      " [ 67. 181.]]\n"
     ]
    }
   ],
   "source": [
    "x = np.array([[1., 2., 3.], [4., 5., 6.]])\n",
    "y = np.array([[6., 23.], [-1, 7], [8, 9]])\n",
    "print(x.dot(y))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5U-4odUw_wP0"
   },
   "source": [
    "40. Generate a matrix of 20 random values and find its cumulative sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "id": "_oOHdiYEAF8N"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0550848435208104\n"
     ]
    }
   ],
   "source": [
    "x= np.random.randn(20)\n",
    "y=np.sum(x)\n",
    "print(y)"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "name": "Numpy-Assignment-PIAIC-Batch35-Q2.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}

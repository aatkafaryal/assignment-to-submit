{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reading Recipes \n",
    "\n",
    "Note: Data file is recipes.csv Attached with jupyter notebook"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "1. Start by importing NumPy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "#type your code here\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. All of Alize’s recipes call for milk, eggs, sugar, flour, and butter. For example, her cupcake recipe calls for:\n",
    "\n",
    "Flour Sugar Eggs Milk Butter 2 cups 0.75 cups 2 eggs 1 cups 0.5 cups Create a NumPy array that represents this data. Each element should be a number (i.e., 2 for “2 cups”). Save this array as cupcakes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2.  , 0.75, 2.  , 1.  , 0.5 ]])"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#type your code here\n",
    "\n",
    "cupcakes= np.array([[2, 0.75, 2, 1, 0.5]])\n",
    "\n",
    "np.save(\"cupk.npy\",cupcakes)\n",
    "np.load (\"cupk.npy\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Alize’s assistant has compiled all of her recipes into a csv (comma-separated variable) file called recipes.csv. Load this file into a variable called recipes.\n",
    "\n",
    "###########Explore yourselves how to load a csv file in numpy#######"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2.    0.75  2.    1.    0.5  ]\n",
      " [1.    0.125 1.    1.    0.125]\n",
      " [2.75  1.5   1.    0.    1.   ]\n",
      " [4.    0.5   2.    2.    0.5  ]]\n"
     ]
    }
   ],
   "source": [
    "from numpy import genfromtxt\n",
    "recipes = genfromtxt('recipes.csv', delimiter=',')\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4.Display recipes using print.\n",
    "Display recipes using print.\n",
    "\n",
    "\n",
    "Each row represents a different recipe. Each column represents a different ingredient.\n",
    "\n",
    "Recipe\t       Cups of Flour\tCups of Sugar\tEggs\tCups of Milk\tCups of Butter\n",
    "\n",
    "Cupcakes\t         …\t              …\t          …\t         …\t              …\n",
    "\n",
    "Pancake\t             …                …\t          …\t         …\t              …\n",
    "\n",
    "Cookie\t             …\t              …\t          …\t         …\t              …\n",
    "\n",
    "Bread\t             …\t              …\t          …\t         …\t              …"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2.    0.75  2.    1.    0.5  ]\n",
      " [1.    0.125 1.    1.    0.125]\n",
      " [2.75  1.5   1.    0.    1.   ]\n",
      " [4.    0.5   2.    2.    0.5  ]]\n"
     ]
    }
   ],
   "source": [
    "#type your code here\n",
    "print(recipes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5.The 3rd column represents the number of eggs that each recipe needs.\n",
    "\n",
    "Select all elements from the 3rd column and save them to the variable eggs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2.],\n",
       "       [1.],\n",
       "       [1.],\n",
       "       [2.]])"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#type your code here\n",
    "eggs= recipes[:,2:3]\n",
    "eggs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6.Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[False]\n",
      " [ True]\n",
      " [ True]\n",
      " [False]]\n"
     ]
    }
   ],
   "source": [
    "#type your code here\n",
    "print(eggs==1)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7.Alize is going to make 2 batches of cupcakes (1st row) and 1 batch of cookies (3rd row).\n",
    "\n",
    "You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2.75 1.5  1.   0.   1.  ]]\n"
     ]
    }
   ],
   "source": [
    "#type your code here\n",
    "cookies = recipes[2:3, :]\n",
    "print(cookies)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8.\n",
    "Get the number of ingredients for a double batch of cupcakes by using multiplication on cupcakes. Save your new variable to double_batch."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[4.  1.5 4.  2.  1. ]]\n"
     ]
    }
   ],
   "source": [
    "#type your code here\n",
    "double_batch = 2*cupcakes\n",
    "print(double_batch)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9.\n",
    "Create a new variable called grocery_list by adding cookies and double_batch."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2.75 1.5  1.   0.   1.  ]\n",
      " [4.   1.5  4.   2.   1.  ]]\n"
     ]
    }
   ],
   "source": [
    "#type your code here\n",
    "grocery_list= np.concatenate((cookies,double_batch))\n",
    "print(grocery_list)\n"
   ]
  }
 ],
 "metadata": {
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
 "nbformat_minor": 2
}

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# CrunchieMunchies\n",
    "\n",
    "You work in marketing for a food company <b>myCorps</b>, which is developing a new kind of tasty, wholesome cereal called <b>CrunchieMunchies</b>. \n",
    "\n",
    "You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you’ve dug up nutritional data on several different competitors.\n",
    "\n",
    "Your task is to use <em>NumPy statistical calculations</em> to analyze this data and prove that your <b>CrunchieMunchies</b> is the healthiest choice for consumers.\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task STEPS\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1.First, import numpy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# your code goes here\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.Look over the <b><em>cereal.csv</em></b> file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as <b><em>calorie_stats.</em></b>\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 70., 120.,  70.,  50., 110., 110., 110., 130.,  90.,  90., 120.,\n",
       "       110., 120., 110., 110., 110., 100., 110., 110., 110., 100., 110.,\n",
       "       100., 100., 110., 110., 100., 120., 120., 110., 100., 110., 100.,\n",
       "       110., 120., 120., 110., 110., 110., 140., 110., 100., 110., 100.,\n",
       "       150., 150., 160., 100., 120., 140.,  90., 130., 120., 100.,  50.,\n",
       "        50., 100., 100., 120., 100.,  90., 110., 110.,  80.,  90.,  90.,\n",
       "       110., 110.,  90., 110., 140., 100., 110., 110., 100., 100., 110.])"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# your code goes here\n",
    "from numpy import genfromtxt\n",
    "calorie_stats = genfromtxt('cereal.csv', delimiter=',')\n",
    "calorie_stats\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3.There are <em>60 calories per serving of CrunchieMunchies</em>. How much <b>higher</b> is the <b>average calorie count</b> of your competition?\n",
    "\n",
    "Save the answer to the variable <b>average_calories</b> and print the variable to the terminal to see the answer.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.961038961038961"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# your code goes here\n",
    "average_calories =np.mean(calorie_stats>60)\n",
    "average_calories\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4.Does the <b>average calorie count</b> adequately reflect the distribution of the dataset? Let’s sort the data and see.\n",
    "\n",
    "<b><em>Sort</em></b> the data and save the result to the variable <b>calorie_stats_sorted</b>. Print the sorted data to the terminal.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 50.,  50.,  50.,  70.,  70.,  80.,  90.,  90.,  90.,  90.,  90.,\n",
       "        90.,  90., 100., 100., 100., 100., 100., 100., 100., 100., 100.,\n",
       "       100., 100., 100., 100., 100., 100., 100., 100., 110., 110., 110.,\n",
       "       110., 110., 110., 110., 110., 110., 110., 110., 110., 110., 110.,\n",
       "       110., 110., 110., 110., 110., 110., 110., 110., 110., 110., 110.,\n",
       "       110., 110., 110., 110., 120., 120., 120., 120., 120., 120., 120.,\n",
       "       120., 120., 120., 130., 130., 140., 140., 140., 150., 150., 160.])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# your code goes here\n",
    "calorie_stats_sorted = np.sort(calorie_stats)\n",
    "calorie_stats_sorted\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5.Do you see what I’m seeing? Looks like <b><em>the majority of the cereals are higher than the mean</em></b>. Let’s see if the <b>median</b> is a better representative of the dataset.\n",
    "\n",
    "Calculate the median of the dataset and save your answer to <b><em >median_calories</em></b>. Print the median so you can see how it compares to the mean."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "110.0"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# your code goes here\n",
    "median_calories =np.median(calorie_stats_sorted)\n",
    "median_calories\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6.While the median demonstrates that <b><em><q>at least half of our values are over 100 calories</q></em></b>, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.\n",
    "\n",
    "<b>Calculate different percentiles</b> and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable <b>nth_percentile</b>.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "70.0\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "nth_percentile = np.percentile(calorie_stats,7)\n",
    "nth_percentile = np.percentile(calorie_stats,5)\n",
    "nth_percentile = np.percentile(calorie_stats,4)\n",
    "print(nth_percentile)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7.While the percentile shows us that<b><em><q>the majority of the competition has a much higher calorie count</q></em></b>, it’s an awkward concept to use in marketing materials.\n",
    "\n",
    "Instead, let’s calculate the percentage of cereals that <b><em><q>have more than 60 calories per serving</q></em></b>. Save your answer to the variable <b><em>more_calories</em></b> and print it to the terminal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "74\n",
      "77\n",
      "96.1038961038961\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "more_calories =calorie_stats[calorie_stats>60]\n",
    "\n",
    "print(np.size(more_calories))\n",
    "print(np.size(calorie_stats))\n",
    "percentage = np.size(more_calories)/ np.size(calorie_stats)\n",
    "\n",
    "print(percentage*100)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8.Wow! That’s a really high percentage. That’s going to be very useful when we promote CrunchieMunchies. But one question is, <b><em>how much variation exists in the dataset? </b></em></q>Can we make the generalization that most cereals have around 100 calories or is the spread even greater?\n",
    "\n",
    "Calculate the amount of variation by finding the <b><em>standard deviation</em</b> Save your answer to <b><em>calorie_std</em></b> and print to the terminal. How can we incorporate this value into our analysis?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19.35718533390827\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "calorie_std = calorie_stats.std()\n",
    "print(calorie_std)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9.Write a short paragraph that sums up your findings and how you think this data could be used to \n",
    "<b>myCorp’s</b> advantage when marketing CrunchieMunchies.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Through finding i can suggest the company that 96 percent ceraeals have more than 60 calories per serving. So we can promote this CrunchieMunchies by saying that it has more nutritional value than other brands and its calories per serving is very low as compare to others."
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

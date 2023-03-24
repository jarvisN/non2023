import numpy as np
import matplotlib.pyplot as plt

# get user input for number of trials and probability of success
n = int(input("Enter the number of trials: "))
P = int(input("Enter the probability of success: "))

p = P/100


# generate binomial distribution
binomial = np.random.binomial(n, p, size=1000)

# plot histogram of results
plt.hist(binomial, bins=np.arange(n+2)-0.5, density=True, rwidth=0.8)
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title(f'Binomial Distribution (n={n}, p={p})')
plt.show()

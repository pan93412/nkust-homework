import numpy as np
import matplotlib.pyplot as plt

# Generate data
Me = 0.5
mu, sigma = Me, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
s = s[s < Me] # keep only values less than Me

# Plot histogram
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt.axvline(x=Me, color='k', linestyle='--', linewidth=2)

# Show plot
plt.show()

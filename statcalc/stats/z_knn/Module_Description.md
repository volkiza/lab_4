
# Subpackage: z_knn

- The subpackage is inherited from stats package
- It has two modules calculating z_score and k-nearest neighbours 

## Module 1. z_score

### Functions:

"p_obs": function that outputs random integers with parameters 'n' and 'values'. 'n' is the size of the population and 'values' is the limit of dataset that a user wants to get.

"p_zscore": function that caculates z-score of population which is the number of standard deviations away from a mean for a data point. A z-score helps point out how unusual or usual a data point is from the other values. For this function, I used functions such as "s_mean" and "s_std" that were inherited from stats package. A user should input three parameters of which include 'x', 'n', and 'values'. 'x' is the score, 'n' is the size of the population and 'values' is the limit of dataset.

"p_se": function that calculates standard error of poupulation. For this fucntion, I used functions such as "s_std" that was inherited from stats package. A user should input three parameters of which include 'n' and 'values'. 'n' is the size of the population and 'values' is the limit of dataset that a user wants to get.

## Module 2. knn

### Functions:

"knn": function that outputs the mean of the most similar neighbors. A user should input three parameters of which include 'tr', 'te_row', 'n_neighbors'. 'tr' is the train data. 'te_row' is the testing rows. 'n_neighbors' is the number of neighbours. The function was designed to follow these steps:

#### Steps

1. It is locating the neighbors by calculating the distance between each record in the dataset which was already loaded from the distance module from stats package
2. With the calculated distances, the function sorts the records in the training
3. It will keep tracking each records as tuple and sort the lists by the descending order
4. Finally, it retursn the nearest neighbors and calculates the mean using s_mean function that was inherited from the stats packge

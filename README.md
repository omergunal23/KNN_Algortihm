# KNN_Algortihm
ELE489-Fundamentals of Machine Learning HW1

* knn.py file which includes k-NN implementataion code is also present in the analysis.ipynb file. So, no need to add it from the outside.
* The codes are written and tested in the Google Collab environment.

In this project, KNN algorithm is applied to the Wine Dataset from the UCI Machine Learning Repository.
The dataset consists of 178 instances with 13 numerical features and a class label (1, 2, or 3).
KNN algo. is tested with this dataset and value of K is observed with respect to accuracy for different distance metrics (Euclidean, Manhattan).
Finally, confusion matrix and classification report is provided to analyze the results. 

analysis.ipynb
1) Dataset is loaded which is taken from this website: https://archive.ics.uci.edu/dataset/109/wine. It doesn't contain feature names in the first row of the data so, it is added in the first part of the code by looking feature names from the given website and visualized some of the features.
2) Some data preprocessing steps are applied. There is no duplicate items in this dataset and by looking to feature's values, it is necessary to apply normalization on this dataset which is done in the next step.
3) Data normalization by using MinMaxScaler on entire dataset except for the 'class' label with 80%-20% train-test split. 
4) KNN algorithm from the knn.py file is runned and evalauted on the test data according to different distance metric. It is indicated in the for loop.
5) Visalization of Accuracy vs K.
6) Results.
7) By using cross validation technique, it is investigated that the results of KNN algorithm for the best k value can be improved as well. The results are not very different significantly.

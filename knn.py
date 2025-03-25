import numpy as np

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def manhattan_distance(x1, x2):
    return np.sum(np.abs(x1 - x2))

# For KNN algo: when a new test data comes, its distance is calculated with the train dataset which is in the memory
def knn_predict(X_train, y_train, X_test, k, distance_metric):
    distances = []
    for i, x_train in enumerate(X_train):
        if distance_metric == 'Euclidean':
            distance = euclidean_distance(X_test, x_train)
        elif distance_metric == 'Manhattan':
            distance = manhattan_distance(X_test, x_train)

        distances.append((distance, y_train[i])) # Test data point-Train data points distances with train datas classes to choose the kth nearest among them

    # Select the nearest k-neighbour
    distances.sort(key=lambda x: x[0])
    k_neighbors = []
    for i in range(k):
        distance, label = distances[i]
        k_neighbors.append(label)

    # Most one among the k-neighbour
    return max(k_neighbors, key=k_neighbors.count)
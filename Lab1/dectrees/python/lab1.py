from tabulate import tabulate
import dtree as d
import monkdata as m


monk_datasets = [m.monk1, m.monk2, m.monk3]
monk_test_datasets = [m.monk1test, m.monk2test, m.monk3test]
dataset_names = ["MONK-1", "MONK-2", "MONK-3"]


# Assignment 1
def assignment1():
    table_data = []
    i = 0
    for dataset in monk_datasets:
        table_data.append([dataset_names[i], d.entropy(dataset)])
        i += 1
    headers = ["Dataset", "Entropy"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# Assignment 3
def assignment3():
    
    table_data = []
    i = 0
    for dataset in monk_datasets:
        information_gains = [d.averageGain(monk_datasets[i], attribute) for attribute in m.attributes]
        
        table_data.append([dataset_names[i]] + information_gains)
        i += 1

    # Print the table using tabulate
    headers = ["Dataset", "a1", "a2", "a3", "a4", "a5", "a6"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))



# Assignment 5

def assignment5():

    table_data = []
    i = 0
    for _ in monk_datasets:
        t = d.buildTree(monk_datasets[i], m.attributes)
        table_data.append([dataset_names[i], d.check(t, monk_datasets[i]), d.check(t, monk_test_datasets[i])])
        i += 1
    headers = ["Dataset", "E-train", "E-test"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


import random
import numpy as np
import matplotlib.pyplot as plt
import monkdata as m
import dtree as d

def partition(data, fraction):
    """
    Partition the dataset into training and validation sets based on the given fraction.
    """
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

# Load the datasets
monk1 = m.monk1
monk3 = m.monk3

def prune_trees(data, test_data, num_runs=1000):
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    mean_errors = []
    std_errors = []

    # For each fraction, we will collect errors across num_runs
    for frac in fractions:
        errors = []  # To store errors for each run
        for i in range(num_runs):
            # Partition the data into training and validation sets
            train, validation = partition(data, frac)
            # Build the tree
            tree = d.buildTree(train, m.attributes)
            # Prune the tree
            pruned_tree = d.allPruned(tree)
            # Check the performance of the tree on the validation
            best_performance = d.check(tree, validation)

            tree_best = tree
            # Find the best pruned tree
            for t in pruned_tree:
                temp_performance = d.check(t, validation)
                if temp_performance > best_performance:
                    best_performance = temp_performance
                    tree_best = t
            # Add the best pruned tree's error on the test set
            errors.append(1 - d.check(tree_best, test_data))
        
        # Calculate the mean error for this fraction
        mean_errors.append(np.mean(errors))
        std_errors.append(np.std(errors))

    return fractions, mean_errors, std_errors

def assignment7():
    # Run for monk1 dataset
    fractions, mean_errors_monk1, std_errors_monk1 = prune_trees(monk1, m.monk1test, num_runs=1000)
    # Run for monk3 dataset
    fractions, mean_errors_monk3, std_errors_monk3 = prune_trees(monk3, m.monk3test, num_runs=1000)

    # Plot for monk1
    plt.plot(fractions, mean_errors_monk1, marker='o', label='MONK1')
    # Plot for monk3
    plt.plot(fractions, mean_errors_monk3, marker='o', label='MONK3')

    plt.xlabel('Fraction of Training Data')
    plt.ylabel('Mean Error')
    plt.title('Pruning Performance vs Fraction of Training Data')
    plt.legend()
    plt.grid(True)
    plt.show()

        # Plot standard deviations for monk1 and monk3
    plt.figure(figsize=(10, 5))
    plt.plot(fractions, std_errors_monk1, marker='o', label='MONK1 Std Error')
    plt.plot(fractions, std_errors_monk3, marker='o', label='MONK3 Std Error')

    plt.xlabel('Fraction of Training Data')
    plt.ylabel('Standard Deviation of Error')
    plt.title('Pruning Performance vs Fraction of Training Data (Standard Deviation)')
    plt.legend()
    plt.grid(True)
    plt.show()

    

def main():
    # Assignment 1
    # assignment1()  # Commented since not relevant here

    # Assignment 3
    # assignment3()  # Commented since not relevant here

    # Assignment 5
    # assignment5()  # Commented since not relevant here

    # Assignment 7
    assignment7()

# Call main
if __name__ == '__main__':
    main()

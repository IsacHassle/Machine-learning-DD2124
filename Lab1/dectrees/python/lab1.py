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
        information_gains = [d.averageGain(dataset, attribute) for attribute in m.attributes]
        
        table_data.append([dataset_names[i]] + information_gains)
        i += 1

    # Print the table using tabulate
    headers = ["Dataset", "a1", "a2", "a3", "a4", "a5", "a6"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))



# Assignment 5

def assignment5():

    table_data = []
    i = 0
    for dataset in monk_datasets:
        t = d.buildTree(monk_datasets[i], m.attributes)
        table_data.append([dataset_names[i], d.check(t, monk_datasets[i]), d.check(t, monk_test_datasets[i])])
        i += 1
    headers = ["Dataset", "E-train", "E-test"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# Assignment 7


def main():
    # Assignment 1
    assignment1()

    # Assignment 3
    assignment3()

    # Assignment 5
    assignment5()

if __name__ == "__main__":
    main()

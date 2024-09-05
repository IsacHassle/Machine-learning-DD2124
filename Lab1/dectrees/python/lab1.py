import dtree as d
import monkdata as m


# Assignment 1

monk_datasets = [m.monk1, m.monk2, m.monk3]
dataset_names = ["MONK-1", "MONK-2", "MONK-3"]

i = 0
for dataset in monk_datasets:
    entropy_value = d.entropy(dataset)
    print(f"Entropy of {dataset_names[i]}: {entropy_value}")
    i += 1

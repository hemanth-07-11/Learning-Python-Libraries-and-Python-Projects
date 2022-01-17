from collections import Counter
from pprint import pprint
import pandas as pd
import math

def entropy(probabilities):
    return sum([-probability * math.log(probability, 2) for probability in probabilities])

def entropy_of_list(a_list):
    cnt = Counter(x for x in a_list)
    num_instances = len(a_list)
    probabilities = [x / num_instances for x in cnt.values()]
    return entropy(probabilities)

def information_gain(dataset, split_attribute_name, target_attribute_name):
    dataset_split = dataset.groupby(split_attribute_name)
    nobs = len(dataset.index)
    df_agg_ent = dataset_split.agg({target_attribute_name: [entropy_of_list, lambda x: len(x) / nobs]})[
        target_attribute_name]
    df_agg_ent.columns = ['Entropy', 'PropObservations']
    new_entropy = sum(df_agg_ent['Entropy'] * df_agg_ent['PropObservations'])
    old_entropy = entropy_of_list(dataset[target_attribute_name])
    return old_entropy - new_entropy


def id3(dataset, target_attribute, attribute_names, default_class=None):
    cnt = Counter(x for x in dataset[target_attribute])
    if len(cnt) == 1:
        return list(cnt.keys())[0]
    elif dataset.empty or (not attribute_names):
        return default_class
    else:

        default_class = cnt.most_common()[0][0]
        gains = [information_gain(dataset, attribute, target_attribute) for attribute in attribute_names]
        best_attr = attribute_names[gains.index(max(gains))]

        tree = {best_attr: {}}
        remaining_attribute_names = [i for i in attribute_names if i !=
                                     best_attr]
        for attr_val, data_subset in dataset.groupby(best_attr):
            subtree = id3(data_subset, target_attribute,
                          remaining_attribute_names, default_class)
            tree[best_attr][attr_val] = subtree
    return tree


def classify(instance, tree, default=None):
    attribute = next(iter(tree))
    if instance[attribute] in tree[attribute].keys():
        result = tree[attribute][instance[attribute]]
        if isinstance(result, dict):
            return classify(instance, result)
        return result
    return default

def main():
    dataset = pd.read_csv('dec_tree_id3.csv')

    print(dataset)
    attribute_names = list(dataset.columns)
    attribute_names.remove('PlayTennis')

    tree = id3(dataset, 'PlayTennis', attribute_names)
    print("The Resultant Decision Tree is :")
    pprint(tree)
    dataset['predicted'] = 0
    for i in range(len(dataset)):
        dataset.loc[i, 'predicted'] = classify(dataset.loc[i], tree)

    print(dataset)
    count = 0
    for i in range(len(dataset)):
        if dataset['PlayTennis'][i] == dataset['predicted'][i]:
            count += 1
    print('Accuracy is : ', count / len(dataset) * 100)
    dataset.drop(['predicted'], axis=1, inplace=True)

    training_data = dataset.iloc[1:-4]
    test_data = dataset.iloc[-4:]

    training_data = training_data.reset_index(drop=True)
    test_data = test_data.reset_index(drop=True)

    train_tree = id3(training_data, 'PlayTennis', attribute_names)
    print("The Resultant Decision Tree for Training Data is :")

    pprint(train_tree)
    for i in range(len(test_data)):
        test_data.loc[i, 'predicted'] = classify(test_data.loc[i], train_tree)

    count = 0
    for i in range(len(test_data)):
        if test_data['PlayTennis'][i] == test_data['predicted'][i]:
            count += 1
    print('Accuracy is : ', count / len(test_data) * 100)
main()


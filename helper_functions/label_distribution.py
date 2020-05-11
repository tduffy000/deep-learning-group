import os
import numpy as np

def is_image_file(filename):
    """
    :param filename:
    :type str:
    :return: If the file is an image.
    :rtype: bool
    """
    return filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.jpg')

def get_label_distribution(root):
    """
    :param root:
    :type root: str
    :return: A dictionary mapping each label to the count of images associated with it.
    :rtype: dict(label -> count)
    """
    labels = {}
    irrelevant_files = ['__MACOSX','dataset','pose_dataset']
    for f in os.walk(root):
        path, subdirs, contents = f
        label = path.split('/')[-1]
        if label not in irrelevant_files:
            labels[label] = labels.get(label, 0) + len(list(filter(is_image_file, contents)))
    return labels

def get_label_priors(label_counts):
    """
    :param label_counts: A dict mapping possible labels to their counts.
    :type label_counts: int
    :return: A random prediction just based on P(y).
    :rtype: str
    """
    total = sum([ x for x in label_counts.values() ])
    return { label: count / total for label, count in label_counts.items() }

class RandomPredictor:
    """
    A dummy model which just makes predictions based on the class prior, P(y) of a label.
    """

    def __init__(self, label_priors):
        self.label_priors = label_priors

    def predict(self):
        return np.random.choice(list(self.label_priors.keys()), replace=True, p=list(self.label_priors.values()))

import os
import scipy.io
import json
import numpy as np


def new_name(file):
    return f'{str(file).split(".")[0]}.json'


def read_directory(directory='data/', save=True):
    indirectory = os.path.join(directory, 'in')

    collections_dataset = []

    for file in os.listdir(indirectory):
        if file.endswith(".mat"):
            filename = os.path.join(indirectory, str(file))
            mat = scipy.io.loadmat(filename)

            dataset = mat.get('av_subs')
            collections_dataset.append(dataset)

            if save is True:
                outpath = os.path.join(directory, 'out', new_name(file))

                listified = dataset.tolist()

                with open(outpath, 'w') as outfile:
                    json.dump(listified, outfile)

                    print('Saved in ', outpath)

    return collections_dataset


if __name__ == '__main__':
    dataset_collection = read_directory(save=False)

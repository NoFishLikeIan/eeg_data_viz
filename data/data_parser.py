import os
import scipy.io
import json


def new_name(file):
    return f'{str(file).split(".")[0]}.json'


def read_directory(directory='data/'):
    indirectory = os.path.join(directory, 'in')

    for file in os.listdir(indirectory):
        if file.endswith(".mat"):
            filename = os.path.join(indirectory, str(file))
            mat = scipy.io.loadmat(filename)

            outpath = os.path.join(directory, 'out', new_name(file))
            listified = mat.get('av_subs').tolist()

            with open(outpath, 'w') as outfile:
                json.dump(listified, outfile)

                print('Saved in ', outpath)


if __name__ == '__main__':
    read_directory()

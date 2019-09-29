import tarfile


def extract(filename):
    print('Extracting {}...'.format(filename))
    tar = tarfile.open(filename, 'r')
    tar.extractall('data')
    tar.close()


if __name__ == "__main__":
    extract('data/data_thchs30.tgz')

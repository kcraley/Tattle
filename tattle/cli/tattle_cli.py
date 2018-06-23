"""
Usage:
    tattle tell [(--respository <repository>)]
    tattle config new []
    tattle config show [--location]
    tattle -h | --help
    tattle -v | --version

Options:
    -h --help       Show this help dialog.
    -v --version    Show version.
    -

"""

from docopt import docopt
import tattle

def main():
    args = docopt(__doc__, version='Tattle {version}'.format(version=tattle.__version__))



if __name__ == '__main__':
    main()

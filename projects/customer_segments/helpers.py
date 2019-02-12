import numpy as np
import pandas as pd
from time import time
from IPython.display import display, HTML # Allows the use of display() for DataFrames
import seaborn as sns
# Import supplementary visualization code visuals.py
import visuals as vs
import matplotlib.pyplot as plt
import warnings

# Section for helper functions
def display_html(display_string: str, color: str = 'blue', heading_value: str = 'h4'):
    """
    Display some text in HTML form inside the display sections
    """
    display(HTML(' <span style="color:{0}"><{2}>{1}</{2}> </span>  '.format(color, display_string, heading_value)))


def print_general_information(title: str, data):
    """
    Display general information related to data
    """
    display_html('Display basic information about the records "{}":'.format(title))
    # Success - Display the first record
    display(data.head(n=5))
    display(data.info())
    print("Get an overview of the data before we proceed:")
    display(data.describe())
    display_html('Checking the shape of the data:')
    display(data.shape)


def display_pair_plot(title: str, data):
    """
    Display pairplot
    """
    display_html('Pairplot "{}":'.format(title))
    sns.pairplot(data)
    plt.show()
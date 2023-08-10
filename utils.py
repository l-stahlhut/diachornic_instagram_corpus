"""Helper functions"""

from collections import OrderedDict
import os

def add_item_to_dictionary(dictionary, key, value):
    new_dictionary = OrderedDict()
    new_dictionary[key] = value
    for k, v in dictionary.items():
        new_dictionary[k] = v
    return new_dictionary

def get_folder_names(dir):
    """Return all folder names in root directory in order to return a list of account names.
    Adjust path if data is not located on the same level/in the same place as this code."""
    blacklist = ['.idea', '__pycache__']
    folder_names = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name)) if name not in blacklist]
    return folder_names
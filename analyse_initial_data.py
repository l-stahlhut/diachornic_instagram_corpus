"""
Carry out some initial data analysis on the greedily scraped instagram posts in order to identify relevant
posts for the final corpus.
Adjust paths in main function if necessary.
"""

import csv
import os
from account import Account
from utils import add_item_to_dictionary, get_folder_names

def get_accounts_info(data_path):
    """Returns a list of dictionaries with some information on each account."""
    accounts = get_folder_names(data_path)
    account_info = []
    for a in accounts:
        try:
            d = {}
            A = Account(a)
            d['name'] = A.name
            d['n_posts'] = A.n_posts
            d['mean_post_len'] = A.mean_post_len
            d['earliest_date'] = A.earliest_date
            d['latest_date'] = A.latest_date
            account_info.append(d)
        except FileNotFoundError:
            pass
    return account_info


def get_posts_info(data_path):
    """
    Returns a list of dictionaries with the text and some info on each post such as:
    account name, post name, post date, text, term in text, post len
    """
    accounts = get_folder_names(data_path)
    post_info = []
    for a in accounts:
        try:
            A = Account(a)
            account_dict = {'account': A.name}
            for post in A.posts:
                post.update(account_dict) # add account name
                # re-order keys
                new_dict = {'account': post['account']}
                for key, value in post.items():
                    if key != 'account':
                        new_dict[key] = value
                post_info.append(new_dict)

        except FileNotFoundError:
            pass
    return post_info


def posts_to_csv(data_path, analysis_path, filename):
    """For the initial corpus, there is no difference but for the smaller subcorpora there is a path difference"""
    keys = get_posts_info(data_path)[0].keys()

    with open(os.path.join(analysis_path, filename), 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(get_posts_info(data_path))


def accounts_to_csv(data_path, analysis_path, filename):
    """For the initial corpus, there is no difference but for the smaller subcorpora there is a path difference"""
    keys = get_accounts_info(data_path)[0].keys()

    with open(os.path.join(analysis_path, filename), 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(get_accounts_info(data_path))


def main():
    # target path for analysis files
    if not os.path.exists('./analysis_all_data'):
        os.makedirs('./analysis_all_data')
    target_path = './analysis_all_data'
    # path to data of greedily collected instagram posts (containing one sub-folder per account)
    data_path = '/Users/laurastahlhut/projects/InstaKorpus_diachron'

    # create csv with info on accounts
    accounts_to_csv(data_path, target_path, "all_accounts_info.csv")
    # create csv with info on posts
    posts_to_csv(data_path, target_path, "all_posts_info.csv")


if __name__ == '__main__':
    main()
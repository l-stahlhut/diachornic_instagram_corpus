"""Grab all posts of an account, caluclate post length in n words and identify whether some search term occurs in any given
post.
Furthermore, calculate number of posts as well as earliest and latest date the account has
published a post and mean post length in number of words."""
import os
from datetime import datetime

# Gesamtkorpus: 1200 Posts
# Subkorpus 1: 2020 - 2023 (grösstenteils bereits analysierte darin enthalten)
# Subkorpus 2: 2013/14 - ... (4 Jahre)

class Account():
    def __init__(self, account_name):
        self.name = account_name
        self.posts = self.get_posts()
        self.n_posts = len(self.get_posts())
        self.mean_post_len = self.calculate_mean_length()
        self.earliest_date = self.get_earliest_latest_dates()[0]
        self.latest_date = self.get_earliest_latest_dates()[1]


    def get_posts(self):
        """posts = [
            {name: name, date: date, text: text, text_len}
        ]"""
        posts = []
        for root, dirs, files in os.walk(self.name):

            for file in files:
                if file.endswith(".txt"):
                    d = {}
                    d['post_name'] = file
                    d['date'] = file.split('_')[0]
                    d['text'] = self.get_text(os.path.join(self.name, file))
                    # TODO predefine search terms
                    terms = ['körper', 'body', 'health', 'sport', 'fit', 'schlank', 'sportlich',
                             'kraft', 'arm', 'bein', 'dehnungsstreifen', 'bauch', 'po', 'nase', 'kinn', 'augen', 'haut',
                             'haar', 'haare', 'schminken', 'geschminkt', 'ungeschminkt', 'ohren', 'augenbrauen', 'stirn',
                             'kinn', 'wangen', 'hals', 'brust', 'brüste', 'busen', 'arm', 'arme', 'muttermal', 'unsicher',
                             'komplex', 'komplexe', 'unwohl', 'hübsch', 'schön', 'normal', 'selbstbewusst', 'selbstbewusstsein',
                             'pickel', 'unreinheiten', 'dick', 'dünn', 'schlank', 'schlanker', 'abnehmen', 'abgenommen',
                             'zugenommen', 'zunehmen', 'hässlich', 'gewicht', 'mehrgewicht', 'übergewicht',
                             'abnahme', 'zunahme', 'wassereinlagerungen', 'transformation', 'veränderung', 'verändern']
                    d["term_in_text "] = self.check_strings_in_text(terms, d['text'])
                    d['post length (n words)'] = len(d['text'].split(' '))
                    posts.append(d)

        return posts

    def get_text(self, file):
        with open(file) as infile:
            lines = infile.readlines()
            lines = [l.rstrip() for l in lines]

            return ' '.join(lines)

    def check_strings_in_text(self, strings, text):
        for term in strings:
            if term in text.lower():
                return True
        return False

    def get_earliest_latest_dates(self):
        try:
            dates = [datetime.strptime(entry['date'], '%Y-%m-%d') for entry in self.posts]
            earliest_date = min(dates).strftime('%Y-%m-%d')
            latest_date = max(dates).strftime('%Y-%m-%d')
            return earliest_date, latest_date
        except ValueError:
            return 'NA', 'NA'

    def calculate_mean_length(self):
        total_length = 0
        count = 0

        for entry in self.posts:
            if 'post length (n words)' in entry:
                length = entry['post length (n words)']
                total_length += length
                count += 1

        if count > 0:
            mean_length = total_length / count
            return round(mean_length, 2)
        else:
            return 0  # or any other value indicating no valid data


#
A = Account('alexa_katharina')
#
# print(A.posts)
# print("Number of posts for alexa_katharine: ", A.n_posts)
# print("Earliest date to post: ", A.earliest_date)
# print("Mean post length: ", A.mean_post_len)

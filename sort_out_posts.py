"""
Selection of posts for the two sub-corpora.
- 600 posts for subcorpus 2 and
- 211 posts for subcorpus 1
The posts contain a certain search term which can be changed below and are otherwise chosen randomly from all available
posts.
Adjust paths in main function if necessary.
"""
import os
import random
import shutil

def get_folder_names(dir):
    blacklist = ['.idea', '__pycache__']
    folder_names = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name)) if name not in blacklist]
    return folder_names

def get_file_names(folder_path, years):
    """list of txt files contained within folder that contain the search term
    threshold = number of posts to take from each folder"""
    # get list of available posts
    txt_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            txt_files.append(file_name)
    # check for search term
    candidate_files = []
    terms = ['körper', 'body', 'health', 'sport', 'fit', 'schlank', 'thin', 'lean', 'sportlich', 'sportive',
             'trainiert', 'shredded',
             'figur', 'weight', 'weightloss', 'diät', 'diet',
             'arm', 'bein', 'leg', 'dehnungsstreifen', 'stretch marks', 'bauch', 'belly', 'tummy',
             'po', 'butt', 'nase', 'nose', 'kinn', 'chin', 'haut', 'skin',
             'haar', 'haare', 'hair', 'schminken', 'make-up', 'makeup', 'geschminkt', 'ungeschminkt', 'augenbrauen', 'stirn', 'cheeks', 'wangen', 'neck', 'hals', 'breast', 'boobs', 'boob',
             'brust', 'brüste', 'busen', 'muttermal', 'mole',
             'komplex', 'komplexe', 'unwohl', 'hübsch', 'selbstbewusst',
             'selbstbewusstsein', 'confident', 'confidence', 'self-secure','selbstsicher',
             'pickel', 'unreinheiten', 'dick', 'thick', 'fat', 'overweight', 'thin', 'skinny', 'dünn', 'schlank',
             'schlanker', 'abnehmen', 'abgenommen', 'weight', 'waage', 'scale',
             'zugenommen', 'zunehmen', 'hässlich', 'ugly', 'gewicht', 'mehrgewicht', 'übergewicht',
             'abnahme', 'zunahme', 'wassereinlagerungen', 'transformation', 'veränderung', 'verändern', 'aussehen',
             'äusserlichkeit', 'äusserlichkeiten']

    for f in txt_files:
        with open(os.path.join(folder_path, f), 'r') as infile:
            lines = infile.readlines()
            lines = ' '.join([l.rstrip() for l in lines])
            if f[0:4] in years:
                if is_word_in_string(terms, lines) is True:
                    candidate_files.append(folder_path + "/" + f)

    return candidate_files


def get_random_strings(string_list, num_strings=5):
    return random.sample(string_list, num_strings)


def is_word_in_string(word_list, target_string):
    for word in word_list:
        if word in target_string.lower().split():
            return True
    return False


def rename_file(account, old_name):
    """Change name to match naming pattern of previously downloaded posts.
    'endlich_zufrieden/2023-05-06_14-46-45_UTC.txt' -> 'endlich_zufrieden_050623.txt'"""
    year, day, month = old_name[2:4], old_name[5:7], old_name[8:10]
    new_name = account + "_" + day + month + year + '.txt'
    return new_name


def chose_posts(years, threshold):
    """chose posts for a subcorpus form all accounts
    years is 2023 for extension of subcorpus 1 and 2013-2016 for subcorpus 2
    threshold is ca. 5 for subcorpus 1 (i need 211 posts) and ca. 13 for subcorpus 2 (i need 600 posts)
    """
    all_chosen_files = []
    for account in get_folder_names('.'):
        chosen_files = get_file_names(account, years)
        for f in chosen_files:
            all_chosen_files.append(f)

    sample = get_random_strings(all_chosen_files, num_strings=threshold)

    return sample


def copy_txt_files(source_folder, destination_folder, file_names_list):
    """Save the chosen files from a given subcorpus and rename the files"""
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for source_file_path in file_names_list:
        if source_file_path.endswith('.txt'):
            source_file_name = os.path.basename(source_file_path)
            destination_subfolder, file_name = os.path.split(source_file_name)
            new_file_name = rename_file(destination_subfolder, file_name)
            account = source_file_path.split('/')[0]
            destination_path = os.path.join(destination_folder, account + new_file_name)

            shutil.copy2(os.path.join(source_folder, source_file_path), destination_path)


def filenames_to_file(path, corpus, filenames):
    """Write the list of chosen filenames to a txt file"""
    with open(os.path.join(path, corpus + "_chosen_files.txt"), "w") as outfile:
        for i in filenames:
            outfile.write(i + "\n")


def main():

    # target path
    target_path = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten'
    # subkorpus 2: 2013-2015
    path_subcorpus2 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/Subkorpus1_2013_2014_2015_2016'
    # subkorpus 1: 2013-2015
    path_subcorpus1 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/Subkorpus2_2020_2021_2022_2023'

    # chose posts for the extension of subcorpus 1 (211 more posts)
    #print("subcorpus 1: ", len(chose_posts(['2023'], 220)))
    #print("subcorpus 2: ", len(chose_posts(['2013', '2014', '2015', '2016'], 418)))

    posts_subcorpus1 = chose_posts(['2023'], 38)
    print("subcorpus 1 : ", len(posts_subcorpus1))
    filenames_to_file(target_path, "subcorpus1", posts_subcorpus1)  # write txt files in order to get images later

    # chose posts for subcorpus 2 (600 posts)
    posts_subcorpus2 = chose_posts(['2013', '2014', '2015', '2016'], 418)
    print("subcorpus 2 : ", len(posts_subcorpus2))
    # print(posts_subcorpus2)
    filenames_to_file(target_path, "subcorpus2", posts_subcorpus2)  # write filenames to txt file

    # copy paste files to make corpora
    copy_txt_files('.', path_subcorpus1, posts_subcorpus1)
    copy_txt_files('.', path_subcorpus2, posts_subcorpus2)


if __name__ == '__main__':
    main()
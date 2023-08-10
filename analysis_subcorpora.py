import os
import csv

def get_file_names(folder_path):
    """list of txt files contained within folder """
    # get list of available posts
    txt_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            txt_files.append(file_name)
    return txt_files

def merge_txt_files(folder_path, outpath, outfile_name):
    """Write content from all txt files within a folder to one txt-file
    excluding account names."""
    with open(os.path.join(outpath, outfile_name), 'w') as output_file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as input_file:
                    content = input_file.read()
                    output_file.write(content)
                    output_file.write('\n')  # Separate content from different sources with a line break

def merge_txt_files_with_account(folder_path, outpath, outfile_name):
    """Write content from all txt files within a folder to one txt-file
        including account names."""
    with open(os.path.join(outpath, outfile_name), 'w') as output_file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as input_file:
                    content = input_file.read()
                    output_file.write(filename + '\n\n')
                    output_file.write(content)
                    output_file.write('\n-------------------------\n\n')
                    output_file.write('\n')  # Separate content from different sources with a line break

def get_post_length(post):
    """Get post length in n char and n words"""
    n_char = len(post)
    n_words = len(post.split())
    return n_char, n_words

def write_info_file(folder_path, outpath,outfile_name):
    """Write info file for subcorpus with name of account, date, and post length."""
    with open(os.path.join(outpath, outfile_name), 'w', encoding='UTF8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["post", "account", "date", "year", "n_char", "n_words"])

        for filename in get_file_names(folder_path):
            account = filename.rstrip('txt')[:-8]
            date = filename.rstrip('.txt')[-6:]
            year = filename.rstrip('.txt')[-2:]
            with open(os.path.join(folder_path, filename), 'r') as infile:
                l = infile.read()
                n_char, n_words = get_post_length(l)

            writer.writerow([filename, account, date, year, n_char, n_words])

def main():
    # paths containing the data (adjust if necessary)
    path_subcorpora = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten'
    path_subcorpus1 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/Subkorpus1_2013_2014_2015_2016'
    path_subcorpus2_old = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/Subkorpus2_alt'
    path_subcorpus2 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/Subkorpus2_2020_2021_2022_2023'

    #  write a csv file for each subcorpus that contains one post per line
    write_info_file(path_subcorpus1, 'analysis_subcorpora', 'posts_info_subcorpus1.csv')
    write_info_file(path_subcorpus2, 'analysis_subcorpora', 'posts_info_subcorpus2.csv')
    # this is for some data we already had previously
    write_info_file(path_subcorpus2_old, 'analysis_subcorpora', 'posts_info_subcorpus2_old.csv')

    # merge txt files of a subcorpus into a joined txt file INCL account names (optional take the function without
    # account names in order to count total words)
    merge_txt_files_with_account(path_subcorpus1, "analysis_subcorpora", "subcorpus1_all_texts_with_account_names.txt")
    merge_txt_files_with_account(path_subcorpus2, "analysis_subcorpora", "subcorpus2_all_texts_with_account_names.txt")


if __name__ == '__main__':
    main()
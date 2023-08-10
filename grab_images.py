"""
Copy-paste some jpeg-files.
I have a list of txt files and want to grab all the corresponding jpeg files.

"""
import shutil
import os
import re

# lists with filenames of txt files (we want the corresponding jpg files)
path_files_sc1 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/subcorpus1_chosen_files.txt'
path_files_sc2 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/subcorpus2_chosen_files.txt'

inpath = '/Users/laurastahlhut/projects/InstaKorpus_diachron'
outpath1 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/Subkorpus1_2013_2014_2015_2016'
outpath2 = '/Users/laurastahlhut/Documents/Jobs/HA_Marie/IG_Korpus_Diachron/Daten/Subkorpus2_2020_2021_2022_2023'


def replace_suffix(filename, old_suffix, new_suffix):
    if filename.endswith(old_suffix):
        return filename[:-len(old_suffix)] + new_suffix
    else:
        return filename


def copy_files(source_filenames, destination_path):
    for source_filename in source_filenames:
        print(source_filename)
        #destination_filename = re.findall(r'[^\/]*.jpg+$', source_filename)[0]  # without source path
        destination_filename = extract_desired_string(source_filename)
        # print(destination_filename)
        destination_filename_full = destination_path + "/" + destination_filename
        print(destination_filename_full)
        try:
            shutil.copy(source_filename, destination_filename_full)
        except FileNotFoundError:
            destination_filename_full = destination_filename_full.rstrip('.jpg') + '_01.jpg'
        print(f"File {source_filename} copied to {destination_filename_full}")


def extract_desired_string(input_string):
    match = re.search(r"/([^/]+)/(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-\d{2}_UTC\.jpg$", input_string)
    # return match
    if match:
        username = match.group(1)
        year = match.group(2)
        month = match.group(3)
        day = match.group(4)
        time = match.group(5) + match.group(6)

        return f"{username}_{month}{day}{year[2:]}.jpg"
    else:
        return None

def main():
    # input_string = "/Users/laurastahlhut/projects/InstaKorpus_diachron/anjazeidler/2023-02-14_08-49-24_UTC.jpg"
    # desired_output = extract_desired_string(input_string)
    # print(desired_output)
    input_file = path_files_sc2  # TODO Update this with your input file's name
    old_suffix = ".txt"
    new_suffix = ".jpg"
    destination_path = outpath2  # TODO Update this with the destination folder's path

    try:
        with open(input_file, "r") as file:
            filenames = [os.path.join(inpath, line.strip()) for line in file.readlines()]

        jpg_filenames = [replace_suffix(filename, old_suffix, new_suffix) for filename in filenames] # source paths

        copy_files(jpg_filenames, destination_path)

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()

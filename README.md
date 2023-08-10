# Diachronic Instagram Corpus

This repo creates a diachronic corpus of instagram posts surrounding the topic of body positivity. 
The corpus was created for an analysis of how language use on the platform and within the domain has changed over 
time. Subcorpus 1 contains posts from 2013-2016, Subcorpus 2 contains posts from 2020-2023.

## Scraping Data
Relevant accounts have been identified manually depending on whether they frequently use certain hashtags 
(e.g.#bodypositivity) and data has been greedily scraped using the [Instaloader](https://instaloader.github.io) Library. <br>
This creates the following folder structure: 
```
InstagramKorpus
|-- account1
|   |-- 2019-01-19_18-09-59_UTC.jpg
|   |-- 2019-01-19_18-09-59_UTC.txt
|   |-- 2019-01-21_13-36-08_UTC.jpg
|   |-- 2019-01-21_13-36-08_UTC.txt
|   |-- ...
|-- account2
|   |-- 2013-02-04_13-22-26_UTC.jpg
|   |-- 2013-02-04_13-22-26_UTC.txt
|   |-- ...
|-- ...
```
Corresponding txt and jpg files can be identified using the date and time stamps.

## Initial Analysis of all data
After initial scraping, some basic analysis can be carried out with: 
```
python3 analyse_initial_data.py
```
This creates two csv-files within the folder `analysis_all_data`: 
* `all_accounts_info.csv`: One account per line with number of posts, mean post length (n words) and earliest/latest 
date of posting.
* `all_posts_info.csv`: One post per line with account and post_name, date, text, post length (n words)post length 
(n words), and an indication of whether or not it contains any relevant search term belonging to some domain.
Search terms can be changed in `account.py`.

##  Selection of relevant data for sub-corpora
The sub-selection of the two sub-corpora is done by running:
```
python3 sort_out_posts.py
```
! Only run this code once since it overwrites the corpus with another subset of posts if it is run multiple times.! <br>
This picks a random sample of 600 posts for subcorpus 2 and 211 posts for subcorpus 1 that belong to the correct time 
period and contain any search term in a predefined list which can be adjusted in the code. The txt-files of the selected 
posts are copy-pasted to a target folder specified in the main function. Files are re-named to match the naming scheme of 
previously downloaded posts. The folder structure is as follows: 
```
Subkorpora
|-- Subkorpus1_2013_2014_2015_2016
|   |-- anjazeidler_012716.txt
|   |-- angeliquelini_022616.txt
|   |-- charlotte_weise_010616.txt
|   |-- ...
|-- Subkorpus2_2020_2021_2022_2023
|   |-- ...
```
This also creates the files `subcorpus1_chosen_files.txt` and `subcorpus2_chosen_files.txt` which each contain a list of 
filenames that have been copy-pasted. This will be needed to select the corresponding jpg files.

## Analysis of selected subcorpora
To perform a basic analysis of the selected subcorpora, run: 
```
python3 analysis_subcorpora.py
```
This creates some csv files with info on the selected files. Use this to determine whether the selection
process using the search terms has been successful. Change search terms and re-create the corpus otherwise.
If you're happy with the choice of posts, you can download the corresponding images.
The code above also creates one txt-file per subcorpus containing the texts of all posts of a subcorpus.

## Selection of the corresponding images
To select and copy-paste the corresponding images to the same directory, run this code: 
```
python3 grab_images.py
```



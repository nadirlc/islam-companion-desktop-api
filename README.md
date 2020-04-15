![Islam Companion Desktop API](https://pakjiddat.netlify.com/static/7f2d195ad7c772ec2e7065e946722dff/f8915/islamcompanion-desktop-api.png)

### Introduction

The "**Islam Companion Desktop API**" project is a API (Application Programming Interface) written in [Python](https://www.python.org/) language, that allows users to add Holy Quran and Hadith data to their applications. Currently it provides Quranic and Hadith translations in Urdu language. Support for other languages is planned.

An example of an application that uses the Islam Companion Desktop API is the [Islam Companion Desktop](https://pakjiddat.netlify.com/posts/islam-companion-desktop-api) application.

The goal of the Islam Companion Desktop API is to help users develop desktop applications that provide knowledge about Islam.

### Features

The Islam Companion Desktop API has the following features:

* It provides translations of Holy Quran and Hadith in Urdu language. Support for more languages is planned
* It provides meta data about Holy Quran and Hadith data
* The source code is available under [GPL License](https://github.com/nadirlc/islam-companion-desktop-api/blob/master/LICENSE)
* The source code is well commented and easy to update
* The data is stored in sqlite3 database and can easily be accessed using the sqlite3 Python package

### Requirements

The Islam Companion Desktop API requires the os and sqlite3 Python packages. These packages are part of the standard Python distribution

### Installation

The following steps can be used to install the "Islam Companion Desktop API":

* Create a Python virtual environment using the command: **virtualenv -p python3.7 islam-companion**
* Activate the virtual environment using the command: **source bin/activate**
* Install from the Python Package Index (PPI) using the command: **pip install ic-desktop-api**
* Create a folder called **source**
* Download the **test** and **data** folders from the [source code](https://github.com/nadirlc/islam-companion-desktop-api/archive/master.zip) on GitHub. Copy the folders to the source folder
* Download the [quran](https://drive.google.com/open?id=11a_dQ4i0__--x5PkFjlmwMUxgMdTWbIa) sqlite database. Extract the downloaded file to **source/data/holy-quran.db**
* Download the [hadith](https://drive.google.com/open?id=1pHo5auUuKiNEi9jlmQJ0-n3oqDEdbDR0) sqlite database. Extract the downloaded file to **source/data/hadith.db**
* Install the [unittest2](https://pypi.org/project/unittest2/) Python package using the command: **pip install unittest2**. It will be used to unit test the API
* Test the quran api using the command: **python -m unittest test/quran.py**
* Test the hadith api using the command: **python -m unittest test/hadith.py**

### Usage

The Islam Companion Desktop API supports the following functions:

##### API calls for fetching Holy Quran data

1.  Name: **get_sura_names**  
Description: **Fetches list of all sura names from database**  
Response: **A numerically indexed array containing list of sura names**  
Parameters: **none**  
    
2.  Name: **get_ruku_count**  
Description: **Fetches the number of rukus in the given sura**  
Response: **An integer containing the number of rukus in the given sura**  
Parameters:  
    * **sura**. The sura number. It should be a number between 1 and 114  
    
3.  Name: **get_ayat_range**  
Description: **It returns the start and end ayat number for the given sura and ruku**  
Response: **An associative array with two elements. start (start ayat number) and end (end ayat number)**  
Parameters:  
    * **sura**. The sura number. It should be a number between 1 and 114  
    * **ruku**. The ruku number. It should be a number between 1 and 40  
    
4.  Name: **get_ayat_text**  
Description: **Fetches the ayat text for the given sura and ruku**  
Response: **A numerically indexed array containing list of ayas**  
Parameters:  
    * **sura**. The sura number. It should be a number between 1 and 114  
    * **ruku**. The ruku number. It should be a number between 1 and 40  

##### API calls for fetching Hadith data

1.  Name: **get_source_list**  
Description: **Fetches list of all hadith sources from database**  
Response: **A numerically indexed array containing list of hadith sources**  
Parameters:**none**  
    
2.  Name: **get_book_list**  
Description: **Fetches list of all hadith books for the given source from database**  
Response: **A numerically indexed array containing list of hadith books. Each index contains a numerically indexed array with two elements. The book id and book title**  
Parameters:  
    * **source**. The hadith source  
   
3.  Name: **get_title_list**  
Description: **Fetches list of all hadith titles for the given hadith book from database**  
Response: **A numerically indexed array containing the list of hadith titles. Each index contains a numerically indexed array with two elements. The title id and title text**  
Parameters:  
    * **book**. The hadith book id  
    
4.  Name: **get_hadith_text**  
Description: **It fetches and returns the hadith text for the given hadith id**  
Response: **A string containing the hadith text**  
Parameters:  
    * **hadith_id**. The hadith id  

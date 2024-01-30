# Book Scraper App

## Overview

This web scraper is designed to extract detailed information about books from [Books to Scrape](https://books.toscrape.com/). It navigates through each book category, collects data on every book, and saves this information in structured CSV files. Additionally, it downloads book images and sorts them into category-based folders.

## Features

- **Data Extraction**: Retrieves data such as title, UPC, price, availability, and more for each book.
- **Image Download**: Downloads book cover images.
- **Category-wise Organization**: Creates a CSV file for each book category and organizes images into respective category folders.
- **Progress Tracking**: Displays progress bars in the console during data scraping.

## How to Use

### Prerequisites

- Python 3.12.x
- PIP (Python package installer)

### Installation

1. **Clone the repository** (or download the source code).

    ```bash
    git clone https://github.com/Aura974/BooksOnlineScraper.git
    cd your_project
    ```

2. **Set Up a Python Virtual Environment** (optional but recommended):

    ```bash
    py -m venv env
    .\env\Scripts\activate.bat  # On Windows
    source env/bin/activate  # On Unix or MacOS
    ```

3. **Install required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scraper**:

    ```bash
    py main.py
    ```

## How it works

1. **Categories Scraping**:
The app starts by fetching URLs for all book categories from the home page.

2. **Books Data Extraction**:
For each category, it scrapes data for each book, including its title, price, UPC, and other relevant details.

3. **Data Organization**:
Each book's data is saved in a CSV file named after its category. These files are stored in the **data/\<category name\>** directories.

4. **Image Downloading**:
The cover images of the books are downloaded and saved in the folders corresponding to their categories within the data directory.

![Python Version](https://img.shields.io/badge/python-3.12.1-blue.svg)
![Last Commit](https://img.shields.io/github/last-commit/Aura974/BooksOnlineScraper/version-2024.svg)
![Static Badge](https://img.shields.io/badge/OpenClassrooms-P2-6b3fa0)

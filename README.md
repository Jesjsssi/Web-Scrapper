﻿# Web-Scraper

A simple web application for scraping content from websites using custom CSS selectors.

## Features

- Scrape data from any website by providing the URL
- Use custom CSS selectors to target specific elements
- Download results as CSV files
- Responsive user interface with Bootstrap

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```sh
   https://github.com/Jesjsssi/Web-Scrapper.git
   cd web-scraper
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```sh
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`

3. Enter the URL of the website you want to scrape in the "URL Website" field.

4. (Optional) Enter a CSS selector to target specific elements:
   - For tables rows: `table tr`
   - For elements with a specific class: `div.classname`
   - For elements with a specific ID: `#elementid`
   - Leave empty to scrape all paragraph (`<p>`) elements

5. Click "Scrape Data" to initiate the scraping process.

6. View the results in the "Hasil Scraping" section below.

7. Click "Download CSV" to download the scraped data as a CSV file.

## Project Structure

- `app.py` - Main Flask application
- `templates/index.html` - Frontend HTML template
- `static/data` - Directory for storing scraped data in CSV format
- `requirements.txt` - Python dependencies

## Dependencies

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing library
- [Requests](https://requests.readthedocs.io/) - HTTP library
- [Pandas](https://pandas.pydata.org/) - Data manipulation library
- [Bootstrap](https://getbootstrap.com/) - Frontend framework

## License

This project is licensed under the MIT License - see the LICENSE file for details.

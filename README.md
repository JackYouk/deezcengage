# DEEZCENGAGE SCRAPER

**Warning**: Image scraping functionality is not yet operational. Blame the cookie monster.

## Prerequisites
Before using the DEEZCENGAGE Scraper, ensure you have the necessary system dependency. Install `pdfkit` by following the guide available at [wkhtmltopdf downloads](https://wkhtmltopdf.org/downloads.html).

## Installation
1. Install the required Python packages:
   ```bash
   pip3 install -r requirements
   ```

## Configuration
1. Edit `run.py` to include your login credentials, the target eTextbook, and the number of pages you wish to scrape. Replace `username`, `password`, `textbook_name`, and `num_pages` with your information:
   ```python
   asyncio.run(scrape_textbook_runner(username='', password='', textbook_name='eTextbook: Introduction to Algorithms and Data Structures', num_pages=10))
   ```

## Usage
1. Run the script:
   ```bash
   python3 run.py
   ```

2. To observe the script in action, set the `headless` argument to `False` in the following line of code:
   ```python
   browser = await p.chromium.launch(headless=True)
   ```
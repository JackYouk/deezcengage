# deezcengage

**Warning**: Image scraping functionality is not yet operational. Blame the cookie monster.

## Prerequisites
Install `pdfkit` system deps using this guide: [wkhtmltopdf downloads](https://wkhtmltopdf.org/downloads.html).

## Installation
1. Install the required Python packages and browser binaries:
   ```bash
   pip3 install -r requirements
   python3 -m playwright install
   ```

## Configuration
1. Edit `run.py` to include your login credentials, the target eTextbook, and the number of pages you wish to scrape:
   ```python
   asyncio.run(scrape_textbook_runner(username='', password='', textbook_name='eTextbook: Introduction to Algorithms and Data Structures', num_pages=10))
   ```

## Usage
1. To run the script:
   ```bash
   python3 run.py
   ```

2. To see the bot in action, set the `headless` arg to `False` in the following line of code:
   ```python
   browser = await p.chromium.launch(headless=True)
   ```
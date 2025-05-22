# RERA Odisha Project Scraper
#Primenumbers Technologies - Assignment for the role of Data Engineer

This script scrapes the first 6 projects listed on the "RERA Odisha Project" page. It collects details required by the company such as:
Rera Regd. No, 
Project Name, 
Promoter Name (Company Name under Promoter Details Tab), 
Address of the Promoter (Registered Office Address under Promoter Details Tab), 
GST No.

## Note:
I tried to run this python program to scrape project details using Selenium because it interact with the browser and capture the dynamically rendered data.
Because of my chrome version and ChromeDriver version issues, I am not able to generate the result. That's why providing the logic for this assignment. If I go through other OS and other browser, it might be easy for this assignment.


## How to Run:

1. Run the script in terminal or any IDE:
   python rera_scraper.py

2. The script will:
   - Open the Odisha RERA project list.
   - Click "View Details" on the first 6 projects.
   - Collect the required information from each project page.
   - Print the results to console.

## Note:
- This script uses headless Firefox, so no browser window will open.
- Wait times (`time.sleep`) are used to allow pages to load properly.


## Author:
Shyam Kumar

# apple_app_store_purchases_scraper
A python script to scrape your apple app store purchases and output them in a CSV.

To access your apple purchases, visit the site https://reportaproblem.apple.com/ and log in with your Apple ID.

You will have to scroll down the page until all of the purchases you want to scrape have been populated and revealed by the site in your browser.  Once this has happened, right click on the page and select the `save as` option in the mouse menu to save the page as a local .html file on your computer.

To run the script, first make sure that you have Python installed on your computer.  Next, open the Command Line and navigate to the directory where you have saved the scraper script using `cd`.  Then run the script with the command `python apple_purchases_scraper.py`.

A file dialog will open asking you to select the html file you just saved on your computer.  Once opened, a second file dialog will open asking where you would like to save the CSV output file.  Once selected, the script will process the HTML file and save your purchases to the CSV file at the file destination you selected.

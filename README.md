# apple_app_store_purchases_scraper
A Python script to scrape your Apple App Store purchases and output them in a CSV format.


**Directions:**

1. To access your apple purchases, visit the site https://reportaproblem.apple.com/ and log in with your Apple ID.

2.  You will have to scroll down the page until all of the purchases you want to scrape have been populated and revealed by the site in your browser.  The script will only scrape data that has been provided by the server to your browser client, so scrolling down the page assures that the browser has requested the data you ultimately want.

3.  Right click on the Report a Problem page in your browser and select the `save as` option in the mouse menu to save the page as a local .html file on your hard drive.

4.  To run the script, first make sure that you have Python installed on your computer.  

5.  Open the Command Line and navigate to the directory where you have saved the scraper script using `cd`.

    Example:

    If you've saved the scraper file in your documents folder, type `cd Documents` to navigate to `C:/Users/username/Documents` where `username` is your local username on your computer.

6.  Run the script with the command `python apple_purchases_scraper.py`.

7.  A file dialog will open asking you to select the html file you just saved on your hard drive.  

8.  A second file dialog will open asking where you would like to save the CSV output file.  

9.  Once you've specified where to save the output file, the script will process the HTML file on your hard drive and your purchases will be saved in a CSV file at your selected file destination.

*Disclaimers:
- The script is specific to the HTML formatting used by Apple on the Report a Problem webpage.  Future changes to the page on Apple's part are likely to be breaking changes.
- I have not tested the script on a mac, so assume PC compatibility for now.*

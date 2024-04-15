from bs4 import BeautifulSoup
import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def select_html_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.html"), ("All files", "*.*")])
    return file_path

def prompt_save_location(default_name='output.csv'):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', initialfile=default_name, filetypes=[("CSV files", "*.csv")])
    return file_path

html_content = ''
html_file_path = select_html_file()
if html_file_path:
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

purchase_blocks = soup.find_all('div', class_='purchase loaded collapsed')

rows = []
for block in purchase_blocks:
    invoice_date_span = block.find('span', class_='invoice-date')
    if invoice_date_span:
        try:
            invoice_date = datetime.strptime(invoice_date_span.text.strip(), '%b %d, %Y').strftime('%m/%d/%y')
        except ValueError:
            invoice_date = "Invalid Date Format"
    else:
        invoice_date = "N/A"

    list_items = block.find_all('li', class_='pli')
    
    for item in list_items:
        title_label = item.find('label', class_='pli-title')
        title = title_label.text.strip() if title_label else "Title Missing"
        
        publisher_div = item.find('div', class_='pli-publisher has-publisher')
        publisher = publisher_div.text.strip() if publisher_div else "Publisher Missing"
        
        price_div = item.find('div', class_='pli-price')
        if price_div:
            price = price_div.text.strip().lower()
            price = "0" if "free" in price else price
        else:
            price = "Price Missing"
        
        rows.append([invoice_date, title, publisher, price])

output_file_path = prompt_save_location()

if output_file_path:
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Invoice Date', 'Title', 'Publisher', 'Price'])
        writer.writerows(rows)

    print(f'Data successfully written to {output_file_path}')
else:
    print("File save operation was canceled.")
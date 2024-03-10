import requests 
from bs4 import BeautifulSoup
import pandas as pd
def scrape_w3schools(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table")
        headers = [th.text.strip() for th in table.find_all("th")]
        rows = []
        for tr in table.find_all("tr")[1:]:
            row = [td.text.strip() for td in tr.find_all("td")]
            rows.append(row)
        df = pd.DataFrame(rows, columns=headers)
        file_name = input("Enter the file name: ")
        file_format = input("Enter the file format (excel/csv): ").lower()
        if file_format == 'excel':
            df.to_excel(f"{file_name}.xlsx", index=False)
            print("Data is stored in Excel file successfully.")
        elif file_format == 'csv':
            df.to_csv(f"{file_name}.csv", index=False)
            print("Data is stored in CSV file successfully.")
        else:
            print("Invalid file format. Please choose either 'excel' or 'csv'.")
    except requests.RequestException as e:
        print("Error fetching URL:", e)
    except Exception as e:
        print("An error occurred:", e)
url = "https://www.w3schools.com/html/html_tables.asp"
scrape_w3schools(url)

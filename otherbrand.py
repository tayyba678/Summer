from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome WebDriver
service = Service(executable_path=r'C:\Users\Hp\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Lists to store extracted data
phone_names = []
phone_conditions = []
phone_prices = []
shipping_costs = []
locations = []
sellers_info = []
quantities_sold = []

# Navigate to eBay
driver.get('https://www.ebay.com/sch/i.html?_oaa=1&_dcat=9355&_fsrp=1&Brand=Huawei%7CNokia%7COPPO%7CGoogle%7CRedmi%7CVIVO&_nkw=mobile+phones&_ipg=240&rt=nc&_pgn=1')

# Increase the wait time to ensure the page loads fully
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "s-item__info"))
    )
except Exception as e:
    print(f"Error occurred: {e}")
    driver.quit()
    exit()

# Function to extract data from the current page
def extract_data():
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    # Find all items
    items = soup.findAll('div', attrs={'class': 's-item__info clearfix'})

    if not items:
        print("No items found.")
    else:
        # Loop through each item and extract data
        for item in items:
            # Extract phone name
            name_element = item.find('div', attrs={'class': 's-item__title'})
            phone_name = name_element.text.strip() if name_element else 'Name not found'
            
            # Extract phone condition
            condition_element = item.find('span', attrs={'class': 'SECONDARY_INFO'})
            phone_condition = condition_element.text.strip() if condition_element else 'Condition not found'
            
            # Extract price
            price_element = item.find('span', attrs={'class': 's-item__price'})
            phone_price = price_element.text.strip() if price_element else 'Price not found'
            
            # Extract shipping cost
            shipping_element = item.find('span', attrs={'class': 's-item__shipping s-item__logisticsCost'})
            shipping_cost = shipping_element.text.strip() if shipping_element else 'Shipping cost not found'
            
            # Extract location
            location_element = item.find('span', attrs={'class': 's-item__location s-item__itemLocation'})
            location = location_element.text.strip() if location_element else 'Location not found'
            
            # Extract seller information
            seller_element = item.find('span', attrs={'class': 's-item__seller-info-text'})
            seller_info = seller_element.text.strip() if seller_element else 'Seller info not found'
            
            # Extract quantity sold
            quantity_sold = item.find('span', attrs={'class': 's-item__dynamic s-item__quantitySold'})
            quantity = quantity_sold.text.strip() if quantity_sold else 'Quantity sold not found'
            
            # Store the extracted data
            phone_names.append(phone_name)
            phone_conditions.append(phone_condition)
            phone_prices.append(phone_price)
            shipping_costs.append(shipping_cost)
            locations.append(location)
            sellers_info.append(seller_info)
            quantities_sold.append(quantity)

# Scrape multiple pages
for _ in range(30):  # Adjust the number of pages as needed
    extract_data()  # Extract data from the current page

    # Click the "Next" button
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "a.pagination__next.icon-link")
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
    except Exception as e:
        print(f"Error occurred while navigating to the next page: {e}")
        break  # Exit loop if there is an issue with clicking next

# Create a DataFrame with the extracted data
df = pd.DataFrame({
    'Phone Name': phone_names,
    'Condition': phone_conditions,
    'Price': phone_prices,
    'Shipping Cost': shipping_costs,
    'Location': locations,
    'Seller Info': sellers_info,
    'Quantity Sold': quantities_sold
})

# Save the data to a CSV file
df.to_csv('ebay_mobile_otherbrand.csv', index=False, encoding='utf-8')

# Close the driver
driver.quit()

print("Scraping complete. Data saved to CSV.")

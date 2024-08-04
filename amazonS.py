from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


driver = webdriver.Chrome()

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

query = "laptop"
file = 0

for i in range(1, 20):
    # Navigate to the Amazon search results page
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1SHZQ9484BWV8&sprefix=laptop%2Caps%2C493&ref=nb_sb_noss_2")
    
    # Wait until elements with the class 'puis-card-container' are present
    wait = WebDriverWait(driver, 10)
    elems = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "puis-card-container")))

    # Print the number of elements found
    print(f"{len(elems)} items found")

    # Iterate over elements and save their HTML
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file += 1

    time.sleep(5)

# Close the WebDriver after the loop completes
driver.quit()


    


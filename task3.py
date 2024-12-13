import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()

url = 'https://www.divan.ru/category/divany-i-kresla'

driver.get(url)

divans = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div._Ud0k'))
)

parsed_data = []

for divan in divans:
    try:
        prices = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
        parsed_data.append([prices])
    except Exception as e:
        print('Произошла ошибка при парсинге: {e}')
        continue

driver.quit()

with open("price.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])
    writer.writerows(parsed_data)
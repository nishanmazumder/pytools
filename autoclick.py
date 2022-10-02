from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mysite.com")

# For anchor tag
anchor = driver.find_element(By.TAG_NAME, "a")

# For Styles & Scripts
links = driver.find_elements(By.TAG_NAME, "link")
scripts = driver.find_elements(By.TAG_NAME, "script")

for link in links:
    href = link.get_attribute("href")
    driver.execute_script("window.open('"+href+"')")

    print(link.get_attribute("href"))
    # break

for script in scripts:
    src = script.get_attribute("src")
    driver.execute_script("window.open('"+src+"')")

    print(script.get_attribute("src"))
    # break

driver.quit()

print('done!')

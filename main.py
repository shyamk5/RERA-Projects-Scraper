#main.py

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(url)
time.sleep(3)

projects = []

# Loop for getting first 6 projects details
for i in range(1, 7):
    try:
        view_button = driver.find_element(By.XPATH, f"(//a[contains(text(),'View Details')])[{i}]")
        driver.execute_script("arguments[0].click();", view_button)
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        rera_no = driver.find_element(By.XPATH, "//label[contains(text(),'RERA Regd. No')]/following-sibling::div").text.strip()
        project_name = driver.find_element(By.XPATH, "//label[contains(text(),'Project Name')]/following-sibling::div").text.strip()

        promoter_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Promoter Details')]")
        promoter_tab.click()
        time.sleep(1)

        promoter_name = driver.find_element(By.XPATH, "//label[contains(text(),'Company Name')]/following-sibling::div").text.strip()
        promoter_address = driver.find_element(By.XPATH, "//label[contains(text(),'Registered Office Address')]/following-sibling::div").text.strip()
        gst_number = driver.find_element(By.XPATH, "//label[contains(text(),'GST No')]/following-sibling::div").text.strip()

        projects.append({
            "RERA Regd. No": rera_no,
            "Project Name": project_name,
            "Promoter Name": promoter_name,
            "Promoter Address": promoter_address,
            "GST No": gst_number
        })

        # Closing the connection
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

    except Exception as e:
        print(f"Error in project {i}: {e}")
        continue

driver.quit()

# final output
for idx, proj in enumerate(projects, 1):
    print(f"\nProject {idx}:")
    for key, value in proj.items():
        print(f"{key}: {value}")

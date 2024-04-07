import json
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from utils.get_data import get_data

vessels = [
    "KRITI II",
    "EVER GIVEN",
    "OASIS OF THE SEAS",
    "QUEEN ELIZABETH",
    "BLUE STAR DELOS",
    "FESTOS PALACE",
    "LEFKA ORI",
    "KISSAMOS",
    "LE LYRIAL",
]

EMAIL = "" # YOUR EMAIL HERE
PASSWORD = "" # YOUR PASSWORD HERE

def main():

    driver = uc.Chrome()  # Tested on Chrome browser
    driver.maximize_window()
    driver.get("https://www.marinetraffic.com/")
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    wait = WebDriverWait(driver, 15, ignored_exceptions=ignored_exceptions)
    data = []  # the final data

    try:
        # wait until cookies group buttons appear
        wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "qc-cmp2-summary-buttons"))
        )

        # find the agree button and click it
        agreeBtn = driver.find_element(By.XPATH, '//*[text()="AGREE"]')
        wait.until(EC.element_to_be_clickable(agreeBtn))
        agreeBtn.click()

        # wait for the login button to render
        wait.until(EC.presence_of_element_located((By.ID, "login")))
        wait.until(EC.element_to_be_clickable((By.ID, "login")))

        login = driver.find_element(By.ID, "login")
        login.click()

        # wait for the form to render and fill the inputs
        wait.until(EC.presence_of_element_located((By.ID, "email")))
        wait.until(EC.element_to_be_clickable((By.ID, "email")))

        wait.until(EC.presence_of_element_located((By.ID, "password")))
        wait.until(EC.element_to_be_clickable((By.ID, "password")))

        emailElem = driver.find_element(By.ID, "email")
        passElem = driver.find_element(By.ID, "password")

        emailElem.send_keys(EMAIL)
        passElem.send_keys(PASSWORD) # PASSWORD HERE

        wait.until(EC.presence_of_element_located((By.ID, "login_form_submit")))
        submitBtm = driver.find_element(By.ID, "login_form_submit")
        wait.until(EC.element_to_be_clickable(submitBtm))
        submitBtm.click()

        # wait unit the login backdrop and dialog disappears
        wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, '//div[@role="presentation"]')
            )
        )
        wait.until(
            EC.invisibility_of_element_located(
                (By.XPATH, '//*[@class="MuiBackdrop-root"]')
            )
        )

        # click the vessel button on the left panel
        wait.until(EC.presence_of_element_located((By.ID, "vessels")))
        vesselButton = driver.find_element(By.ID, "vessels").find_element(
            By.XPATH, './/div[@role="button"]'
        )
        wait.until(EC.element_to_be_clickable(vesselButton))
        vesselButton.click()

        # repeat for each vessel
        for vessel_name in vessels:  

            # wait until vessel page fully loads
            wait.until(
                EC.presence_of_element_located((By.XPATH, '//input[@role="combobox"]'))
            )
            
            # fill the input with the vessel name
            inputBox = driver.find_element(By.XPATH, '//input[@role="combobox"]')
            inputBox.send_keys(vessel_name)

            # wait until the vessel lists loads, then find and click the vessel
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[text()=" + '"' + str(vessel_name) + '"' + "]")
                )
            )
            
            driver.find_element(
                By.XPATH, "//*[text()=" + '"' + str(vessel_name) + '"' + "]"
            ).click()
            
            # find the table with all the vessels the system found and click it
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[text()=" + '"' + str(vessel_name) + '"' + "]")
                )
            )
            driver.find_element(
                By.XPATH, "//a[text()=" + '"' + str(vessel_name) + '"' + "]"
            ).click()
            
            # wait until the vessel details page loads
            wait.until(
                EC.presence_of_element_located((By.ID, "vesselDetails_generalSection"))
            )
            
            # find the first table
            section = driver.find_element(By.ID, "vesselDetails_generalSection")
            table_id = section.find_element(By.CLASS_NAME, "MuiTable-root")

            data.append(get_data(table_id))
            driver.back()

        # write the data to json file
        with open("results.json", "w") as json_file:
            json.dump(data, json_file)

    finally:
        driver.close()


if __name__ == "__main__":
    main()

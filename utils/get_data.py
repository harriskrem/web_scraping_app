from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

def get_data(table_id: WebElement):

    name = ""
    imo = ""
    mmsi = ""
    speed = ""
    course = ""

    for row in range(1, 11):
        rows = table_id.find_elements(By.XPATH, "//body//tbody//tr[" + str(row) + "]")

        # for each row get the key and element
        for row_data in rows:
            col1 = row_data.find_elements(By.TAG_NAME, "th")
            col2 = row_data.find_elements(By.TAG_NAME, "td")
            for i in range(min(len(col1), len(col2))):
                if col1[i].text == "Name":
                    name = col2[i].text
                elif col1[i].text == "IMO":
                    imo = col2[i].text
                elif col1[i].text == "MMSI":
                    mmsi = col2[i].text
                elif col1[i].text == "Speed":
                    speed = col2[i].text
                elif col1[i].text == "Course":
                    course = col2[i].text
                    
    # return the data as a object
    return {"Name": name, "IMO": imo, "MMSI": mmsi, "Speed": speed, "Course": course}

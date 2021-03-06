from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("릴리 콜린스")
elem.send_keys(Keys.RETURN)
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

count = 1
for i in range(0,200):
    try:
        driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[i].click()
        time.sleep(0.5)
        imgUrl = driver.find_element_by_css_selector(".n3VNCb.KAlRDb").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "./img04/"+str(count)+".jpg")
        count=count+1
    except:
        pass

driver.close()
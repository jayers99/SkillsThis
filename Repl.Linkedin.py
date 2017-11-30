from selenium import webdriver
import time

browser = webdriver.Chrome("/Applications/chromedriver")
browser.get("https://linkedin.com")
url = "https://www.linkedin.com/jobs/search/?keywords=devops%20engineer&location=San%20Rafael%2C%20California&locationId=PLACES.us.7-1-0-21-22"
browser.get(url)
time.sleep(3)
# you must scroll to the bottom of the page for all the items to be loaded
windowheight = browser.get_window_size()['height']
innerheight = browser.execute_script("return window.innerHeight")
docheight = browser.execute_script("return document.body.scrollHeight")
scrollpos = 0
while scrollpos < docheight:
    scrollpos += (innerheight - 100)
    scrollcmd = "window.scrollTo(0, " + str(scrollpos) + ");"
    browser.execute_script(scrollcmd)
    time.sleep(3)

linkselements = browser.find_elements_by_css_selector(".job-card-search__upper-content-wrapper-left a")
links += [link.get_attribute("href") for link in linkselements]



for link in links:
    print(link)
    browser.get(link)
    time.sleep(3)







next = browser.find_element_by_css_selector("button.next")
next.click()
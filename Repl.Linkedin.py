from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys


# setup the env
browser = webdriver.Chrome("/Applications/chromedriver")

# loop through n number of job posting pages and build a list of job links
thismanypages = 20
currentpage = 10
baseurl = "https://www.linkedin.com/jobs/search/?keywords=devops%20engineer&location=San%20Rafael%2C%20California&locationId=PLACES.us.7-1-0-21-22"
links = []

while currentpage < thismanypages:
    # create the url
    if currentpage != 0:
        startpara = "&start={}".format(currentpage*25)
    else:
        startpara = ""
    url = "{0}{1}".format(baseurl, startpara)
    print(url)
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
    currentpage += 1

# scrape the job description of the job links
len(links)
with open('/Users/jayers/Temp/aJobDesctions.html', 'w') as file:
    file.write(time.strftime("%c"))

for link in links:
    print(link)
    try:
        # try to grab the page and extract the data i want
        browser.get(link)
        jobtitle = WebDriverWait(browser, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".jobs-details-top-card__content-container.mt6.pb5 h1")))
        #time.sleep(4)
        #jobtitle = browser.find_element_by_css_selector(".jobs-details-top-card__content-container.mt6.pb5 h1")
        jobtitlestr = jobtitle.get_attribute("innerHTML")
        jobloc = browser.find_element_by_css_selector(".jobs-details-top-card__content-container.mt6.pb5 h3")
        joblocstr = jobloc.get_attribute("innerHTML")
        jobdesc = browser.find_element_by_id("job-details")
        jobdescstr = jobdesc.get_attribute("innerHTML")
    except exceptions.NoSuchElementException as ex:
        print("ERROR: {}".format(ex.msg))
    except exceptions.TimeoutException as ex:
        print("ERROR: {}".format(ex.msg))
    except:
        print("Unexpected ERROR:", sys.exc_info()[0])
    else:
        # write the results to a file
        with open('/Users/jayers/Temp/aJobDesctions.html', 'a') as file:
            file.write('\n<br>\n<hr>\n<br>')
            file.write('\n<div class="jayers-job">')
            file.write('\n<div class="jayers-job-title">{}\n</div>'.format(jobtitlestr))
            file.write('\n<div class="jayers-job-loc">{}\n</div>'.format(joblocstr))
            file.write('\n<div class="jayers-job-link"><a href="{}" target="_blank">Job Link</a>\n</div>'.format(link))
            file.write('\n<div class="jayers-job-desc">{}\n</div>'.format(jobdescstr))
            file.write('\n</div>')



        except as ex:
        #print("    ERROR Code: {} - {}".format(ex.code, ex.reason))







jobdesc.text


next = browser.find_element_by_css_selector("button.next")
next.click()
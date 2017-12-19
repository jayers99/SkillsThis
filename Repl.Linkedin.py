"""

The file is full of a bunch of commands i was experimenting with pulling data
off the linkedin web site.  It will NOT run as a complete program.

"""
# pylint: skip-file

import time
import sys
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setup the env
BROWSER = webdriver.Chrome("/Applications/chromedriver")

# loop through n number of job posting pages and build a list of job links
THIS_MANY_PAGES = 40
CURRENT_PAGE = 0
BASE_URL = "https://www.linkedin.com/jobs/search/?keywords=devops%20engineer&location=San%20Rafael%2C%20California&locationId=PLACES.us.7-1-0-21-22"
links = []

while CURRENT_PAGE < THIS_MANY_PAGES:
    # create the url
    if CURRENT_PAGE != 0:
        startpara = "&start={}".format(CURRENT_PAGE*25)
    else:
        startpara = ""
    url = "{0}{1}".format(BASE_URL, startpara)
    print(url)
    BROWSER.get(url)
    time.sleep(4)
    # you must scroll to the bottom of the page for all the items to be loaded
    windowheight = BROWSER.get_window_size()['height']
    innerheight = BROWSER.execute_script("return window.innerHeight")
    docheight = BROWSER.execute_script("return document.body.scrollHeight")
    scrollpos = 0
    while scrollpos < docheight:
        scrollpos += (innerheight - 100)
        scrollcmd = "window.scrollTo(0, " + str(scrollpos) + ");"
        BROWSER.execute_script(scrollcmd)
        time.sleep(3)
    linkselements = BROWSER.find_elements_by_css_selector(".job-card-search__upper-content-wrapper-left a")
    links += [link.get_attribute("href") for link in linkselements]
    CURRENT_PAGE += 1

# save all those links off to a file
print("{} links scraped".format(len(links)))
with open('/Users/jayers/Temp/alinks.txt', 'w') as file:
    file.write(str(links))
# reload the links from file
import ast
links = []
with open('/Users/jayers/Temp/alinks.txt', 'r') as file:
    links = ast.literal_eval(file.read())

links[400:410]

# scrape the job description of the job links
with open('/Users/jayers/Temp/aJobDesctions.html', 'w') as file:
    file.write(time.strftime("%c"))

# get the job desc for posts when you are logged on see below for not logged on format
for link in links[800:1000]:
    print(link)
    try:
        # try to grab the page and extract the data i want
        BROWSER.get(link)
        jobtitle = WebDriverWait(BROWSER, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".jobs-details-top-card__content-container.mt6.pb5 h1")))
        jobloc = WebDriverWait(BROWSER, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, ".jobs-details-top-card__content-container.mt6.pb5 h3")))
        jobdesc = WebDriverWait(BROWSER, 10).until(EC.presence_of_element_located((
            By.ID, "job-details")))
        jobtitlestr = jobtitle.get_attribute("innerHTML")
        joblocstr = jobloc.get_attribute("innerHTML")
        jobdescstr = jobdesc.get_attribute("innerHTML")
    except exceptions.NoSuchElementException as ex:
        print("ERROR: {}".format(ex.msg))
    except exceptions.TimeoutException as ex:
        print("ERROR: {}".format(ex.msg))
    except KeyboardInterrupt:
        print('interrupted!')
        break
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



with open('/Users/jayers/Temp/aJobDesctionsOldformatTest.html', 'w') as file:
    file.write(time.strftime("%c"))

# get the job desc for posts when you are not logged on
for link in links[390:500]:
    print(link)
    try:
        # try to grab the page and extract the data i want
        BROWSER.get(link)
        jobtitle = WebDriverWait(BROWSER, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "h1.title")))
        jobcompany = WebDriverWait(BROWSER, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "span.company")))
        jobloc = WebDriverWait(BROWSER, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "h3.location")))
        jobdesc = WebDriverWait(BROWSER, 10).until(EC.presence_of_element_located((
            By.ID, "div.summary")))
        jobtitlestr = jobtitle.get_attribute("innerHTML")
        joblocstr = "{}{}".format(jobcompany.get_attribute("innerHTML"), jobloc.get_attribute("innerHTML"))
        jobdescstr = jobdesc.get_attribute("innerHTML")
    except exceptions.NoSuchElementException as ex:
        print("ERROR: {}".format(ex.msg))
    except exceptions.TimeoutException as ex:
        print("ERROR: {}".format(ex.msg))
    except KeyboardInterrupt:
        print('interrupted!')
        break
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




# convert the html file to text for nlp
from bs4 import BeautifulSoup

# read the massive 1000 html file, filter it and convert it to text for NLP
fpath = r"/Users/jayers/Temp/Linkedin1000JobDesctions.html"
page = open(fpath, encoding='utf-8', errors='ignore')
soup = BeautifulSoup(page, 'html5lib')
jobs = soup.select("div.jayers-job")

# test things out on a single entry
job1 = jobs[0].select("div.jayers-job-title")
type(job1)
job1[0].text.strip()
job1desc = jobs[0].select("div.jayers-job-desc")[0].text.strip()
type(jobs[0].select("div.jayers-job-desc")[0].get_text(separator='\n'))
jobsamp = jobs[0].select("div.jayers-job-desc")[0].get_text(separator='\n')
import chardet
chardet.detect(jobs[0].select("div.jayers-job-desc")[0].get_text(separator='\n'))
''.join([i if ord(i) < 128 else ' ' for i in jobsamp])

# loop through all jobs to create text to analyze
jobdescs = ""
for i, job in enumerate(jobs):
    try:
        jobtitle = job.select("div.jayers-job-title")[0].text.strip()
        jobcompany = job.select("div.jayers-job-loc a")[0].text.strip()
        jobdescraw = job.select("div.jayers-job-desc")[0].get_text(separator='\n').replace("’", "'").replace("/", " ")
        jobdesc = ''.join([i if ord(i) < 128 else ' ' for i in jobdescraw])
    except IndexError as ex:
        print("{}  index error".format(i))
    else:
        print("{}  {} - {}".format(i, jobtitle, jobcompany))
        jobdescs += jobdesc


jobdescs

with open('/Users/jayers/Temp/Linkedin1000JobDesctions.txt', 'w') as file:
    file.write(jobdescs)


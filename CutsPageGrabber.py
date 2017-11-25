import sys
import urllib.request
import ssl
from bs4 import BeautifulSoup
import os
clear = lambda: os.system('clear')
clear()
print(sys.version, end='\n\n')

terms = 'DevOps Engineer'
loc = 'San Rafael, CA'
baseurl = "https://www.indeed.com"

terms = terms.replace(' ', '+')
loc = loc.replace(' ', '+')
loc = loc.replace(',', '%2C')
searchbaseurl = 'https://www.indeed.com/jobs?q={}&l={}'.format(terms, loc)

requrl = searchbaseurl
print(requrl)
https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
opener = urllib.request.build_opener(https_sslv3_handler)
urllib.request.install_opener(opener)
resp = opener.open(requrl)
udata = resp.read().decode('utf-8')
soup = BeautifulSoup(udata, "html5lib")

searchtitle = soup.find_all("title")
searchcountelement = soup.select_one("#searchCount")
searchcounttext = searchcountelement.text.strip()
searchcountnum = int(searchcounttext.split()[-1])
#next page link didn't work
#soup.select_one(".np").parent.parent["href"]
# for some reason this data-pp grab is failing now
# + "&pp=" + soup.select_one(".np").parent.parent["data-pp"]
#soup.select_one(".np").parent.parent["href"]

jobpostsummaries = soup.find_all(attrs={"data-tn-component": "organicJob"})
startnum = 10

while (searchcountnum - startnum > 0): 
    print("\nNow Getting Page that starts with {}".format(str(startnum)))
    requrl = searchbaseurl + "&start=" + str(startnum)
    print(requrl)
    https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
    opener = urllib.request.build_opener(https_sslv3_handler)
    urllib.request.install_opener(opener)
    resp = opener.open(requrl)
    udata = resp.read().decode('utf-8')
    soup = BeautifulSoup(udata, "html5lib")
    pagesumm = soup.find_all(attrs={"data-tn-component": "organicJob"})
    for jobpost in pagesumm:
        jobpostsummaries.append(jobpost)
    startnum = startnum + 10

len(jobpostsummaries)



errorcount = 0
successcount = 0
errorresults = []
for idx, jobpost in enumerate(jobpostsummaries):
    print(idx)
    if idx > 1000:
        break
    else:
        jobtitle = jobpost.find(attrs={"data-tn-element": "jobTitle"})['title']
        print(jobtitle)
        https_sslv3_handler = urllib.request.HTTPSHandler(context=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
        opener = urllib.request.build_opener(https_sslv3_handler)
        urllib.request.install_opener(opener)
        requrl = baseurl + jobpost.find(attrs={"data-tn-element": "jobTitle"})['href']
        print(requrl)
        try:
            resp = opener.open(requrl)
            udata = resp.read().decode('utf-8', errors='ignore')
            with open('/Users/jayers/Temp/Jobpost{}.html'.format(str(idx).zfill(3)), 'w') as file:
                file.write(udata)
            soup = BeautifulSoup(udata, "html5lib")
            print(soup.find_all("title"))
            successcount += 1
        except urllib.request.HTTPError as ex:
            print("    ERROR Type: {}".format(type(ex)))
            print("    ERROR Code: {} - {}".format(ex.code, ex.reason))
            errorcount += 1
            errorresults.append(jobpost)
        except urllib.error.URLError as ex:
            print("    ERROR Type: {}".format(type(ex)))
            print("    ERROR Code: {}".format(ex.reason))
            errorcount += 1
            errorresults.append(jobpost)
    print("\n")

print("Successful Count: {}".format(successcount))
print("Error count: {}".format(errorcount))

for idx, jobpost in enumerate(errorresults):
    print(idx)
    jobtitle = jobpost.find(attrs={"data-tn-element": "jobTitle"})['title']
    print(jobtitle)
    requrl = baseurl + jobpost.find(attrs={"data-tn-element": "jobTitle"})['href']
    print(requrl)
    print("\n")

#function to get just visible text
#https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
from bs4.element import Comment
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(passedsoup):
    texts = passedsoup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


#parse a lot of the junk out of a single saved html file
from bs4 import BeautifulSoup
filepath = r"/Users/jayers/Temp/Jobpost003.html"
print(filepath)
page = open(filepath, encoding='utf-8', errors='ignore')
soup = BeautifulSoup(page, 'html5lib')
jobsummary = soup.find("span", {"id": "job_summary"})
if jobsummary is not None:
    soup = jobsummary

#print(text_from_html(page))
newfilepath = os.path.dirname(filepath) + "/{0}.{2}".format(*os.path.basename(filepath).split('.') + ['txt'])
with open(newfilepath, "w") as file:
    file.write(str(text_from_html(soup)))

#looping name conflict check
for filepath in glob.glob("/Users/jayers/Temp/Jobpost[0-9][0-9][0-9].html"):
    print("original file: {}".format(filepath))
    bodyhtmlpath = os.path.dirname(filepath) + "/{0}.{2}.{1}".format(*os.path.basename(filepath).split('.') + ['body'])
    print("body html:{}".format(bodyhtmlpath))
    bodytextpath = os.path.dirname(filepath) + "/{0}.{2}".format(*os.path.basename(filepath).split('.') + ['body.txt'])
    print("body text: {}".format(bodytextpath))


#loop to generate all the stripped html and text files
import glob, os
for filepath in glob.glob("/Users/jayers/Temp/Jobpost[0-9][0-9][0-9].html"):
    print(filepath)
    page = open(filepath, encoding='utf-8', errors='ignore')
    soup = BeautifulSoup(page, 'html5lib')
    jobsummary = soup.find("span", {"id": "job_summary"})
    if jobsummary is not None:
        soup = jobsummary
        print("job summary found")
        
    newfilepath = os.path.dirname(filepath) + "/{0}.{2}".format(*os.path.basename(filepath).split('.') + ['txt'])
    with open(newfilepath, "w") as file:
        file.write(str(text_from_html(soup)))







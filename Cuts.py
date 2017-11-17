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
    if idx > 10:
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
            with open('Jobpost{}.html'.format(str(idx).zfill(3)), 'w') as file:
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




import sys
from bs4 import BeautifulSoup
import os
print(sys.version, end='\n\n')

# linkedin url
https://www.linkedin.com/jobs/search/?keywords=devops%20engineer&location=San%20Rafael%2C%20California&locationId=PLACES.us.7-1-0-21-22
https://www.linkedin.com/jobs/search/?keywords=devops%20engineer&location=San%20Rafael%2C%20California&locationId=PLACES.us.7-1-0-21-22&start=25
https://www.linkedin.com/jobs/view/464597740/

# try using the requests lib
import requests
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://www.linkedin.com/',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

basesearchurl = "https://www.linkedin.com/jobs/search/"
payload = {'keywords': 'devops engineer', 'location': 'San Rafael, California', 'locationId': 'PLACES.us.7-1-0-21-22'}
cookies = {
    "bcookie":"v=2&7ccadf5c-f645-45e8-85d4-cdb35b4b041b",
    "bscookie":"v=1&20170712222207b024f77c-59e4-4db9-812c-e65946e039d4AQG-rjuWQ28BC6rJMyAI_Cc4iqdn9vRh",
    "visit":"v=1&M",
    "sl":"v=1&65ShK",
    "liap":"true",
    "li_at":"AQEDAQD2XMgFYblAAAABX_9u6ZAAAAFgI3ttkFYAuLA4rwXDVfMtCL9aOWHdbLr31wfA0Jplppk3RFlncV2vDj9PiOttmSc1z0pqEDg6RqWVANnJKZsGTVdy_I0WNgxA5_RY4KcgXA2t62RI6Meo8Xoj",
    "JSESSIONID":"ajax:8513822846118758376",
    "lang":"v=2&lang=en-us",
    "_ga":"GA1.2.1396653397.1511818507",
    "_gat":"1",
    "_lipt":"wEAAAFgCpf01tekOhoeXP9SoAh8TQovR1HCuB5MFMhea6D0RzdWAGEjEtbcuT9LBGY6acr8tgZQZl5hIUzS4463VYE2xnBuSLEMcHCPupzjU4HvwCM4YPSEkit82qPrxUy-_f86LZdzrTP7-_MUeq2Kv4cTjHJeOMz_HNoD6vyxqZ3QP4kZikvg-VyhsqlFgA-ux195trvf8PKcHxik4g_3Mptv5AdIwp3p_nwOkequAwJ0ddeEhL9pcq3HqTB2TN5XUzh1B6LBkW_zAK0kRnd8GKPYC110P_fXKEKdKW4VMmN6aEdFUY1_rcd8tr7ElVNTx6WjeoGOWWvqzSLvWrAGX5V_VNT80B1FfcNjwL5MxIJ5pw1YeZ0",
    "lidc":"b=OB08:g=664:u=197:i=1512006277:t=1512084706:s=AQHYM04HIXMrAjFr4z2D3Ual3UCeVxi6"
}
cookies = {
    "bcookie":"v=2&7ccadf5c-f645-45e8-85d4-cdb35b4b041b",
    "bscookie":"v=1&20170712222207b024f77c-59e4-4db9-812c-e65946e039d4AQG-rjuWQ28BC6rJMyAI_Cc4iqdn9vRh",
    "visit":"v=1&M",
    "sl":"v=1&65ShK",
    "liap":"true",
    "li_at":"AQEDAQD2XMgFYblAAAABX_9u6ZAAAAFgI3ttkFYAuLA4rwXDVfMtCL9aOWHdbLr31wfA0Jplppk3RFlncV2vDj9PiOttmSc1z0pqEDg6RqWVANnJKZsGTVdy_I0WNgxA5_RY4KcgXA2t62RI6Meo8Xoj",
    "JSESSIONID":"ajax:8513822846118758376",
    "lang":"v=2&lang=en-us",
    "_ga":"GA1.2.1396653397.1511818507",
    "_lipt":"wEAAAFgCpf01tekOhoeXP9SoAh8TQovR1HCuB5MFMhea6D0RzdWAGEjEtbcuT9LBGY6acr8tgZQZl5hIUzS4463VYE2xnBuSLEMcHCPupzjU4HvwCM4YPSEkit82qPrxUy-_f86LZdzrTP7-_MUeq2Kv4cTjHJeOMz_HNoD6vyxqZ3QP4kZikvg-VyhsqlFgA-ux195trvf8PKcHxik4g_3Mptv5AdIwp3p_nwOkequAwJ0ddeEhL9pcq3HqTB2TN5XUzh1B6LBkW_zAK0kRnd8GKPYC110P_fXKEKdKW4VMmN6aEdFUY1_rcd8tr7ElVNTx6WjeoGOWWvqzSLvWrAGX5V_VNT80B1FfcNjwL5MxIJ5pw1YeZ0",
    "lidc":"b=OB08:g=664:u=197:i=1512006277:t=1512084706:s=AQHYM04HIXMrAjFr4z2D3Ual3UCeVxi6"
}
#bcookie="v=2&7ccadf5c-f645-45e8-85d4-cdb35b4b041b"; bscookie="v=1&20170712222207b024f77c-59e4-4db9-812c-e65946e039d4AQG-rjuWQ28BC6rJMyAI_Cc4iqdn9vRh"; visit="v=1&M"; sl="v=1&65ShK"; liap=true; li_at=AQEDAQD2XMgFYblAAAABX_9u6ZAAAAFgI3ttkFYAuLA4rwXDVfMtCL9aOWHdbLr31wfA0Jplppk3RFlncV2vDj9PiOttmSc1z0pqEDg6RqWVANnJKZsGTVdy_I0WNgxA5_RY4KcgXA2t62RI6Meo8Xoj; JSESSIONID="ajax:8513822846118758376"; lang="v=2&lang=en-us"; _ga=GA1.2.1396653397.1511818507; _gat=1; _lipt=CwEAAAFgCpf01tekOhoeXP9SoAh8TQovR1HCuB5MFMhea6D0RzdWAGEjEtbcuT9LBGY6acr8tgZQZl5hIUzS4463VYE2xnBuSLEMcHCPupzjU4HvwCM4YPSEkit82qPrxUy-_f86LZdzrTP7-_MUeq2Kv4cTjHJeOMz_HNoD6vyxqZ3QP4kZikvg-VyhsqlFgA-ux195trvf8PKcHxik4g_3Mptv5AdIwp3p_nwOkequAwJ0ddeEhL9pcq3HqTB2TN5XUzh1B6LBkW_zAK0kRnd8GKPYC110P_fXKEKdKW4VMmN6aEdFUY1_rcd8tr7ElVNTx6WjeoGOWWvqzSLvWrAGX5V_VNT80B1FfcNjwL5MxIJ5pw1YeZ0; lidc="b=OB08:g=664:u=197:i=1512006277:t=1512084706:s=AQHYM04HIXMrAjFr4z2D3Ual3UCeVxi6"
#respsearch = requests.get(basesearchurl, params=payload, headers=headers, cookies=cookies)

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

req = requests.Request('GET', basesearchurl, params=payload, headers=headers)
prepared = req.prepare()

pretty_print_POST(prepared)

respsearch = requests.get(basesearchurl, params=payload, headers=headers)
respsearch
respsearch.cookies
with open('/Users/jayers/Temp/atest.html', 'w') as file:
    file.write(respsearch.text)

# make some soup
soupsearch = BeautifulSoup(respsearch.text, "html5lib")
searchtitle = soupsearch.find_all("title")
print(searchtitle)
# linked in uses javascript to ender page
# pull out the json object with the job listings in it
codesoup = soupsearch.find("code", {"id": "decoratedJobPostingsModule"})
codesoup.contents[0]

# turn in into python json object
import json
jobsjson = json.loads(codesoup.contents[0])
# parse out the url for the job listing
print(jobsjson['elements'][0]['viewJobTextUrl'])
for job in jobsjson['elements']:
    print(job['viewJobTextUrl'])

# get full job text
print(jobsjson['elements'][1]['viewJobTextUrl'])
respjob = requests.get(jobsjson['elements'][1]['viewJobTextUrl'], headers=headers, cookies=respsearch.cookies)
respjob
with open('/Users/jayers/Temp/ajobtest.html', 'w') as file:
    file.write(respjob.text)
soupjob = BeautifulSoup(respjob.text, "html5lib")
codesoupjob = soupjob.find("code", {"id": "jobDescriptionModule"})
#codesoupjob.contents[0]
codesoupjob.contents[0]
jsonjob = json.loads(codesoupjob.contents[0])
print(jsonjob['description'])
print(jsonjob['skillsDescription'])
with open('/Users/jayers/Temp/ajobdesctest.html', 'w') as file:
    file.write(jsonjob['description'])
    if jsonjob['skillsDescription'] is not None:
        file.write(jsonjob['skillsDescription'])


# now try to loop through a page of jobs
for job in jobsjson['elements']:
    print(job['viewJobTextUrl'])
    respjob = requests.get(job['viewJobTextUrl'], headers=headers)
    if respjob.status_code == 999:
        print("response code 999")
    else:
        soupjob = BeautifulSoup(respjob.text, "html5lib")
        codesoupjob = soupjob.find("code", {"id": "jobDescriptionModule"})
        jsonjob = json.loads(codesoupjob.contents[0])
        print(jsonjob['description'])
        print(jsonjob['skillsDescription'])
        #with open('/Users/jayers/Temp/ajobstest.html', 'a') as file:
        with open('d:\Temp\ajobstest.html', 'a') as file:
            file.write(jsonjob['description'])
            if jsonjob['skillsDescription'] is not None:
                file.write(jsonjob['skillsDescription'])
            file.write('<hr>')












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







#import the tools
import glob, os



#loop to concat a few files to create a file to do nlp on
for filepath in glob.glob("/Users/jayers/Temp/Jobpost[0-0][0-3][0-9].body.txt"):
    print(filepath)
    jobtext = open(filepath, 'r', encoding='utf-8', errors='ignore')
    #print(jobtext.read())
    with open("/Users/jayers/Temp/concatfile.txt", "a") as myfile:
        myfile.write(jobtext.read())
    



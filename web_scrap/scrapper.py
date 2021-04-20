from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import urllib.request
import csv


url = "https://www.acog.org/womens-health/faqs/nutrition-during-pregnancy"

def scrap_data(url=url):
    ans = None
    count = 0

    #create a .csv file
    resume_csv = open("Chatbot_data.csv",'w')
    csv_writer = csv.writer(resume_csv)
    csv_writer.writerow(['questions','answers'])

    #target the url and get the data
    source = requests.get(url).text
    #getting the page
    page = BeautifulSoup(source,'lxml')
    # getting all button tag
    questions = page.find_all('button',class_="accordion-trigger")
    #getting the div tag
    content = page.find_all('div',class_="accordion-content wysiwyg-content")

    for i in range(41):
        qsn_adrs = questions[i]
        qsn = qsn_adrs.text
        content_p = content[i].find_all('p')
        kk_ans = str()
        for j in content_p:
            ans = j.text
            kk_ans+=ans
        csv_writer.writerow([qsn,kk_ans])
        count +=1
        print(f'done {qsn} ||======> {count}')

    print(count)
    resume_csv.close()


if __name__=="__main__":

    scrap_data(url)

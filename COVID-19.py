# scraping
import urllib.request # import urllib.request for get url's html data
import lxml.html # import lxml.html for scraping

url = "https://stopcovid19.metro.tokyo.lg.jp/" # Define a variable called "url" and assign "url" the URL of the homepage of COVID-19 in Tokyo

html = urllib.request.urlopen(url).read() # Open and read "url", and assign "html" "url"'s HTML data

tree = lxml.html.fromstring(html) # get html and assign "tree" html'data

def get_text_from_xpath(xpath): # define the function "get_text_from_xpath(xpath)"
    list = tree.xpath(xpath) # get list data from xpath
    element = list[0] # This time, the length of the list is 1, so only the beginning is taken
    text = element.text # get text
    non_blank_text = text.replace(' ', '').replace('\n','') # delete blank and indention from text
    return non_blank_text

last_update = get_text_from_xpath('//*[@id="app"]/div[1]/div/main/div/div/div[1]/div[2]/time') # using function the function "get_text_from_xpath(xpath)"
new_patient_number = get_text_from_xpath('//*[@id="app"]/div/div/main/div/div/div[3]/div[3]/div/div/div[1]/div/span') 
tested_number = get_text_from_xpath('//*[@id="app"]/div[1]/div/main/div/div/div[3]/div[9]/div/div/div[1]/div/span')
positive_rate = get_text_from_xpath('//*[@id="app"]/div[1]/div/main/div/div/div[3]/div[7]/div/div/div[1]/div/span')

print("COVID-19 in Tokyo Last update " + last_update)
print("Number of new patient: " + new_patient_number + " by day")
print("Number of people tested: " + tested_number  + " by day")
print("Positive rate: " + positive_rate  + " by day")

# making histgram
import requests
import io
import pandas as pd # for using dataframe
import matplotlib.pyplot as plt # for ploting histgram

url = 'https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv' # define url which is used to download csv file

res = requests.get(url).content # i dont know, maybe get csv

df = pd.read_csv(io.StringIO(res.decode('utf-8')), header=0, index_col=0) # make datagrame

df_date = df.iloc[:,3].astype("datetime64") # Extract date only

fig = plt.figure(figsize=(30, 10)) # setting graph size

df_date.groupby([df_date.dt.month, df_date.dt.day]).count().plot(kind="bar") # i dont know, maybe cont each date and making histgram

plt.title("Number of new COVID-19 patient in 2020") # setting title

plt.xlabel('date') # setting xlabel

plt.ylabel('Number of new COVID-19 patient') # setting ylabel

plt.rcParams["font.size"] = 20 # setting font size

plt.show() # show histgram

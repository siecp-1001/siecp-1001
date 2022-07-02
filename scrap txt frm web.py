from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series,DataFrame
from ipywidgets import FloatProgress
from time import sleep
from IPython.display import display 
import re 
import pickle
url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
result = requests.get(url)
c = result.content
soup = BeautifulSoup(c,"lxml")
summary = soup.find('div',{'class':'article'})
moviename = []
cast = []
description = []
rating = []
ratingoutof = []
year = []
genre = []
movielength = []
rot_audscore = []
rot_avgrating = []
rot_users = []
rgx = re.compile('[%s]' % '()')
f = FloatProgress(min=0, max=250)
display(f)
for row,i in zip(summary.find('table').
findAll('tr'),range(len(summary.find('table').findAll('tr')))):
    for sitem in row.findAll('span',{'class':'secondaryInfo'}):
        s = sitem.find(text=True)
        year.append(rgx.sub('', s))
    for ritem in row.findAll('td',{'class':'ratingColumnimdbRating'}):
        for iget in ritem.findAll('strong'):

            rating.append(iget.find(text=True))
            ratingoutof.append(iget.get('title').split(' ', 4)[3])
    for item in row.findAll('td',{'class':'titleColumn'}):
        for href in item.findAll('a',href=True):
            moviename.append(href.find(text=True))
            rurl = 'https://www.rottentomatoes.com/m/'+ href.find(text=True)
            try:
                rresult = requests.get(rurl)
            except requests.exceptions.ConnectionError:
                status_code = "Connection refused"
            rc = rresult.content
            rsoup = BeautifulSoup(rc)
            try:
                rot_audscore.append(rsoup.find('div',{'class':'meter-value'}).find('span',{'class':'superPageFontColor'}).text)
                rot_avgrating.append(rsoup.find('div',{'class':'audience-info hidden-xssuperPageFontColor'}).find('div').contents[2].strip())
                rot_users.append(rsoup.find('div',{'class':'audience-info hidden-xssuperPageFontColor'}).contents[3].contents[2].strip())
            except AttributeError:
                rot_audscore.append("")
                rot_avgrating.append("")
                rot_users.append("")
                cast.append(href.get('title'))
                imdb = "http://www.imdb.com" + href.get('href')
             
            try:
                iresult = requests.get(imdb)
                ic = iresult.content
                isoup = BeautifulSoup(ic)
                
                description.append(isoup.find('div',{'class':'summary_text'}).find(text=True).strip())
                
                genre.append(isoup.find('span',{'class':'itemprop'}).find(text=True))
                
                movielength.append(isoup.find('time',{'itemprop':'duration'}).find(text=True).strip())

            except requests.exceptions.ConnectionError:
                   description.append('')
                   genre.append('')
                   movielength.append("")
                   sleep(.1)
                   f.value = i
moviename=Series(moviename)
cast = Series(cast)
description =Series(description)
rating = Series(rating)
ratingoutof=Series(ratingoutof)
year=Series(year)
genre=Series(genre)
movielength=Series(movielength)
rot_audscore=Series(rot_audscore)
rot_avgrating=Series(rot_avgrating)
rot_users = Series(rot_users)   
imdp_df=pd.concat([moviename,year,description,genre,movielength,cast,rating,ratingoutof,rot_audscore,rot_avgrating,rot_users],axis=1)    
imdp_df.columns = ['moviename','year','description','genre','movielength','cast','imdb_rating','imdb_ratingbasedon','tomatoes_audscore','tomatoes_rating','tomatoes_ratingbasedon']
imdp_df['rank']=imdp_df.index +1
imdp_df.head(1)
imdp_df.to_csv("imdbdataexport.csv")
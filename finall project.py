import re
import bs4
import requests
import mysql.connector

# This program takes over 2000 cars name and price and save them into a database

cnx = mysql.connector.connect( user = 'root' , password = '' ,
                                     host = '127.0.0.1' , database = 'mydatabase' )
                                     
cursor = cnx.cursor()

    
n = 1

while n < 70 :

    link = "https://bama.ir/car/all-brands/all-models/all-trims?page=" + str(n)

    r = requests.get (link)

    soup = bs4.BeautifulSoup( r.text , "html.parser" )

    cars = soup.find_all('h2' , attrs = {'class' : 'persianOrder' , 'itemprop' : 'name'})

    costs = soup.find_all('span' , attrs = { 'itemprop' : 'price'})

    for i in range (0 , 30):
        query = "INSERT INTO cars VALUES (%s , %s)"
        values = ( re.sub ( r'\s+' , ' ' , cars[i].text).strip() , re.sub ( r'\s+' , ' ' , costs[1].text).strip())
        cursor.execute(query,values)
        cnx.commit()

    n += 1




cnx.close()




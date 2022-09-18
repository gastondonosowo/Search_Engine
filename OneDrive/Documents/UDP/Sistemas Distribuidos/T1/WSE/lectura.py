from bs4 import BeautifulSoup
import requests
import os

f = open('/home/donoso/Documents/user-ct-test-collection-01.txt')
i = 0
salida = open("/home/donoso/Documents/init.sql", "w")
salida.write("CREATE TABLE T1(id SERIAL , title VARCHAR, description VARCHAR, keywords VARCHAR, web VARCHAR PRIMARY KEY);" + os.linesep)
while True:
    datos = f.readline()
    if len(datos) > 0:
        i += 1
        if datos.find("http://") != -1:
            datos = datos.split()
            try:
                url = datos[-1]
                r = requests.get(url, verify=False, timeout=5)
                soup = BeautifulSoup(r.content, "html.parser")
                kw = soup.find("meta", attrs={'name': 'keywords'})
                description = soup.find("meta", attrs={'name': 'description'})
                title = soup.title.string
                title = title.strip()
                if kw and title and description:
                    kw = str(kw).split('\"', 2)[1]
                    description = str(description).split('\"', 2)[1]
                    kw = kw.strip()
                    description = description.strip()
                    print("si", i)
                    query = "INSERT INTO T1 (title, description, keywords, web) VALUES( '"+str(title)+"', '"+str(description)+"', '"+str(kw)+"', '"+str(url)+"');"
                    salida.write(query + os.linesep)
            except:
                print("ERROR")
    else:
        break
salida.close()

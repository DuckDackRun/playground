import psycopg2
import psycopg2.extras
#import src.components.layout import createlayout
from dash import Dash, html, dcc
#from dash_bootstrap_components.theme import BOOTSTRAP
import pandas as pd
import csv
import time
import os

cur=None
conn=None
try:
    conn=psycopg2.connect(host ="postgres.tut.jbb.ghsq.de", 
                        dbname = "gruppe1", 
                        user = "gruppe1", 
                        password = "peirieBei4Aeb9sae4neThiSangechee",
                        #port="5432"
                        )

    cur= conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #<- sorgt dafür, dass data mittels [attribut] zugreifbar ist

    cur.execute("""CREATE TABLE IF NOT EXISTS StatGender (
        Id INT PRIMARY KEY,
        Bezirk VARCHAR(255),
        Gestohlen Int,
        Gender VARCHAR(16)
        
        );""") 
    
    cur.execute("""CREATE TABLE IF NOT EXISTS StatJahr (
        Id INT PRIMARY KEY,
        Jahr VARCHAR(255),
        Gestohlen Int,
        wtf VARCHAR(255)

        
        );""") 
    
    #cur.execute("INSERT INTO StatGender(Id, Bezirk, Gestohlen,Gender) VALUES (3,'Reinickendorf', 161,'Herr'),(5,'Mzahn', 51,'Herr'),(65,'Entenhausen', 212,'Herr'),(78,'pfurzheim', 41,'Herr');")
  
    cur.execute("SELECT * FROM StatGender;")
    data=cur.fetchall()
    print(data)

    conn.commit()
    
except Exception as error:
  print("error, du bist schlimm,", error)
  data=[]
finally:
    if cur is not None:
        cur.close()
  
    if conn is not None:
        conn.close()

print("Hallo")
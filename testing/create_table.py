import requests
import json
import mysql.connector as mysql

## run each section sequentially
## Get keys for col names
details = requests.request('GET', 'http://www.themealdb.com/api/json/v1/1/lookup.php?i=53016').text
detail_json = json.loads(details)
keys = [keys for keys in detail_json['meals'][0].keys()]

## connect and create db  ===============================
db = mysql.connect(
    host = "192.168.3.70",
    user = "root",
    passwd = "challenge",
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE api_agg")

## connect to db and create table from keys  ================================
db = mysql.connect(
    host = "192.168.3.70",
    user = "root",
    passwd = "challenge",
    database = "api_agg"
)

cursor = db.cursor()

cursor.execute(f"""CREATE TABLE meals ({keys[0]} varchar(255),
                    {keys[1]} varchar(255),
                    {keys[2]} varchar(255),
                    {keys[3]} varchar(255),
                    {keys[4]} varchar(255),
                    {keys[5]} varchar(255),
                    {keys[6]} varchar(255),
                    {keys[7]} varchar(255),
                    {keys[8]} varchar(255),
                    {keys[9]} varchar(255),
                    {keys[10]} varchar(255),
                    {keys[11]} varchar(255),
                    {keys[12]} varchar(255),
                    {keys[13]} varchar(255),
                    {keys[14]} varchar(255),
                    {keys[15]} varchar(255),
                    {keys[16]} varchar(255),
                    {keys[17]} varchar(255),
                    {keys[18]} varchar(255),
                    {keys[19]} varchar(255),
                    {keys[20]} varchar(255),
                    {keys[21]} varchar(255),
                    {keys[22]} varchar(255),
                    {keys[23]} varchar(255),
                    {keys[24]} varchar(255),
                    {keys[25]} varchar(255),
                    {keys[26]} varchar(255),
                    {keys[27]} varchar(255),
                    {keys[28]} varchar(255),
                    {keys[29]} varchar(255),
                    {keys[30]} varchar(255),
                    {keys[31]} varchar(255),
                    {keys[32]} varchar(255),
                    {keys[33]} varchar(255),
                    {keys[34]} varchar(255),
                    {keys[35]} varchar(255),
                    {keys[36]} varchar(255),
                    {keys[37]} varchar(255),
                    {keys[38]} varchar(255),
                    {keys[39]} varchar(255),
                    {keys[40]} varchar(255),
                    {keys[41]} varchar(255),
                    {keys[42]} varchar(255),
                    {keys[43]} varchar(255),
                    {keys[44]} varchar(255),
                    {keys[45]} varchar(255),
                    {keys[46]} varchar(255),
                    {keys[47]} varchar(255),
                    {keys[48]} varchar(255),
                    {keys[49]} varchar(255),
                    {keys[50]} varchar(255),
                    {keys[51]} varchar(255),
                    {keys[52]} varchar(255)
        )""")



"""
{keys[0]} varchar(255), 
        {keys[1]} varchar(255), {keys[2]} varchar(255), {keys[3]} varchar(255),
        {keys[4]} varchar(255), {keys[5]} varchar(255), {keys[7]} varchar(255),
        {keys[9]} varchar(255), {keys[10]} varchar(255), {keys[11]} varchar(255),
        {keys[12]} varchar(255), {keys[13]} varchar(255), {keys[14]} varchar(255),
        {keys[15]} varchar(255), {keys[16]} varchar(255), {keys[17]} varchar(255),
        {keys[18]} varchar(255), {keys[19]} varchar(255), {keys[20]} varchar(255),
        {keys[25]} varchar(255), {keys[24]} varchar(255), {keys[23]} varchar(255),
        {keys[26]} varchar(255), {keys[27]} varchar(255), {keys[28]} varchar(255),
        {keys[29]} varchar(255), {keys[30]} varchar(255), {keys[31]} varchar(255),
        {keys[32]} varchar(255), {keys[33]} varchar(255), {keys[34]} varchar(255),
        {keys[35]} varchar(255), {keys[36]} varchar(255), {keys[37]} varchar(255),
        {keys[38]} varchar(255), {keys[39]} varchar(255), {keys[40]} varchar(255),
        {keys[41]} varchar(255), {keys[42]} varchar(255), {keys[43]} varchar(255),
        {keys[44]} varchar(255), {keys[45]} varchar(255), {keys[46]} varchar(255),
        {keys[47]} varchar(255), {keys[48]} varchar(255), {keys[49]} varchar(255)
        """
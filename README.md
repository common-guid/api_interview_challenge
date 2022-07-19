#MealDB API Project
Documentation for setup and use.
---

### Technologies 

 - Python [3 files]
     -  create_db.py to setup
     - aggregate.py to collect items from mealDB
     - make_request.py to make request to our database
 - MySQL on docker 
 - Ubuntu Server host
 - Developed and tested on Pop_OS 22.04 
---

# Setup

Pull and run MySQL container

```
docker run -d --name mysql -p 3306:3306 -v ~/mysql/data:/var/lib/mysql mysql/mysql-server
```

     -  Review the docker startup logs to find the randomly generated MySQL password.
Log into the MySQL container 

```
docker exec -it mysql bash
```

Execute the commands below in order to create user account for Python to connect

```
mysql> CREATE USER 'root'@'%' IDENTIFIED BY 'challenge';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
mysql> FLUSH PRIVILEGES;
```

 MySQL is ready

---

### Python

> Note: any item between angles \[“<xxx>”\] is user supplied

In each of the 3 python files change the user, password, host ip, and add database name as seen below

```
host = "<host ip>",
user = "root",
passwd = "<password>",
database = "<database>"
# in the aggregate.py file
engine = create_engine(
    'mysql+mysqlconnector://root:<password>@<ip>/<database>')
```

Now run each of the 3 sections in the create_db.py file sequentially.

Everything should now be setup and ready for use.

---

# Use

The application has two py files. 

 - aggregate.py generates requests to mealDB and collects the response for upload to MySQL while displaying the result on the Flask page
 - make_request.py makes requests to the MySQL database we own
**agregate.py** has 4 endpoints which can be used to proxy requests to the mealDB.

```
http://{Flask_URL}/search_name/<name_of_dish>
http://{Flask_URL}/main_ingredient/<ingredient>
http://{Flask_URL}/category/<category>
http://{Flask_URL}/region/<region>
```

 -  Data returned is used to generate more requests to the mealdb by ‘idMeal’ to get detailed information about each meal
 - This detailed data is split into two tables - one for ‘idMeal’ and cooking instructions, and another for everything [minus instructions]
     - this was due to the length of instructions causing problems on occasion
 -  Data is then sent to MySQL and displayed on flask page
**make_request.py** has 4 endpoints for searching the MySQL database create previously.

```
http://{Flask_URL}/search_name/<name_of_dish>
http://{Flask_URL}/search_main_ingredient/<ingredient>
http://{Flask_URL}/search_instructions/<id>
http://{Flask_URL}/filter_by_ingredients?ingredient1=<item_1>&ingredient2=<item_2>&and_or_or=<choice>
```

This returns data from the MySQL query.

### Opportunities For Improvements and Enhancements

 1. Error Handling
 2. Duplicate filter for write to database
 3. SQLi prevention - input sanitization
 4. html form allowing user to see data returned and either save to MySQL or drop the data after reviewing

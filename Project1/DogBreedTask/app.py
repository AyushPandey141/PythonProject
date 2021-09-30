# Project:RESTFUL API SERVER
# Program By:Ayush Pandey
# Email Id:1805290@kiit.ac.in
# DATE:27-Sept-2021
# Python Version:3.7
# CAVEATS:None
# LICENSE:None

from flask import Flask, request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import jsonify
import pymongo
import json
import requests

app = Flask(__name__)

connection = pymongo.MongoClient("mongodb://localhost:27017")


class ayush_json:
    def check_url(self, url):
        try:
            url = requests.get(url)
            return True
        except:
            return False

    def read_url(self, url):
        url = requests.get(url)
        return url.json()


url = "https://api.thedogapi.com/v1/breeds"
check = []
s = ayush_json()
# Checking whether url is present or not
if(s.check_url(url)):
    see = s.read_url(url)
    flag = 0
    for i in see:
        with open("Breed.json", "w") as f:
            check.append(i)
            json.dump(check, f)
else:
    print("URL NOT PRESENT")


class Ayush_Mongo:
    connection = pymongo.MongoClient("mongodb://localhost:27017")

    def mongo_connection(self):
        # Checking whether connection is successful or not
        if self.connection:
            return True
        else:
            return False

    def db_exists(self, db_name):
        if db_name in self.mongodb_list():
            return True
        else:
            return False

    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            # For inserting data into the document
            self.connection[db_name][new_collection].insert_many(data)
            return True
        else:
            return("error")

    def display_all(self, db_name, collection_name):
        result = []
        if(self.connection):
            # Getting the documents from the collection
            see = self.connection[db_name][collection_name].find({})
            for data in see:
                # As there were many fields which were either not present or empty
                # And by using this out of 172 documents less than 10 were printed
                """if('breed_group' in data and 'bred_for' in data and 'origin' in data):
                    # print(data['breed_group'])
                    # print(data['bred_for'])
                    # print(data['image']['url'])
                    a = data['breed_group']
                    s = data['bred_for']
                    d = data['image']['url']
                    f = data['origin']
                    q = []
                    q.append(a)
                    q.append(s)
                    q.append(d)
                    q.append(f)
                    result.append(q)"""
                q = []
                if('breed_group' in data and data['breed_group'] != ""):
                    a = data['breed_group']
                else:
                    a = "Not Present"
                if('bred_for' in data and data['bred_for'] != ""):
                    s = data['bred_for']
                else:
                    s = "Not Present"
                if('origin' in data and data['origin'] != ""):
                    f = data['origin']
                else:
                    f = "Not Present"
                d = data['image']['url']
                q.append(a)
                q.append(s)
                q.append(d)
                q.append(f)
                result.append(q)

            self.a = []
            self.s = []
            self.d = []
            self.f = []
            # print(result[4][1])
            for i in range(len(result)):
                self.a.append(result[i][0])
                self.s.append(result[i][1])
                self.d.append(result[i][2])
                self.f.append(result[i][3])
            # print(self.a)
            return(self.a, self.s, self.d, self.f)
        else:
            print("Error")


# For printing the data in the tabular form
@app.route('/')
def show():
    q = Ayush_Mongo().display_all("DETAIL", "Values")
    a = q[0]
    s = q[1]
    d = q[2]
    f = q[3]
    finalresult = []
    for i in range(len(a)):
        q = []
        q.append(a[i])
        q.append(f[i])
        q.append(s[i])
        q.append(d[i])
        finalresult.append(q)
    """finalresult = []
    finalresult.append(a)
    finalresult.append(f)
    finalresult.append(s)
    finalresult.append(d)"""
    return render_template('index.html', z=finalresult, length=len(a))

# Creating a new collection for storing the new data


def new_document():
    q = Ayush_Mongo().display_all("DETAIL", "Values")
    a = q[0]
    s = q[1]
    d = q[2]
    f = q[3]
    for i in range(len(a)):
        q = []
        q.append(a[i])
        q.append(f[i])
        q.append(s[i])
        q.append(d[i])
        db = connection['New_Details']
        Values = db['Values']
        q = Values.insert({'Breed': q[0], 'Origin': q[1],
                           'Purpose': q[2], 'Image': q[3]})


# Displaying the result for those whose all elements in the document are present
@app.route('/All')
def get():
    db = connection['New_Details']
    Values = db['Values']
    q = Values.find({}, {'_id': 0})
    ans = []
    for i in q:
        if(i['Breed'] == "Not Present" or i['Origin'] == "Not Present" or i['Purpose'] == "Not Present"):
            continue
        else:
            ans.append(i)
    # print(ans)
    return render_template('Updated.html', z=ans, length=len(ans))


@app.route('/Insert')
def get1():
    return render_template('Insert.html')


@app.route('/updating', methods=["POST"])
def get2():
    if request.method == 'POST':
        a = request.form['breed']
        f = request.form['origin']
        s = request.form['purpose']
        d = request.form['image']
        db = connection['New_Details']
        Values = db['Values']
        Values.insert({'Breed': a, 'Origin': f, 'Purpose': s, 'Image': d})
    q = Values.find({}, {'_id': 0})
    ans = []
    for i in q:
        if(i['Breed'] == "Not Present" or i['Origin'] == "Not Present" or i['Purpose'] == "Not Present"):
            continue
        else:
            ans.append(i)
    # print(ans)
    return render_template('Updated.html', z=ans, length=len(ans))


# I have used this API->https://api.thedogapi.com/v1/breeds
# I have saved this API as Breed.json in my machine
with open('Breed.json') as f:
    data = json.load(f)
ob = Ayush_Mongo()
# Will return True is connection is successful
print(ob.mongo_connection())
# Used for inserting the data in the collection named as Values
print(ob.create_new_collection("DETAIL", "Values"))
# For printing all the documents present in the collection
#print(ob.display_all("DETAIL", "Values"))
# ob.show()

new_document()

if __name__ == '__main__':
    app.run(debug=True, port=5000)

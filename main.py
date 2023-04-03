from pymongo import MongoClient
import pprint

# Para conectar com o MongoDB, use a string de conexão padrão: mongodb://<user_name>:<password>@localhost:27017/<database_name>?authSource=admin
conection_string = "mongodb://root:123456@localhost:27017"

# Conectando ao MongoDB
client = MongoClient(conection_string)

# Listando os bancos de dados
dbs = client.list_database_names()
pprint.pprint(dbs)


#mostrando as colections do banco de dados
test = client['pythonmongodb']
colections = test.list_collection_names()
pprint.pprint(colections)

def insert_pythonmongodb_doc(name, password, email):
    colection = test.user
    pythonmongodb_document = {"user_name": name,
                                  "passw":password,
                                  "email": email}
    insert_id = colection.insert_one(pythonmongodb_document).inserted_id
    print(insert_id)

# insert_pythonmongodb_doc("teste", "123456", "teste@gmail.com")

#Creando um banco de dados nuevo
production = client['production']

#create a collection
person_collection = production.person


#incluir varios documentos
def create_documents():
    firs_name = {"Tim", "John", "Mary", "Jane", "Peter", "Paul", "Mark", "Sarah", "Kate", "Sara"}
    last_name = {"Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"}
    ages = {18, 19, 20, 21, 22, 23, 24, 25, 26, 27}
    docs = []
    for firs_name, last_name, ages in zip(firs_name, last_name, ages):
        person_document = {"first_name": firs_name,
                           "last_name": last_name,
                           "age": ages}
        docs.append(person_document)
    
    person_collection.insert_many(docs)

#create_documents()

def find_all_peoples():
    peoples = person_collection.find()
    for people in peoples:
        pprint.pprint(people)

#find_all_peoples()
def find_people_by_name(name):
    peoples = person_collection.find({"first_name": name})
    for people in peoples:
        pprint.pprint(people)
        
#find_people_by_name("Tim")

def count_people():
    peoples = person_collection.count_documents({})
    print(peoples)

count_people()



def get_person_by_id(person_id):
    from bson.objectid import ObjectId
    
    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    pprint.pprint(person)
    
get_person_by_id('6429b41cb71b185b4a48ac40')

# $and = and

# $gt = greater than
# $lt = less than
def get_age_range(min_age, max_age):
    # query = {"$and":[
    #                 {"age": {"$gte": min_age}},
    #                 {"age": {"$lte": max_age}}
    #                 ]}
        
    # people = person_collection.find(query).sort("age")
    
    people = person_collection.find({"age": {"$gte": min_age, "$lte": max_age}}).sort("age") 
    for person in people:
        pprint.pprint(person)

get_age_range(20, 25)
import pymongo
if __name__=="__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017")
    name=input("enter your database name")
    db=client[name]
    collection=db['list_items']
    f=open("file.txt",'+a')

    num=int(input("enter the number of items to be added"))
    for i in range(1,num+1):
        key=input(f"enter item {i}")
        value=input(f"enter value of {i}th item")
        f.write(f"{key} --- {value}")
        f.write("\n")
    
    
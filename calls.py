import requests ;
import json ;
from dotenv import load_dotenv ;
import os ;
load_dotenv()

key = os.getenv("SECRET_TOKEN")
URLforDraft = "https://"+os.getenv("STORE_NAME")+"/admin/api/2022-10/draft_orders.json"
idd = 6038008168634
h = {"X-Shopify-Access-Token":key, "Content-Type":"application/json"}
d = {"draft_order":{"line_items":[{"title":"Custom Tee","price":"5.00","quantity":2}],"customer":{"id":idd},"use_customer_default_address":'true'}}

def getCustomer(email):
    url = "https://"+os.getenv("STORE_NAME")+"/admin/api/2022-10/customers/search.json?query="+email 
    x = requests.get(url,headers=h)
    return x.json()
def createDraftOrder() :
    return

#x = requests.post(URLforDraft,data=json.dumps(d),headers=h)
#print(x.status_code)

if __name__ == "__main__" :
    response = getCustomer("philiptester@gmail.com")
    print(response["customers"][0]["id"])


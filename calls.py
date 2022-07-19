import requests ;
import json ;
from dotenv import load_dotenv ;
import os ;
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow , Flow
from googleapiclient import discovery

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credentials.json"

key = os.getenv("SECRET_TOKEN")
URLforDraft = "https://"+os.getenv("STORE_NAME")+"/admin/api/2022-10/draft_orders.json"


def getCustomer(email):
    url = "https://"+os.getenv("STORE_NAME")+"/admin/api/2022-10/customers/search.json?query="+email 
    x = requests.get(url,headers=h)
    return x.json()

def createDraftOrder(customerid,title,depositYN,price) :
    d = {"draft_order":{"line_items":[{"title":title+" "+depositYN,"price":str(price),"quantity":1}],"customer":{"id":customerid},"use_customer_default_address":'true'}}
    h = {"X-Shopify-Access-Token":key, "Content-Type":"application/json"}
    x = requests.post(URLforDraft,data=json.dumps(d),headers=h)
    return x

def getOrders():    
    credentials = None
    service = discovery.build('sheets', 'v4', credentials=credentials)
    spreadsheet_id = '1gr7wB9hHDgTA3tg3dfUjYkVsNoJPF7Ltwgb9VeHsp-0'
    range_ = 'B2:Q7'
    value_render_option = 'FORMATTED_VALUE'
    date_time_render_option = 'SERIAL_NUMBER'

    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_, valueRenderOption=value_render_option, dateTimeRenderOption=date_time_render_option)
    response = request.execute()
    return response

#x = requests.post(URLforDraft,data=json.dumps(d),headers=h)
#print(x.status_code)

if __name__ == "__main__" :
    #customerEmail = input("customer Email Please: ")
    #itemDescription = input("Enter Item Description: ")
    #response = getCustomer(customerEmail)
    #customerID = response["customers"][0]["id"]
    #res = createDraftOrder(customerID,itemDescription,"DEPOSIT",Price)
    #print(res.status_code)
    print(getOrders())



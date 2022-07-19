import requests ;
import json ;
from dotenv import load_dotenv ;
import os ;
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow , Flow
from googleapiclient import discovery

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credentials.json"

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

key = os.getenv("SECRET_TOKEN")
URLforDraft = "https://"+os.getenv("STORE_NAME")+"/admin/api/2022-10/draft_orders.json"
idd = 6038008168634
h = {"X-Shopify-Access-Token":key, "Content-Type":"application/json"}
d = {"draft_order":{"line_items":[{"title":"Custom Tee","price":"5.00","quantity":2}],"customer":{"id":idd},"use_customer_default_address":'true'}}

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

# The ID of the spreadsheet to retrieve data from.
    spreadsheet_id = '1gr7wB9hHDgTA3tg3dfUjYkVsNoJPF7Ltwgb9VeHsp-0'  # TODO: Update placeholder value.

# The A1 notation of the values to retrieve.
    range_ = 'B2:Q7'  # TODO: Update placeholder value.

# How values should be represented in the output.
# The default render option is ValueRenderOption.FORMATTED_VALUE.
    value_render_option = 'FORMATTED_VALUE'  # TODO: Update placeholder value.

# How dates, times, and durations should be represented in the output.
# This is ignored if value_render_option is
# FORMATTED_VALUE.
# The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].
    date_time_render_option = 'SERIAL_NUMBER'  # TODO: Update placeholder value.

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
    getOrder()


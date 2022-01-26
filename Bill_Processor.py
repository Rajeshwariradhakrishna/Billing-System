import glob
import pymysql
import os
import shutil
import json 
import atexit
import uuid

#####################################PASSING THE FILE FROM PYTHON TO DB################################
def LoadBillDataToDB(p_conn,p_json):
    l_data = json.loads(p_json)
    cursor = p_conn.cursor()   
    l_sql = "insert into BillHeader values({},{},STR_TO_DATE(\"{}\",\"%Y%m%d%H%i%S\"),{});".format(l_data["bill_id"],l_data["store_id"],l_data["bill_date"],l_data["bill_total"])
    cursor.execute(l_sql)
    
    for l_bill_details in l_data["bill_details"]:
        l_bill_det_sql = "insert into BillDetail values(\"{}\",{},{},{},{});".format(str(uuid.uuid4()), l_data["bill_id"],l_bill_details["ProductID"],l_bill_details["Quantity"],l_bill_details["LineTotal"])
        #print(l_bill_det_sql)
        cursor.execute(l_bill_det_sql) 
    p_conn.commit()

 #Error table   
    for l_errorbill_details in l_data["bill_details"]:
        l_errorbill_det_sql = "insert into Error values({},{},STR_TO_DATE(\"{}\",\"%Y%m%d%H%i%S\"),{});".format(l_data["bill_id"],l_data["store_id"],l_data["bill_date"],l_data["bill_total"])        #print(l_bill_det_sql)
        cursor.execute(l_errorbill_det_sql) 
    p_conn.commit()
    
#def error_bills():
 
##############LOCATION AND CONNECTION MADE HERE##################################
l_src_folder = "C:\\Python\\BillingSystem\\Bills\\"
tgt_folder = "C:\\Python\\BillingSystem\\Processed\\"
error_folder = "C:\\Python\\BillingSystem\\ErrorBills\\"

conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='sepsales')
cursor = conn.cursor()
bill_total = 0

myquery = "SELECT (UNIT_PRICE * %s) FROM PRODUCTS WHERE PROD_ID = %s" #####used this query to get unitprice from db so I CAN CALL LINETOTAL
atexit.register(print, "Exiting Python Script")

#####################GETTING EACH FILE FROM BILLS FOLDER AND CAL BILLTOTAL AND LINETOTAL#################
d_billdtls = []
l_files = glob.glob(l_src_folder+"*.json") #glob.glob()-fetching file using pattern matching

for curr_file in l_files:
   #print (curr_file)
    curr_filename = os.path.basename(curr_file) #get filename without extension
    print (curr_filename, "is open")
    
    with open(curr_file, 'r') as file: #The with statement in Python is used for resource management and exception handling. You'd most likely find it when working with file streams
        filedata = file.read()
        #print (filedata)
        json_object = json.loads(filedata)
        billdtls = json_object["bill_details"]
        print ("List of keys : ", billdtls.keys())
        #print (billdtls.values())
        
        for key, value in billdtls.items():
            if int(key) <= 25:
                conn.ping() #to check if the mysql connection is active 
                print (key, "- value is being processed")
                cursor.execute(myquery, (value, key))
                final_value = cursor.fetchone()[0]    
                
                l_line_element = { "ProductID":key
                                  ,"Quantity":value
                                  ,"LineTotal":int(final_value)}

                d_billdtls.append(l_line_element)
                
                bill_total = bill_total + final_value
                
                #error table and error folder
            else:
                print("Prod_id is out of range")   
                
                billid = json_object["bill_id"]
                storeid = json_object["store_id"]
                billdate = json_object["bill_date"]
        
                l_errordata = {"bill_id": billid
                , "store_id": storeid
                , "bill_date": billdate
                , "bill_total" : int(bill_total)
                , "bill_details": d_billdtls}   
        
                l_data1 = json.dumps(l_errordata,indent=4)        
                LoadBillDataToDB(conn,l_errordata1)
                shutil.move(curr_file, error_folder)            
            
        file.close()          
        print (curr_filename, "is closed")
        
        billid = json_object["bill_id"]
        storeid = json_object["store_id"]
        billdate = json_object["bill_date"]
        
        l_data = {"bill_id": billid
        , "store_id": storeid
        , "bill_date": billdate
        , "bill_total" : int(bill_total)
        , "bill_details": d_billdtls}   
        
        l_data1 = json.dumps(l_data,indent=4)        
        LoadBillDataToDB(conn,l_data1)
    
        with open(curr_file,'r+') as myfile:
            newdata = myfile.read()
            myfile.seek(0)
            myfile.truncate()
            
            new_file = open(curr_file, "w")
            json.dump(l_data,new_file,indent=4)
            new_file.close()    
        
        shutil.move(curr_file, tgt_folder)       
        print (curr_filename, "has been processed and moved to target location")
    break
    
    
    
    
    
    
    
    
    
    
    

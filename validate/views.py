from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from excelvalidate.settings import MEDIA_ROOT
import os
import pandas as pd
import numpy as np
import re
from .models import *
from xlsxwriter.utility import xl_rowcol_to_cell  #used to return index address of excel sheet
import datetime
from django.http import JsonResponse

# Create your views here.

@csrf_exempt #for accepting request from postman
def inputexcel(request): #function of accepting excelsheet and returing error json data
    if request.method == "POST":
        data = request.FILES.get('excelfile')
        if data and data.name.endswith('.xlsx'):
            fileloc = os.path.join(MEDIA_ROOT,"excelsheets")
            if(os.path.isdir(fileloc) is False):
                os.makedirs(fileloc)
            fs = FileSystemStorage(location=fileloc)
            fs.save(data.name, data)  #saving excel file in media in native way for reading it
            df = pd.read_excel(os.path.join(MEDIA_ROOT,"excelsheets",data.name), sheet_name="Orders",engine='openpyxl')
            df = df.dropna(axis=0,how='all') #ignoring empty rows from data
            df = df.dropna(axis=1,how='all') #ignoring empty columns from data
            columns = len(df.columns)
            rows = len(df)
            #print("Rows : "+str(rows))
            #print("Columns : "+str(columns))
            allerror = []
            bulk_create_data = []
            for row in range(rows):
                order_detail = []
                count = 0
                for col in range(columns):
                    if col==0:
                        try:
                            if re.match(r'^[0-9_]*$',str(int(df.loc[row][col]))):  #use of regrex for allowing only digits and underscore in value
                                count += 1
                                order_detail.append(df.loc[row][col])
                                #print(df.loc[row][col])
                            else:
                                #error[xl_rowcol_to_cell(row+1,col)]='value Should Contain only Numerical Value and Underscore'
                                error = {}
                                error['address']=xl_rowcol_to_cell(row+1,col)
                                error['error']='value Should Contain only Numerical Value and Underscore'
                                allerror.append(error)
                        except:
                                #error[xl_rowcol_to_cell(row+1,col)]='value Should Contain only Numerical Value and Underscore'
                                error = {}
                                error['address']=xl_rowcol_to_cell(row+1,col)
                                error['error']='value Should Contain only Numerical Value and Underscore'
                                allerror.append(error)
                    elif col==1:
                        try:
                            date = df.loc[row][col]
                            date_new = str(date.strftime("%d"))+str("-")+str(date.strftime("%b"))+str("-")+str(date.strftime("%Y"))  #converting the format of date in required format
                            count += 1
                            order_detail.append(date.strftime("%Y-%m-%d"))
                            order_detail.append(date_new)
                        except:
                            #error[xl_rowcol_to_cell(row+1,col)]='Invalid Date Format,Format should be 01-Jan-2011'
                            error = {}
                            error['address']=xl_rowcol_to_cell(row+1,col)
                            error['error']='Invalid Date Format,Format should be 01-Jan-2011'
                            allerror.append(error)
                    elif col==2:
                        try:
                            if(df.loc[row][col] >0 and (isinstance(df.loc[row][col],int) or isinstance(df.loc[row][col],float))): #validating the data for quantity
                                #print(df.loc[row][col])
                                count += 1
                                order_detail.append(df.loc[row][col])
                            else:
                                #error[xl_rowcol_to_cell(row+1,col)]='value should be non zero, non negative'
                                error = {}
                                error['address']=xl_rowcol_to_cell(row+1,col)
                                error['error']='value should be non zero, non negative'
                                allerror.append(error)  
                        except:
                            #error[xl_rowcol_to_cell(row+1,col)]='value should be non zero, non negative'
                            error = {}
                            error['address']=xl_rowcol_to_cell(row+1,col)
                            error['error']='value should be non zero, non negative'
                            allerror.append(error) 
                    elif col == 3:
                        try:
                            if(df.loc[row][col] >0 and (isinstance(df.loc[row][col],int) or isinstance(df.loc[row][col],float))):  #validating the data for sales
                                #print(df.loc[row][col])
                                count += 1
                                order_detail.append(df.loc[row][col])
                            else:
                                #error[xl_rowcol_to_cell(row+1,col)]='value should be greater than zero'
                                error = {}
                                error['address']=xl_rowcol_to_cell(row+1,col)
                                error['error']='value should be greater than zero'
                                allerror.append(error) 
                        except:
                            #error[xl_rowcol_to_cell(row+1,col)]='value should be greater than zero'
                            error = {}
                            error['address']=xl_rowcol_to_cell(row+1,col)
                            error['error']='value should be greater than zero'
                            allerror.append(error)
                    elif col==4:
                        try:
                            if df.loc[row][col].strip() in ["Regular Air","Delivery Truck","Express Air"]:  #validating the data for ship mode
                                count +=1
                                order_detail.append(df.loc[row][col])
                                #print(df.loc[row][col])
                            else:
                                #error[xl_rowcol_to_cell(row+1,col)]='value should contains only the following value (Regular Air | Delivery Truck | Express Air)'
                                error = {}
                                error['address']=xl_rowcol_to_cell(row+1,col)
                                error['error']='value should contains only the following value (Regular Air | Delivery Truck | Express Air)'
                                allerror.append(error)
                        except:
                            #error[xl_rowcol_to_cell(row+1,col)]='value should contains only the following value (Regular Air | Delivery Truck | Express Air)'
                            error = {}
                            error['address']=xl_rowcol_to_cell(row+1,col)
                            error['error']='value should contains only the following value (Regular Air | Delivery Truck | Express Air)'
                            allerror.append(error)
                    
                    elif col==5:
                        try:
                            if((not np.isnan(df.loc[row][col])) and df.loc[row][col] != 0 and (isinstance(df.loc[row][col],int) or isinstance(df.loc[row][col],float))):  #validating the data for profit
                                #print(df.loc[row][col])
                                count += 1
                                order_detail.append(df.loc[row][col])
                            else:
                                #error[xl_rowcol_to_cell(row+1,col)]='value should be non zero and must be numerical'
                                error = {}
                                error['address']=xl_rowcol_to_cell(row+1,col)
                                error['error']='value should be non zero and must be numerical'
                                allerror.append(error)
                        except:
                            error = {}
                            error[xl_rowcol_to_cell(row+1,col)]='value should be non zero and must be numerical'
                            error['address']=xl_rowcol_to_cell(row+1,col)
                            error['error']='value should be non zero and must be numerical'
                            allerror.append(error)
                    elif col==6:
                        try:
                            if((not np.isnan(df.loc[row][col])) and df.loc[row][col] != 0 and (isinstance(df.loc[row][col],int) or isinstance(df.loc[row][col],float))):  #validating the data for unit price
                                #print(df.loc[row][col])
                                count += 1
                                order_detail.append(df.loc[row][col])
                            else:
                                #error[xl_rowcol_to_cell(row+1,col)]='value should be non zero and must be numerical'
                                error = {}
                                error['address']=xl_rowcol_to_cell(row+1,col)
                                error['error']='value should be non zero and must be numerical'
                                allerror.append(error)
                        except:
                            #error[xl_rowcol_to_cell(row+1,col)]='value should be non zero and must be numerical'
                            error = {}
                            error['address']=xl_rowcol_to_cell(row+1,col)
                            error['error']='value should be non zero and must be numerical'
                            allerror.append(error)
                    elif col==7:
                        order_detail.append(df.loc[row][col]) #Undconditional data for customer name
                    elif col==8:
                        order_detail.append(df.loc[row][col]) #Undconditional data for customer segment
                    elif col==9:
                        order_detail.append(df.loc[row][col]) #Undconditional data for product category
                            
                    
                if count == 7:  #data in each column of a row is validated and ready to be inserted in database
                    #Create list of objects that need to be inserted in database using bulk_create
                    bulk_create_data.append(Order(order_id=order_detail[0],
                                                order_date=order_detail[1],
                                                order_date_new=order_detail[2],
                                                order_qty=order_detail[3],
                                                order_sales=order_detail[4],
                                                order_ship_mode=order_detail[5],
                                                order_profit=order_detail[6],
                                                order_unit_price=order_detail[7],
                                                order_customer_name=order_detail[8],
                                                order_customer_segment=order_detail[9],
                                                order_product_category=order_detail[10]))
                #else:    #data in each column of a row is not validated and ready to be inserted in database
                    #print(count)
                #    allerror.append(error)   #creating dictionary that wil be returned as json data to user stating errors
                    #print(allerror)
            try:
                Order.objects.bulk_create(bulk_create_data) #saves times and hits to database for inserting bulk data at once in database
            except:
                pass
            return JsonResponse(allerror,safe=False)
        else:
            return JsonResponse({'error':'Upload file is not Excelsheet'},safe=False) 
    else:
        return JsonResponse({},safe=False)
        
                           

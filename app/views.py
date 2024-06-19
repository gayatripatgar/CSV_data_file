from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
import csv
# Create your views here.
def insert_bank(self):
     with open('C:\\Users\\Admin\\Django\\gayatri\\Scripts\\CSV_data_file\\app\\bank.csv','r') as FO:
          IOD=csv.reader(FO)
          for i in IOD:
               bn=i[0].strip()
               BO=Bank(bank_name=bn)
               BO.save()
          
     return HttpResponse('<center><h1>data inserted successfully.</h1></center>')

def insert_branch(self):
     with open('C:\\Users\\Admin\\Django\\gayatri\\Scripts\\CSV_data_file\\app\\branch1.csv','r') as FO:
          IOD=csv.reader(FO)
          for i in IOD:
               bn=i[0]
               BO=Bank.objects.filter(bank_name=bn)
               if BO:
                    ifs=i[1]
                    br=i[2]
                    ad=i[3]
                    co=i[4]
                    ci=i[5]
                    d=i[6]
                    s=i[7]

                    BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=ci,district=d,state=s)
                    BRO.save()
     return HttpResponse('<center><h1>Branch data successfully inserted.')
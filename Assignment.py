#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

from tika import parser
import re



class Main:
    def __init__(self, filepath):
        self.mainDict = {}
        self.path = filepath
        self.text = self.readFile()
        self.basicInfo()
        self.Row1()
        self.Row3()
        self.Row2()


    def basicInfo(self):
        self.mainDict['Division_Name'] = re.findall('^Division Name(.*?)^Consumer Name',self.text,re.DOTALL|re.MULTILINE)[0].replace('\n', '').strip()
        self.mainDict['Consumer_Name'] = re.findall('^Consumer Name(.*?)^Address',self.text,re.DOTALL|re.MULTILINE)[0].replace('\n', '').strip()

        self.mainDict['Adress'] = re.findall('^Address(.*?)^Book',self.text,re.DOTALL|re.MULTILINE)[0].replace('\n', '').strip().split(',')[0]
        self.mainDict['phoneNumber'] = re.findall('^Address(.*?)^Book',self.text,re.DOTALL|re.MULTILINE)[0].replace('\n', '').strip().split(',')[1].split()[2]

    def readFile(self):
        parsedPDF = parser.from_file(self.path)
        text = parsedPDF["content"]
        return text

        

    def Row1(self):
        string = re.findall('^From To Months(.*?)^Meter No.', pdf, re.DOTALL|re.MULTILINE)[0].replace('\n', '')
        data = re.findall(r'[0-9]{4}/[0-9]{1} |[0-9]{4} / [0-9]{1} ', string)
        string = string.replace(data[0], '')
        a,b,c,d,string = string.split(' ', 4)
        dates = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})', string)
        dates = [x[0] for x in dates]
        self.mainDict.update({'SC_No':a, 'Account_No':b, 'Supply_Realease_Date': c, 'Supply_Type': d, 'BookNo_BillGroup': data[0], 'From': dates[0], 'To':dates[1]})
        for val in dates:
            string = string.replace(val, '')
        data = string.split()
        self.mainDict.update({ 'months': data[-1], 'load': data[0]+' '+data[1], 'Bill_No': data[2]})
    def Row3(self):
        inp = re.findall('^Bill Base(.*?)^Bill Details',pdf,re.DOTALL|re.MULTILINE)[0].replace('\n', '').strip()
        inp = inp.split()[12:]

        self.mainDict.update({'billBase': inp[0][4:], 'alloted_Units': inp[1],
        'adjustment_Units': inp[2],'totalUnits': inp[3], 'totalDemand': inp[4],
        'Inoperative_Amount': inp[-3] , 'security_Amout': inp[-2],
        'Disconnection_Date': inp[-1] })
    def Row2(self):
        string = re.findall('^Demand Status Bill Date Due Date(.*?)^Bill Base',pdf,re.DOTALL|re.MULTILINE)[0].replace('\n', '')
        data = re.findall(r' [A-Za-z]+ ', string)[0]
        string = string.replace(data, '')
        dates = re.findall('(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})', string)
        dates = [x[0] for x in dates]
        for date in dates:
            string = string.replace(date, '')

        rational = re.findall(r'[0-9]+[.][0-9]+ / [0-9]+[.][0-9]+|[0-9]+[.][0-9]+ / [0-9]+|[0-9]+ / [0-9]+[.][0-9]+ | [0-9]+ / [0-9]+', string)
        for val in rational:
            string = string.replace(val, '')
        meterNo, mulFactor, pf, demand = string.split()
        self.mainDict.update({'status': data, 'billDate': dates[0], 'dueDate': dates[1] ,'lastReading': rational[0], 'currentReading': rational[1], 'unitsConsumed': rational[2],'meterNo':meterNo, 'MulFactor': mulFactor, 'powerfactor': pf, 'demand': demand})

obj = Main("/home/rashid139/Desktop/test3.pdf")
df = pd.DataFrame(list(obj.mainDict.items()), columns=['Key', 'Value'])


# In[1]:


get_ipython().system('pip show tika')


# In[ ]:





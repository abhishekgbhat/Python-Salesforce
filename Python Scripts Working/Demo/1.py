from simple_salesforce import Salesforce
sf = Salesforce(username='support@ctmssite.com.abhishek', password='Roopgiri91', security_token='GnMyprasH9Im42ZQo9cJBWXO')
print('Connection Succesful')
protocolRecords = sf.query("SELECT Id,Name,Title__c,Short_Title__c,Protocol_Status__c FROM Protocol__c")
protocolRecords = protocolRecords['records']
print(len(protocolRecords))
for record in protocolRecords:
    idList = record['Id']
    print ""+record['Id']+"  "+record['Name']
print"\n\n\n"
financialRecords = sf.query("SELECT Id,Name,Protocol__c FROM Financials__c ")
financialRecords = financialRecords['records']
print(len(financialRecords))
for record in financialRecords:
    idList1 = record['Id']
    print ""+record['Id']+"  "+record['Name']+"         "+str(record['Protocol__c'])
    
    


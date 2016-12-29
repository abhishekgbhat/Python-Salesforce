from simple_salesforce import Salesforce
sf = Salesforce(username='support@ctmssite.com.abhishek', password='Roopgiri91', security_token='GnMyprasH9Im42ZQo9cJBWXO')
print('Connection Succesful')
records = sf.query("SELECT Id,Name,Title__c,Short_Title__c,Protocol_Status__c FROM Protocol__c")
records = records['records']
print(len(records))
for record in records:
    idList = record['Id']
    print idList
    print ""+record['Id']+"  "+record['Name']+"  "+str(record['Title__c'])+" "+str(record['Protocol_Status__c'])

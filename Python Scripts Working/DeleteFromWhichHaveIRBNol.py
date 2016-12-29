from simple_salesforce import Salesforce
sf = Salesforce(username='support@ctmssite.com.abhishek', password='Roopgiri91', security_token='GnMyprasH9Im42ZQo9cJBWXO')
print('Connection Succesful')
records = sf.query("Select id,IRB_No__c,Name from Protocol__c where IRB_No__c ='1' ")
records = records['records']
print '\nPrinting Financials and Names\n\n'
for record in records:
        FinIdList=record['Id']
        print "" + record['Id']+" "+record['Name']
        sf.Protocol__c.delete(record['Id'])
print('Deletion Succesful')

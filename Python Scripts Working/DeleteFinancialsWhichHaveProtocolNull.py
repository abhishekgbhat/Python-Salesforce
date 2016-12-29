from simple_salesforce import Salesforce
sf = Salesforce(username='support@ctmssite.com.abhishek', password='Roopgiri91', security_token='GnMyprasH9Im42ZQo9cJBWXO')
print('Connection Succesful')
records = sf.query("SELECT Id,Name FROM Financials__c where Protocol__c=null ")
records = records['records']
print '\nPrinting Financials and Names\n\n'
for record in records:
        FinIdList=record['Id']
        print "" + record['Id']+" "+record['Name']
        sf.Financials__c.delete(record['Id'])
print('Deletion Succesful')

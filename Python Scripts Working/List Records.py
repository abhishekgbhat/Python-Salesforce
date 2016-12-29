from simple_salesforce import Salesforce
sf = Salesforce(username='support@ctmssite.com.abhishek', password='Roopgiri91', security_token='GnMyprasH9Im42ZQo9cJBWXO')
print('Connection Succesful')
var='5000VisitAssociation1';
records = sf.query("SELECT id,Name from Protocol__c where Name='%s'"%var)
records = records['records']
print '\nPrinting Protocol Id and Names\n\n'
for record in records:
        FinIdList=record['Id']
        print "" + record['Id']+" "+record['Name']

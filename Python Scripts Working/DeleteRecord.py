from simple_salesforce import Salesforce
import requests
var  = False 
#Credentials to connect to salesforce using the simple_salesforce library/api
sf = Salesforce(username='support@ctmssite.com.abhishek', password='Roopgiri91', security_token='GnMyprasH9Im42ZQo9cJBWXO')
print('Connection Succesful')
protocolToDelete='a1w41000000S7s4AAC';
print "All the protocols present in the salesforce (Allegro)"

protocolRecords = sf.query("SELECT Id,Name FROM Protocol__c ")
protocolRecords = protocolRecords['records']
print(len(protocolRecords))
idList=[];
for record in protocolRecords:
    idList.append(record['Id'])
    print ""+record['Id']+"  "+record['Name']
    var = protocolToDelete == str(record['Id'])
                     

print "\n\n"
                                                 
print "Deleting Financials Records for the Respective Protocol"
                           
financialRecords = sf.query("SELECT Id,Name,Protocol__c FROM Financials__c where protocol__c = '%s'"%protocolToDelete)
financialRecords = financialRecords['records']
idListFinancials=[];
for record in financialRecords:
    idListFinancials.append(record['Id'])
    print ""+record['Id']+"  "+record['Name']+"         "+str(record['Protocol__c'])
    sf.Financials__c.delete(record['Id'])
print (len(financialRecords))," Records Deleted from Financials"

print "Deleting Budgets Records for the Respective Protocol"

budgetRecords = sf.query("SELECT Id,Name,Protocol__c FROM Budget__c where protocol__c = '%s'"%protocolToDelete)
budgetRecords = budgetRecords['records']
idListBudget=[];
for record in budgetRecords:
    idListBudget.append(record['Id'])
    print ""+record['Id']+" "+record['Name']+" "+str(record['Protocol__c'])
    sf.Budget__c.delete(record['Id'])
print (len(budgetRecords))," Records Deleted from Budgets"

print "Deleting Subject Visit Procedure Records for the Respective Protocol"

SVPRecords = sf.query("SELECT Id,Protocol_Procedure__r.Protocol__c FROM Subject_Visit_Procedure__c where Protocol_Procedure__r.Protocol__c = '%s'"%protocolToDelete)
SVPRecords = SVPRecords['records']
idListSVP=[];
for record in SVPRecords:
    idListSVP.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Subject_Visit_Procedure__c.delete(record['Id'])
print (len(SVPRecords))," Records Deleted from Subject Visit Procedure"

print "Deleting Subject Visit Records for the Respective Protocol"

SVRecords = sf.query("SELECT Id FROM Subject_Visit__c where Subject_Segment__r.Protocol_Subject__r.Protocol__c = '%s'"%protocolToDelete)
SVRecords = SVRecords['records']
idListSV=[];
for record in SVRecords:
    idListSV.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Subject_Visit__c.delete(record['Id'])
print (len(SVRecords))," Records Deleted from Subject Visit "

print "Deleting Subject Segment  Records for the Respective Protocol"

SSRecords = sf.query("SELECT Id FROM Subject_Segment__c where  Protocol_Subject__r.Protocol__c = '%s'"%protocolToDelete)
SSRecords = SSRecords['records']
idListSS=[];
for record in SSRecords:
    idListSS.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Subject_Segment__c.delete(record['Id'])
print (len(SSRecords))," Records Deleted from Subject Segment "

print "Deleting Visit Procedure Records for the Respective Protocol"

VPRecords = sf.query("SELECT Id FROM Visit_Procedure__c where Protocol_Procedure__r.Protocol__c = '%s'"%protocolToDelete)
VPRecords = VPRecords['records']
idListVPR=[];
for record in VPRecords:
    idListVPR.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Visit_Procedure__c.delete(record['Id'])
print (len(VPRecords))," Records Deleted from Visit Procedure "        

print "Deleting Schedule Procedure Records for the Respective Protocol"

SPRecords = sf.query("SELECT Id FROM Schedule_Procedure__c where Protocol_Procedure__r.Protocol__c = '%s'"%protocolToDelete)
SPRecords = SPRecords['records']
idListSP=[];
for record in SPRecords:
    idListSP.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Schedule_Procedure__c.delete(record['Id'])
print (len(SPRecords))," Records Deleted from Schedule Procedure "

print "Deleting Schedule Visit Procedure Records for the Respective Protocol"

SVPPRecords = sf.query("SELECT Id FROM Schedule_Visit_Procedure__c where Visit__r.Segment__r.Protocol__c = '%s'"%protocolToDelete)
SVPPRecords = SVPPRecords['records']
idListSVPP=[];
for record in SVPPRecords:
    idListSVPP.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Schedule_Visit_Procedure__c.delete(record['Id'])
print (len(SVPPRecords))," Records Deleted from Schedule Procedure "

print "Deleting Protocol Procedure Records for the Respective Protocol"

PPRecords = sf.query("SELECT Id FROM Protocol_Procedure__c where Visit__r.Segment__r.Protocol__c = '%s'"%protocolToDelete)
PPRecords = PPRecords['records']
idListPP=[];
for record in PPRecords:
    idListPP.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Schedule_Visit_Procedure__c.delete(record['Id'])
print (len(PPRecords))," Records Deleted from Protocol Procedure "

print "Deleting Visit Records for the Respective Protocol"

VRecords = sf.query("SELECT Id FROM Visit__c where Segment__r.Protocol__c = '%s'"%protocolToDelete)
VRecords = VRecords['records']
idListV=[];
for record in VRecords:
    idListV.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Schedule_Visit_Procedure__c.delete(record['Id'])
print (len(VRecords))," Records Deleted from Visit"

print "Deleting Schedule Records for the Respective Protocol"

SRecords = sf.query("SELECT Id FROM Schedule__c where Calendar_Cycle__r.Segment__r.Protocol__c = '%s'"%protocolToDelete)
SRecords = SRecords['records']
idListSR=[];
for record in SRecords:
    idListSR.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Schedule__c.delete(record['Id'])
print (len(SRecords))," Records Deleted from Schedule"

print "Deleting Calendar Records for the Respective Protocol"

CCRecords = sf.query("SELECT Id FROM Calendar_Cycle__c where Segment__r.Protocol__c = '%s'"%protocolToDelete)
CCRecords = CCRecords['records']
idListCC=[];
for record in CCRecords:
    idListCC.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Calendar_Cycle__c.delete(record['Id'])
print (len(CCRecords))," Records Deleted from Calendar"

print "Deleting Segment for the Respective Protocol"

SegRecords = sf.query("SELECT Id FROM Segment__c where Segment__r.Protocol__c = '%s'"%protocolToDelete)
SegRecords = SegRecords['records']
idListSeg=[];
for record in SegRecords:
    idListSeg.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Segment__c.delete(record['Id'])
print (len(SegRecords))," Records Deleted from Segment"

print "Deleting Protocol Subject for the Respective Protocol"

PSRecords = sf.query("SELECT Id FROM Protocol_Subject__c where Protocol__c = '%s'"%protocolToDelete)
PSRecords = PSRecords['records']
idListSeg=[];
for record in PSRecords:
    idListSeg.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Protocol_Subject__c.delete(record['Id'])
print (len(PSRecords))," Records Deleted from Protocol Subject"

print "Deleting Adhoc Payments for the Respective Protocol"

APRecords = sf.query("SELECT Id FROM Adhoc_Payment__c where Protocol__c = '%s'"%protocolToDelete)
APRecords = APRecords['records']
idListAP=[];
for record in APRecords:
    idListAp.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Adhoc_Payment__c.Delete(record['Id'])
print (len(APRecords))," Records Deleted from Protocol Subject"

print "Deleting Email Setup for the Respective Protocol"

ESRecords = sf.query("SELECT Id FROM Email_Setup__c where Is_Organization_Setup__c != true and Protocol__c = '%s'"%protocolToDelete)
ESRecords = ESRecords['records']
idListES=[];
for record in ESRecords:
    idListES.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Email_Setup__c.delete(record['Id'])
print (len(ESRecords))," Records Deleted from Email Setup"

print "Deleting Web Protocol for the Respective Protocol"

WPRecords = sf.query("SELECT Id FROM Web_Protocol__c where Protocol__c = '%s'"%protocolToDelete)
WPRecords = WPRecords['records']
idListWP=[];
for record in WPRecords:
    idListWP.append(record['Id'])
    print ""+record['Id']+"  "+str(record['Protocol__c'])
    sf.Web_Protocol__c.delete(record['Id'])
print (len(WPRecords))," Records Deleted from Web Protocol"

        
        
        #sf.Web_Protocol__c.delete("select Id from Web_Protocol__c where Protocol__c = '%s'"%(record['Id']))
if(var == True):
        sf.Protocol__c.delete(protocolToDelete);
        print "Deleted All the Things Realted with Protocol ID = ",protocolToDelete
print('Succesful')

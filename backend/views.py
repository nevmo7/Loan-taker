from django.shortcuts import render
import json

from django.template.response import TemplateResponse

def index(request):
    return render(request, 'frontend/index.html')

def getBalanceSheet(request):

    companyName = request.GET.get('companyName','')
    loanAmt = request.GET.get('loanAmt','')

    sheetA = getBalanceSheetA(loanAmt) 

    sheetB =  getBalanceSheetB(loanAmt)

    sheetC = getBalanceSheetC(loanAmt)

    

    #renders getBalanceSheet.html according to company name provided
    if(companyName == 'A'):
        return render(request, 'frontend/getBalanceSheet.html', sheetA)

    elif(companyName == 'B'): 
        return render(request, 'frontend/getBalanceSheet.html', sheetB)

    elif(companyName == 'C'): 
        return render(request, 'frontend/getBalanceSheet.html', sheetC)


def getLoanApproval(request):
    companyName = request.GET.get('companyName', '')
    loanAmt = int(request.GET.get('loanAmt', ''))

    company = None

    #get balance sheet according to the company name provided
    if(companyName == 'A'):
        company = getBalanceSheetA(loanAmt)
    elif(companyName == 'B'): 
        company = getBalanceSheetB(loanAmt)
    elif(companyName == 'C'): 
        company = getBalanceSheetC(loanAmt)


    loanApproved = checkLoan(company, loanAmt)

    return render(request, 'frontend/submitApp.html', loanApproved)

#function to check loan approval amount
#takes company balance sheet and loan amount as input
#returns amount apoproved for loan
def checkLoan(company, loanAmt):
    preAssessment = 20

    totalAssetValue = 0

    #if the balance sheet does not have 12 or more months of data then the pre assessment will be 20%
    if(len(company['balanceSheet']) >= 12):
        for e in company['balanceSheet']:
            totalAssetValue += e['assetsValue']

        avgAssetsValue = totalAssetValue/12 #calculate average asset value

        #if average asset value is greater than loan amount pre assessment will be 
        if avgAssetsValue > loanAmt:
            preAssessment = 100

        #if average asset value is less than loan amount then check if the company has made consistent profit
        elif avgAssetsValue < loanAmt:
            profit = True

            #going through profit or loss for each month
            for e in company['balanceSheet']:
                #if there is loss then pre assessment will be the default value = 20
                if e['profitOrLoss'] <= 0:
                    profit = False
                    break
            
            #if there is profit then pre assessment will be 60%
            if profit:
                preAssessment = 60

    #finding the loan amount approved from the loan
    approvedAmt = (preAssessment/100) * loanAmt

    loanApproved = {
        "approvedAmt": approvedAmt
    }

    return loanApproved

# balance sheet to check 100% loan approval on $1000000 loan
def getBalanceSheetA(loanAmt):
    return {"companyName": "A",
    "loanAmt": loanAmt,
    "balanceSheet": [
        {
            "year": 2020,
            "month": 12,
            "profitOrLoss": 250000,
            "assetsValue": 1000070
        },
        {
            "year": 2020,
            "month": 11,
            "profitOrLoss": 1150,
            "assetsValue": 1040000
        },
        {
            "year": 2020,
            "month": 10,
            "profitOrLoss": 2500,
            "assetsValue": 1002000
        },
        {
            "year": 2020,
            "month": 9,
            "profitOrLoss": -187000,
            "assetsValue": 1005000
        },
        {
            "year": 2020,
            "month": 8,
            "profitOrLoss": 250000,
            "assetsValue": 1040000
        },
        {
            "year": 2020,
            "month": 7,
            "profitOrLoss": 1150,
            "assetsValue": 1200000
        },
        {
            "year": 2020,
            "month": 6,
            "profitOrLoss": 2500,
            "assetsValue": 1100000
        },
        {
            "year": 2020,
            "month": 5,
            "profitOrLoss": -187000,
            "assetsValue": 1004000
        },
        {
            "year": 2020,
            "month": 4,
            "profitOrLoss": 250000,
            "assetsValue": 1006000
        },
        {
            "year": 2020,
            "month": 3,
            "profitOrLoss": 1150,
            "assetsValue": 1004000
        },
        {
            "year": 2020,
            "month": 2,
            "profitOrLoss": 2500,
            "assetsValue": 1005000
        },
        {
            "year": 2020,
            "month": 1,
            "profitOrLoss": -187000,
            "assetsValue": 1070000
        },
        
    ]}

# balance sheet to check 60% loan approval on $1000000 loan
def getBalanceSheetB(loanAmt):
    return {"companyName": "B",
    "loanAmt": loanAmt,
    "balanceSheet": [
        {
            "year": 2020,
            "month": 12,
            "profitOrLoss": 250000,
            "assetsValue": 1234
        },
        {
            "year": 2020,
            "month": 11,
            "profitOrLoss": 1150,
            "assetsValue": 5789
        },
        {
            "year": 2020,
            "month": 10,
            "profitOrLoss": 2500,
            "assetsValue": 22345
        },
        {
            "year": 2020,
            "month": 9,
            "profitOrLoss": 700,
            "assetsValue": 223452
        },
        {
            "year": 2020,
            "month": 8,
            "profitOrLoss": 250000,
            "assetsValue": 1234
        },
        {
            "year": 2020,
            "month": 7,
            "profitOrLoss": 1150,
            "assetsValue": 5789
        },
        {
            "year": 2020,
            "month": 6,
            "profitOrLoss": 2500,
            "assetsValue": 22345
        },
        {
            "year": 2020,
            "month": 5,
            "profitOrLoss": 700,
            "assetsValue": 223452
        },
        {
            "year": 2020,
            "month": 4,
            "profitOrLoss": 250000,
            "assetsValue": 1234
        },
        {
            "year": 2020,
            "month": 3,
            "profitOrLoss": 1150,
            "assetsValue": 5789
        },
        {
            "year": 2020,
            "month": 2,
            "profitOrLoss": 2500,
            "assetsValue": 22345
        },
        {
            "year": 2020,
            "month": 1,
            "profitOrLoss": 700,
            "assetsValue": 223452
        },
        
    ]}

# balance sheet to check 20% loan approval on $1000000 loan
def getBalanceSheetC(loanAmt):
    return {"companyName": "C",
    "loanAmt": loanAmt,
    "balanceSheet": [
        {
            "year": 2020,
            "month": 12,
            "profitOrLoss": 250000,
            "assetsValue": 1234
        },
        {
            "year": 2020,
            "month": 11,
            "profitOrLoss": 1150,
            "assetsValue": 5789
        },
        {
            "year": 2020,
            "month": 10,
            "profitOrLoss": 2500,
            "assetsValue": 22345
        },
        {
            "year": 2020,
            "month": 9,
            "profitOrLoss": -187000,
            "assetsValue": 223452
        },
        {
            "year": 2020,
            "month": 8,
            "profitOrLoss": 250000,
            "assetsValue": 1234
        },
        {
            "year": 2020,
            "month": 7,
            "profitOrLoss": 1150,
            "assetsValue": 5789
        },
        {
            "year": 2020,
            "month": 6,
            "profitOrLoss": 2500,
            "assetsValue": 22345
        },
    ]}
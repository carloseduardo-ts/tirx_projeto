import xlrd
import requests

base_url = "http://demo.trixlog.com/trix/"

data = '''
{
    "id": {id},
    "name": {name},
    "type": {type},
    "registration": {registration},
    "vehicles": [],
    "driverTeam": {
        "id": {driverTeam_id}
    },
    "rg": {rg},
    "cpf": {cpf},
    "status": {status},
    "hiringType": {hiring_type},
    "riskDriver": {risk_driver},
    "integrationId": {integration_id},
    "licenseCategory": {l_category},
    "licenseExpedition": {l_expedition},
    "licenseExpiration": {l_expiration},
    "licenseRegister": {l_register},
    "registrationCode": {registration_code}
}
'''

wb = xlrd.open_workbook('teste.xlsx')
ws = wb.sheet_by_index(0)









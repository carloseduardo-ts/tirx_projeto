import xlrd
import requests
from requests.auth import HTTPBasicAuth

def formatarData(t):
    if len(str(t)) != 0:
        r = xlrd.xldate_as_tuple(t, wb.datemode)
        return str(r[0])+"-"+str(r[1])+"-"+str(r[2])+"T03:00:00Z"
    else:
        return ""

base_url = "http://demo.trixlog.com/trix/"
auth = ('carloseduardo@teste', 'carloseduardo@teste')

### teste de requisição
# r1 = requests.get(base_url, auth=auth)
# print(r1)

data = {
    "name": "",
    "type": "",
    "registration": "",
    "vehicles": [],
    "driverTeam": {
        "id": ""
    },
    "rg": "",
    "cpf": "",
    "status": "",
    "hiringType": "",
    "riskDriver": "",
    "integrationId": "",
    "licenseCategory": "",
    "licenseExpedition": "",
    "licenseExpiration": "",
    "licenseRegister": "",
    "registrationCode": ""
}

wb = xlrd.open_workbook('teste.xlsx')
ws = wb.sheet_by_index(0)

for i in range(1, ws.nrows):
    data['name'] = ws.cell_value(i, 2)
    data['type'] = ws.cell_value(i, 6)
    data['registration'] = ws.cell_value(i, 3)
    data['driverTeam']['id'] = ws.cell_value(i, 5)
    data['rg'] = str(int(ws.cell_value(i, 7)))
    data['cpf'] = str(int(ws.cell_value(i, 8)))
    data['status'] = ws.cell_value(i, 13)
    data['hiringType'] = ws.cell_value(i, 15)
    data['riskDriver'] = ws.cell_value(i, 16)
    data['integrationId'] = ws.cell_value(i, 4)
    data['licenseCategory'] = ws.cell_value(i, 10)
    data['licenseExpedition'] = formatarData(ws.cell_value(i, 11))
    data['licenseExpiration'] = formatarData(ws.cell_value(i, 12))
    data['licenseRegister'] = ws.cell_value(i, 9)
    data['registrationCode'] = ws.cell_value(i, 14)
    if data['licenseExpedition'] == '':
        data.pop('licenseExpedition')
    if data['licenseExpiration'] == '':
        data.pop('licenseExpiration')

    print("\n\n",data)
    
    x = requests.post(base_url+'driver', headers={'Content-Type': 'application/json'}, json=data, auth=auth)
    print(x.content)

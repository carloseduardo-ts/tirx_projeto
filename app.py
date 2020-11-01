# from functions import *

# def main():
#     condutoresCadastrados = []
#     #estrutura que será mandada para API após preenchimento
#     data = {
#         "name": "",
#         "type": "",
#         "registration": "",
#         "vehicles": [],
#         "driverTeam": {
#             "id": ""
#         },
#         "rg": "",
#         "cpf": "",
#         "status": "",
#         "hiringType": "",
#         "riskDriver": "",
#         "integrationId": "",
#         "licenseCategory": "",
#         "licenseExpedition": "",
#         "licenseExpiration": "",
#         "licenseRegister": "",
#         "registrationCode": ""
#     }

#     #abrindo planilha do excel
#     wb = xlrd.open_workbook('teste.xlsx')
#     ws = wb.sheet_by_index(0)

#     #percorrendo os dados da planilha
#     for i in range(1, ws.nrows):
#         d_name = ws.cell_value(i, 2)
#         d_type = ws.cell_value(i, 6)
#         d_registration = ws.cell_value(i, 3)
#         d_driverTeam = ws.cell_value(i, 5)
#         d_rg = ws.cell_value(i, 7)
#         d_cpf = ws.cell_value(i, 8)
#         d_status = ws.cell_value(i, 13)
#         d_hiringType = ws.cell_value(i, 15)
#         d_riskDriver = ws.cell_value(i, 16)
#         d_integrationId = ws.cell_value(i, 4)
#         d_licenseCategory = ws.cell_value(i, 10)
#         d_licenseExpedition = ws.cell_value(i, 11)
#         d_licenseExpiration = ws.cell_value(i, 12)
#         d_licenseRegister = ws.cell_value(i, 9)
#         d_registrationCode = ws.cell_value(i, 14)

#         #setando os valores em data
#         data = setDados(data, wb, d_name, d_type, d_registration, d_driverTeam, d_rg, d_cpf, d_status, d_hiringType, d_riskDriver, d_integrationId, d_licenseCategory, d_licenseExpedition, d_licenseExpiration, d_licenseRegister, d_registrationCode)
#         print("\n\n",data)

#         # cadastrando condutor
#         c = cadastrarDriver(data)
#         if c.status_code == 200:
#             condutoresCadastrados.append(str(json.loads(c.content)['id'])+"\n")
#         print(condutoresCadastrados, c.content)

#         # inserindos ids dos condutores em um arquivo
#         f = open('condutores.txt', 'w')
#         f.writelines(condutoresCadastrados)
#         f.close()

# if __name__ == '__main__':
#     main()

import driver
import pandas as pd 

xlsx = pd.ExcelFile('teste.xlsx')
ws = pd.read_excel(xlsx, 'teste')

condutores = []

for i in range(ws.shape[0]):
  d = driver.Driver(
    ws.organization_id[i],
    ws.user_id[i],
    ws.name[i],
    ws.registration[i],
    ws.integrationid[i],
    ws.driverteam_id[i],
    ws.type[i],
    ws.rg[i],
    ws.cpf[i],
    ws.licenseregister[i],
    ws.licensecategory[i],
    ws.licenseexpedition[i],
    ws.licenseexpiration[i],
    ws.status[i],
    ws.registrationcode[i],
    ws.hiringtype[i],
    ws.riskdriver[i]
  )
  condutores.append(d)

  # for i in condutores:
  #   x = i.cadastrar()
  #   print(x)
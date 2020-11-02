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

for i in condutores:
  x = i.cadastrar()
print(x)

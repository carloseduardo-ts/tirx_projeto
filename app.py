from functions import *

def main():
    #estrutura que será mandada para API após preenchimento
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

    #abrindo planilha do excel
    wb = xlrd.open_workbook('teste.xlsx')
    ws = wb.sheet_by_index(0)

    #percorrendo os dados da planilha
    for i in range(1, ws.nrows):
        d_name = ws.cell_value(i, 2)
        d_type = ws.cell_value(i, 6)
        d_registration = ws.cell_value(i, 3)
        d_driverTeam = ws.cell_value(i, 5)
        d_rg = ws.cell_value(i, 7)
        d_cpf = ws.cell_value(i, 8)
        d_status = ws.cell_value(i, 13)
        d_hiringType = ws.cell_value(i, 15)
        d_riskDriver = ws.cell_value(i, 16)
        d_integrationId = ws.cell_value(i, 4)
        d_licenseCategory = ws.cell_value(i, 10)
        d_licenseExpedition = ws.cell_value(i, 11)
        d_licenseExpiration = ws.cell_value(i, 12)
        d_licenseRegister = ws.cell_value(i, 9)
        d_registrationCode = ws.cell_value(i, 14)

        #setando os valores em data
        data = setDados(data, wb, d_name, d_type, d_registration, d_driverTeam, d_rg, d_cpf, d_status, d_hiringType, d_riskDriver, d_integrationId, d_licenseCategory, d_licenseExpedition, d_licenseExpiration, d_licenseRegister, d_registrationCode)
        # print("\n\n",data)

        # cadastrando condutor
        c = cadastrarDriver(data)
        print(c.content)    
if __name__ == '__main__':
    main()
import pandas as pd

class Driver:
  def __init__(self, organization_id, user_id, name, registration, integrationid, driverteam_id, type_, rg, cpf, licenseregister, licensecategory, licenseexpedition, licenseexpiration, status, registrationcode, hiringtype, riskdriver):
    self._organization_id = organization_id
    self._user_id = user_id
    self._name = name
    self._registration = registration 
    self._integrationid = integrationid
    self._driverteam_id = driverteam_id
    self._type = type_
    self._rg = rg
    self._cpf = cpf
    self._licenseregister = licenseregister
    self._licensecategory = licensecategory
    self._licenseexpedition = licenseexpedition if not(pd.isnull(licenseexpedition)) else ""
    self._licenseexpiration = licenseexpiration
    self._status = status
    self._registrationcode = registrationcode
    self._hiringtype = hiringtype
    self._riskdriver = riskdriver
    # print(self)

  def dados_dic(self):
    return self.__dict__

  def cadastrar():
    base_url = "http://demo.trixlog.com/trix/"
    auth = ('carloseduardo@teste', 'carloseduardo@teste')

    x = requests.post(base_url+'driver', headers={'Content-Type': 'application/json'}, json=self.dados_dic(), auth=auth)
    return x


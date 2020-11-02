import pandas as pd
import numpy as np
import requests
import json

class Driver:
  def __init__(self, organization_id, user_id, name, registration, integrationid, driverteam_id, type_, rg, cpf, licenseregister, licensecategory, licenseexpedition, licenseexpiration, status, registrationcode, hiringtype, riskdriver):
    self.organization_id = organization_id
    self.user_id = user_id #user_id if not(np.isnan(user_id)) else ""
    self.name = name
    self.registration = registration 
    self.integrationId = integrationid
    self.driverTeam = {'id': driverteam_id}
    self.type = type_
    self.rg = rg
    self.cpf = cpf
    self.licenseRegister = licenseregister #if not(np.isnan(licenseregister)) else ""
    self.licenseCategory = licensecategory #if not(np.isnan(licensecategory)) else ""
    self.licenseExpedition = licenseexpedition #if not(pd.isnull(licenseexpedition)) else ""
    self.licenseExpiration = licenseexpiration #if not(pd.isnull(licenseexpedition)) else "" 
    self.status = status
    self.registrationCode = registrationcode #  if not(pd.isnull(registrationcode)) else ""
    self.hiringType = hiringtype
    self.riskDriver = riskdriver
    # print(self)

  def dados_dic(self):
    aux = list(self.__dict__.keys())
    self.__dict__['driverTeam']['id'] = int(self.__dict__['driverTeam']['id'])
    for i in aux:
      if pd.isna(self.__dict__[i]):
        self.__dict__.pop(i)
      try:   
        if isinstance(self.__dict__[i], np.int64):
          self.__dict__[i] = int(self.__dict__[i])
        if isinstance(self.__dict__[i], np.float64):
          self.__dict__[i] = float(self.__dict__[i]) 
      except:
        pass  
    return self.__dict__


  def cadastrar(self):
    base_url = "http://demo.trixlog.com/trix/" 
    auth = ('carloseduardo@teste', 'carloseduardo@teste')
    data = self.dados_dic()
    x = requests.post(base_url+'driver', headers={'Content-Type': 'application/json'}, json=data, auth=auth)
    return x


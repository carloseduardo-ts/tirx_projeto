import xlrd
import requests

wb = xlrd.open_workbook('teste.xlsx')
ws = wb.sheet_by_index(0)


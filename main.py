from api.client import APIClient 
from services.excel_service import gerar_excel
from services.personagem_service import buscar_personagens

ids = [1, 10, 456, 7, 8, 61]
dados = buscar_personagens(ids)
gerar_excel(dados, "relatorio_api_exemplo.xlsx")
    


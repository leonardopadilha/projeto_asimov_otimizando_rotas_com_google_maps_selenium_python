# Abrindo o site do google maps e adicionando um destino e abre rotas
# cria função adiciona_destino
# cria função abre_rotas

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www.google.com.br/maps')

def adiciona_destino(endereco):
  barra_vazia = driver.find_element(By.ID, 'searchboxinput')
  barra_vazia.clear()
  barra_vazia.send_keys(endereco)
  barra_vazia.send_keys(Keys.RETURN)

def abre_rotas():
  xpath_botao_rotas = '//button[@data-value="Rotas"]'
  wait = WebDriverWait(driver, timeout=3)
  botao_rotas = wait.until(EC.presence_of_element_located((By.XPATH, xpath_botao_rotas)))
  botao_rotas.click()

  xpath_botao_fechar_rotas = '//button[@aria-label="Fechar rotas"]'
  botao_fechar_rotas = wait.until(EC.presence_of_element_located((By.XPATH, xpath_botao_fechar_rotas)))

if __name__ == '__main__':
  endereco = 'Av. José Bonifácio, 245 - Farroupilha, Porto Alegre - RS, 90040-1300' #Redenção
  adiciona_destino(endereco)
  abre_rotas()
  sleep(100)

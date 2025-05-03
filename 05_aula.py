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

def esta_na_aba_de_rotas():
  xpath_botao_fechar_rotas = '//button[@aria-label="Fechar rotas"]'
  botao_fechar_rotas = driver.find_elements(By.XPATH, xpath_botao_fechar_rotas)
  return len(botao_fechar_rotas) > 0

def adiciona_destino(endereco, num_caixa=1):
  if not esta_na_aba_de_rotas():
    barra_vazia = driver.find_element(By.ID, 'searchboxinput')
    barra_vazia.clear()
    barra_vazia.send_keys(endereco)
    barra_vazia.send_keys(Keys.RETURN)
  else:
    xpath_input_localizacao = '//div[contains(@id, "directions-searchbox")]//input'
    caixas = driver.find_elements(By.XPATH, xpath_input_localizacao)
    caixas = [c for c in caixas if c.is_displayed()]

    if len(caixas) >= num_caixa:
      caixa_endereco = caixas[num_caixa - 1]
      caixa_endereco.send_keys(Keys.CONTROL + 'a')
      caixa_endereco.send_keys(endereco)
      caixa_endereco.send_keys(Keys.RETURN)
    else:
      print(f"Não conseguimos adicionar o endereço {len(caixas)} | {num_caixa}")

def abre_rotas():
  xpath_botao_rotas = '//button[@data-value="Rotas"]'
  wait = WebDriverWait(driver, timeout=3)
  botao_rotas = wait.until(EC.presence_of_element_located((By.XPATH, xpath_botao_rotas)))
  botao_rotas.click()

def adiciona_caixa_destino():
  xpath_add_destino = '//span[text()="Adicionar destino"]'
  wait = WebDriverWait(driver, timeout=3)
  wait.until(EC.visibility_of_element_located((By.XPATH, xpath_add_destino)))

  botao_adiciona_destino = driver.find_element(By.XPATH, xpath_add_destino)
  botao_adiciona_destino.click()

def seleciona_tipo_conducao(tipo_conducao="Carro"):
  xpath_tipo_conducao = f'//div[@aria-label="{tipo_conducao}"]'
  wait = WebDriverWait(driver, timeout=3)
  botao_conducao = wait.until(EC.presence_of_element_located((By.XPATH, xpath_tipo_conducao)))
  botao_conducao.click()

def retorna_tempo_total():
  xpath_tempo_rotas = '//div[@id="section-directions-trip-0"]//div[contains(text(), "min")]'
  wait = WebDriverWait(driver, timeout=3)
  elemento_tempo = wait.until(EC.presence_of_element_located((By.XPATH, xpath_tempo_rotas)))
  return int(elemento_tempo.text.replace(' min', ''))


def retorna_distancia_total():
  xpath_tempo_rotas = '//div[@id="section-directions-trip-0"]//div[contains(text(), "km")]'
  wait = WebDriverWait(driver, timeout=3)
  elemento_tempo = wait.until(EC.presence_of_element_located((By.XPATH, xpath_tempo_rotas)))
  return float(elemento_tempo.text.replace(' km', '').replace(',', '.'))

# ==================== FUNÇÕES PRINCIPAIS ====================

def gera_pares_distancia(enderecos):

    distancia_pares = {}
    driver.get("https://www.google.com/maps")
    adiciona_destino(enderecos[0], 1)
    abre_rotas()
    seleciona_tipo_conducao(tipo_conducao="Carro")

    for i, end1 in enumerate(enderecos):
        adiciona_destino(end1, 1)
        sleep(2)
        for j, end2 in enumerate(enderecos):
            if i != j:
                adiciona_destino(end2, 2)
                tempo_par = retorna_tempo_total()
                distancia_pares[f'{i}_{j}'] = tempo_par
                sleep(2)
    
    return distancia_pares



if __name__ == '__main__':
  enderecos = [
            "Av. José Bonifácio, 245 - Farroupilha, Porto Alegre - RS, 90040-130",  #Redenção
            "Av. Borges de Medeiros, 2035 - Menino Deus, Porto Alegre - RS, 90110-150",  #Marinha
            "Av. Guaíba, 544 - Ipanema, Porto Alegre - RS, 91760-740", #Orla Ipanema
            "Av. Padre Cacique, 2000 - Praia de Belas, Porto Alegre - RS, 90810-180", # Iberê
            ]
  
  distancia_pares = gera_pares_distancia(enderecos)
  print(distancia_pares)


  '''
  adiciona_destino(enderecos[0], 1)
  abre_rotas()

  sleep(1)
  adiciona_destino(enderecos[0], 1)

  sleep(1)
  adiciona_destino(enderecos[1], 2)

  #seleciona_tipo_conducao("Carro")
  seleciona_tipo_conducao(tipo_conducao="Motocicleta")

  print(retorna_tempo_total())
  print(retorna_distancia_total())
'''
  sleep(100)

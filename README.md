# Projeto Asimov - Otimização de Rotas com Google Maps e Selenium

Este projeto demonstra como automatizar a busca de rotas no Google Maps usando Selenium e otimizar múltiplos destinos utilizando programação linear para resolver o problema do Caixeiro Viajante (TSP - Traveling Salesman Problem).

## 📋 Sobre o Projeto

O projeto foi desenvolvido como parte de um curso educacional e utiliza automação web com Selenium para:
- Interagir com o Google Maps
- Coletar informações de distância e tempo entre múltiplos endereços
- Otimizar a ordem de visitação dos endereços usando programação linear (PuLP)
- Visualizar a rota otimizada no Google Maps

## 🚀 Funcionalidades

- **Automação do Google Maps**: Navegação e interação automatizada com a interface do Google Maps
- **Coleta de Dados**: Extração de tempos de viagem entre pares de endereços
- **Otimização de Rotas**: Resolução do problema do Caixeiro Viajante usando programação linear
- **Visualização**: Exibição da rota otimizada diretamente no Google Maps

## 📦 Requisitos

- Python 3.7+
- Google Chrome instalado
- Conexão com a internet

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd projeto_asimov_otimizando_rotas_com_google_maps_selenium_python
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

As dependências incluem:
- `selenium`: Automação web
- `webdriver-manager`: Gerenciamento automático do ChromeDriver
- `pulp`: Biblioteca de programação linear para otimização

## 📚 Estrutura do Projeto

O projeto está organizado em aulas progressivas:

- **02_aula.py**: Introdução básica - adicionar destino e abrir rotas
- **03_aula.py**: Adicionar múltiplos destinos
- **04_aula.py**: Pequenas alterações para treinar
- **05_aula.py**: Pequenas alterações para treinar
- **06_aula.py**: Pequenas alterações para treinar
- **07_aula.py**: Implementação completa - geração de pares de distância, otimização e visualização da rota

## 💻 Como Usar

### Exemplo Básico (02_aula.py)

```python
python 02_aula.py
```

Este script demonstra como:
- Abrir o Google Maps
- Adicionar um destino
- Abrir a aba de rotas

### Exemplo Completo (07_aula.py)

```python
python 07_aula.py
```

Este script realiza o processo completo:
1. Coleta tempos de viagem entre todos os pares de endereços
2. Otimiza a ordem de visitação usando programação linear
3. Exibe a rota otimizada no Google Maps

Para personalizar os endereços, edite a lista `enderecos` no arquivo:

```python
enderecos = [
    "Av. José Bonifácio, 245 - Farroupilha, Porto Alegre - RS, 90040-130",
    "Av. Borges de Medeiros, 2035 - Menino Deus, Porto Alegre - RS, 90110-150",
    # Adicione mais endereços aqui
]
```

## 🔍 Principais Funções

### Funções de Automação

- `adiciona_destino(endereco, num_caixa=1)`: Adiciona um endereço na caixa de busca ou na rota
- `abre_rotas()`: Abre a aba de rotas no Google Maps
- `adiciona_caixa_destino()`: Adiciona uma nova caixa de destino
- `seleciona_tipo_conducao(tipo_conducao="Carro")`: Seleciona o meio de transporte
- `retorna_tempo_total()`: Retorna o tempo total da rota em minutos
- `retorna_distancia_total()`: Retorna a distância total da rota em quilômetros

### Funções de Otimização

- `gera_pares_distancia(enderecos)`: Coleta os tempos de viagem entre todos os pares de endereços
- `gera_otimizacao(enderecos, distancia_pares)`: Resolve o problema do Caixeiro Viajante usando PuLP
- `mostra_rota_otimizada(enderecos, solucao)`: Exibe a rota otimizada no Google Maps

## 🧮 Algoritmo de Otimização

O projeto utiliza programação linear inteira para resolver o problema do Caixeiro Viajante (TSP):

1. **Variáveis de Decisão**: Variáveis binárias indicando se uma aresta é usada na rota
2. **Função Objetivo**: Minimizar o tempo total de viagem
3. **Restrições**:
   - Cada cidade deve ter exatamente uma aresta de saída
   - Cada cidade deve ter exatamente uma aresta de entrada
   - Eliminação de sub-rotas (subtour elimination)

## ⚠️ Observações Importantes

- O projeto utiliza `sleep()` para aguardar o carregamento dos elementos. Em ambientes com conexão lenta, pode ser necessário ajustar esses tempos.
- O Google Maps pode alterar sua interface, o que pode exigir atualizações nos seletores XPath.
- O algoritmo de otimização pode ser lento para um grande número de endereços (complexidade exponencial do TSP).

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais.

## 👨‍💻 Autor

Projeto desenvolvido como parte do curso Asimov.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.


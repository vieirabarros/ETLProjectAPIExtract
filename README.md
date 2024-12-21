# Projeto de ETL com Python usando Requests

## Descrição
Este projeto implementa um processo de ETL (Extract, Transform, Load) usando a biblioteca `requests` do Python para consumir APIs REST. O objetivo é extrair dados de uma API pública, transformá-los e armazená-los em um banco de dados.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Bibliotecas Principais:**
  - `requests` - Para consumo de APIs.
  - `pandas` - Para manipulação de dados.
  - `sqlalchemy` - Para interação com o banco de dados.

## Estrutura do Projeto
```
/etl_project
  |-- main.py          # Script principal para execução do ETL
  |-- config.py        # Configurações do projeto
  |-- extract.py       # Funções para extração de dados
  |-- transform.py     # Funções para transformação de dados
  |-- load.py          # Funções para carregamento de dados
  |-- requirements.txt # Dependências do projeto
  |-- README.md        # Documentação principal
```

## Como Executar
### Pré-requisitos
- Python 3.x instalado
- Ambiente virtual configurado

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/etl_project.git
   cd etl_project
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script principal:
   ```bash
   python main.py
   ```

## Configuração
- Personalize o arquivo `config.py` para definir URLs de API, parâmetros de consulta e configurações de banco de dados.

## Contribuição
- Fork o repositório e envie pull requests com melhorias e novas funcionalidades.

## Licença
Este projeto está licenciado sob a MIT License. Consulte o arquivo `LICENSE` para mais detalhes.

---
**Observação:** Este README serve como um guia inicial e pode ser expandido conforme o desenvolvimento do projeto avança.


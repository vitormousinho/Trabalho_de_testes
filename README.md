## Projeto
Automação de testes de **API** para o **Swagger Petstore** (base URL: `https://petstore.swagger.io/v2`) usando **pytest** + **requests**.

O objetivo é validar cenários variados dos módulos:
- **Pet**
- **Store**
- **User**

## Tecnologias usadas
- **Python 3.11+**
- **pytest**
- **requests**
- **GitHub Actions** (CI)

## Instalação
Crie e ative um ambiente virtual (opcional, mas recomendado) e instale as dependências:

```bash
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Como executar os testes
Rodar todos os testes:

```bash
pytest -q
```

Rodar um arquivo específico:

```bash
pytest -q tests/test_pet.py
```

## Estrutura de pastas
```
.
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   ├── test_pet.py
│   ├── test_store.py
│   └── test_user.py
├── utils/
│   ├── api_client.py
│   ├── ids.py
│   └── payloads.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Prints do funcionamento (reservado)
- (Cole aqui prints da execução local do `pytest` e do workflow no GitHub Actions)

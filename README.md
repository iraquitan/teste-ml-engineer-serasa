# Teste Machine Learning Engineer (Serasa)

Crie uma API para servir um modelo de aprendizado de máquina, dado:

1. Um modelo sklearn (classificador) com duas classes e três features (classifier.joblib)
2. Uma transformação nos inputs do modelo (transform.joblib)
3. Python 3.8
4. scikit-learn==1.0.2

Você tem total liberdade para escolher as tecnologias para servir o modelo.

## Criando ambiente python

- scikit-learn e joblib (para carregar o modelo e transformadores de dado)
- FastAPI e uvicorn (para criar e servir a API)
- pydantic (validação dos dados na api)
- pandas (carregar e validar dados enviados pela API)

```shell
conda create -n ml_eng_py38 -c conda-forge python=3.8 scikit-learn=1.0.2 pandas=1.4.2 numpy=1.22.4
```

Ativando o novo ambiente:

```shell
conda activate ml_eng_py38
```

Instalando libs adicionais para o desenvolvimento da API:

```shell
python -m pip install -f requirements.txt
```

## Antes de rodar

Criar um arquivo **.env** com as seguintes variáveis para carregar o modelo

```
transformer_path=transform[84].joblib
classifier_path=classifier[27].joblib
```

E também colocar os arquivos **transform[84].joblib** e **classifier[27].joblib** na raiz do projeto, no final a estrutura de pastas deve ficar da seguinte forma:

```shell
.
├── README.md
├── classifier[27].joblib
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── data_model.py
│   ├── main.py
│   └── preprocess.py
├── test_main.py
└── transform[84].joblib
```

## Rodar API FastAPI

Para rodar a API localmente é preciso rodar o seguinte comando no terminal depois de ativar o ambiente usando o comando `conda activate ml_eng_py38`:

```shell
uvicorn main:app --host 127.0.0.1 --port 8000
```

Com a API rodando é possível acessar **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs>)** para acessar uma interface da API ([Swagger UI](https://github.com/swagger-api/swagger-ui))

## Testes

É possível rodar os testes usando o comando:

```shell
$ pytest
================================================ test session starts =================================================
platform win32 -- Python 3.8.13, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\iraqu\Developer\ml_engineering_serasa
plugins: anyio-3.6.1
collected 3 items

test_main.py ...                                                                                                [100%]

================================================= 3 passed in 1.80s ==================================================
```

## Descrição da API

A API consiste em fazer a transformação e predição usando 3 endpoints com formato de dados de entrada distintos.

### Predict Single Input

É possível fazer predições de apenas uma entrada chamando o endpoint **/predict-single** com um json no seguinte formato:

```json
{
  "feat1": 10,
  "feat2": 20,
  "feat3": 30
}
```

### Predict Batch Input

É possível fazer predições de várias entradas chamando o endpoint **/predict-batch** com um json no seguinte formato:

```json
{
  "inputs": [
    {
      "feat1": 10,
      "feat2": 20,
      "feat3": 30
    },
    {
      "feat1": 0,
      "feat2": 2,
      "feat3": 2
    }
  ]
}
```

### Predict CSV file Input

É possível fazer predições de um arquivo com várias entradas chamando o endpoint **/predict-file** com um arquivo CSV no seguinte formato:

```csv
feat1,feat2,feat3
10,20,30
1,0,0
0,0,1
1,1,0
10,0,0
```

## Autor

**Iraquitan Cordeiro Filho**

- Github: <https://github.com/iraquitan>
- Linkedin: <https://www.linkedin.com/in/iraquitan/>

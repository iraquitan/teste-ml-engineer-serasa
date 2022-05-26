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

## Rodar API FastAPI

Para rodar a API localmente é preciso rodar o seguinte comando no terminal:

```shell
uvicorn main:app --host 127.0.0.1 --port 8000
```

## Predict Single Input

É possível fazer predições de apenas uma entrada chamando o endpoint **/predict-single** com um json no seguinte formato:

```json
{
  "feat1": 10,
  "feat2": 20,
  "feat3": 30
}
```

## Predict Batch Input

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

## Predict CSV file Input

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

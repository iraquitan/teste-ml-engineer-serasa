api_title = "SerasaMachineLearningApi"

api_version = "0.0.1"

api_license_info = {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}

api_terms_of_service = "http://example.com/terms/"

api_description = """
Serasa - Machine Learning API helps you predict your data using three input strategies. 🚀

## Predict Single Input

You can make predictions by calling the **/predict-single** endpoint with a json in the format:

```json
{
  "feat1": 10,
  "feat2": 20,
  "feat3": 30
}
```

## Predict Batch Input

You can make predictions by calling the **/predict-batch** endpoint with a json in the format:

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

You can make predictions by calling the **/predict-file** endpoint and sending a multipart CSV file in the format:

```csv
feat1,feat2,feat3
10,20,30
1,0,0
0,0,1
1,1,0
10,0,0
```
"""

api_tags_metadata = [
    {
        "name": "predict-single",
        "description": "Predicts a single input with features (_feat1_, _feat2_, _feat3_)",
    },
    {
        "name": "predict-batch",
        "description": "Predicts a batch of inputs with features (_feat1_, _feat2_, _feat3_)",
    },
    {
        "name": "predict-file",
        "description": "Predicts a single CSV file with columns/features (_feat1_, _feat2_, _feat3_)",
    },
]

api_contact_info = {
    "name": "Iraquitan Cordeiro Filho",
    "url": "https://www.linkedin.com/in/iraquitan/",
    "email": "iraquitanfilho@gmail.com",
}

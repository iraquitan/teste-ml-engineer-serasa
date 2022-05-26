from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "API_name": "Machine Learning API - Serasa",
        "endpoints": [
            {
                "/predict-single": "Predicts a single input with features (feat1, feat2, feat3)"
            },
            {
                "/predict-batch": "Predicts a batch of inputs with features (feat1, feat2, feat3)"
            },
            {
                "/predict-file": "Predicts a single CSV file with columns/features (feat1, feat2, feat3)"
            },
        ],
    }


def test_predict_single():
    with TestClient(app) as client_event:
        response = client_event.post(
            "/predict-single", json={"feat1": 10, "feat2": 20, "feat3": 30}
        )
        assert response.status_code == 200
        assert response.json() == {"prediction": 1}


def test_predict_batch():
    with TestClient(app) as client_event:
        response = client_event.post(
            "/predict-batch",
            json={
                "inputs": [
                    {"feat1": 10, "feat2": 20, "feat3": 30},
                    {"feat1": 10, "feat2": 20, "feat3": 30},
                    {"feat1": 10, "feat2": 20, "feat3": 30},
                ]
            },
        )
        assert response.status_code == 200
        assert response.json() == {"prediction": [1, 1, 1]}


# TODO: Finish test_predict_file
# def test_predict_file():
#     with open("test.csv") as f:
#         csv_data = f.read()
#     with TestClient(app) as client_event:
#         response = client_event.post(
#             "/predict-file",
#             headers={"Content-Type": "multipart/form-data"},
#             data={"file": csv_data.encode("utf-8")},
#         )
#         assert response.status_code == 200
#         assert response.json() == {"prediction": [1, 1, 1]}

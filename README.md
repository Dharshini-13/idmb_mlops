
# IMDB Sentiment Analysis Demo

This package contains a trained sentiment analysis model using synthetic IMDB-like movie reviews.

## Files
- `model.pkl` - trained scikit-learn model (TF-IDF + LogisticRegression)
- `metadata.json` - information about dataset and accuracy
- `README.md` - this file

## Usage
```python
import pickle
model = pickle.load(open("model.pkl", "rb"))
print(model.predict(["The movie was excellent and thrilling!"]))
```

## CI/CD & DVC Integration

This repository includes:
- `.github/workflows/ci.yml` — GitHub Actions workflow to run tests, initialize DVC, `dvc pull`, `dvc repro`, and optionally `dvc push` when `secrets.DVC_REMOTE_URL` is configured.
- `dvc.yaml` — DVC stages for `prepare` and `train`.
- `params.yaml` — training parameters for reproducibility.

How to set up DVC remote (example using HTTP remote):
```bash
dvc remote add -d storage https://your-storage.example.com/path
dvc remote modify storage --local auth basic
dvc remote modify storage --local user <username>
dvc remote modify storage --local password <password>
dvc push
```

In GitHub Actions, add repository secrets:
- `DVC_REMOTE_URL` — the URL of the DVC remote (e.g. an S3 or HTTP endpoint)
- `DVC_REMOTE_TOKEN` — optional token used by the workflow to authenticate before `dvc pull` / `dvc push`

The CI workflow will skip `dvc pull` if `DVC_REMOTE_URL` is not set.

import pandas as pd
from pathlib import Path

# This script prepares data files for DVC pipeline. If data/train.csv and data/test.csv already exist, it does nothing.
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
train_csv = data_dir / "train.csv"
test_csv = data_dir / "test.csv"

if train_csv.exists() and test_csv.exists():
    print("Data files already exist. Skipping generation.")
else:
    # Fallback: create small sample dataset
    samples = [
        ("An amazing movie with great performances and storytelling.", 1),
        ("I hated this movie. It was boring and too long.", 0),
        ("Fantastic direction and acting. Highly recommended!", 1),
        ("Awful plot and bad acting. Waste of time.", 0),
        ("Loved the cinematography and soundtrack!", 1),
        ("Terrible movie with weak characters.", 0),
        ("One of the best films I've seen this year.", 1),
        ("Predictable and poorly executed.", 0),
    ]
    df = pd.DataFrame(samples, columns=["text","label"])
    df.to_csv(train_csv, index=False)
    df.to_csv(test_csv, index=False)
    print(f"Generated {train_csv} and {test_csv}")

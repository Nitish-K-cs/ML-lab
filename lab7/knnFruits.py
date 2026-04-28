import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

fruit_df = pd.read_csv("C:/Users/pc/Documents/Nitish093/lab7/fruit.csv")

X = fruit_df.drop("fruit_label", axis=1)
y = fruit_df["fruit_label"]

splits = [("90-10", 0.1), ("70-30", 0.3)]

k_values = [3, 5, 7]

distance_metrics = [
    ("Euclidean", "minkowski"),
    ("Manhattan", "manhattan")
]

all_labels = np.unique(y)

for split_name, test_size in splits:
    print(f"\n==== Split: {split_name} ====")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    for k in k_values:

        for name, metric in distance_metrics:

            knn = KNeighborsClassifier(n_neighbors=k, metric=metric)
            knn.fit(X_train, y_train)

            y_pred = knn.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            cm = confusion_matrix(y_test, y_pred, labels=all_labels)

            print(f"\nK = {k} | Distance = {name}")
            print(f"Accuracy: {acc:.4f}")
            print("Confusion Matrix:")
            print(cm)
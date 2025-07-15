import pandas as pd
from sklearn.cluster import KMeans
from .config import N_CLUSTERS, RANDOM_STATE, RISK_THRESHOLD

class BPClusterModel:
    def __init__(self, n_clusters=N_CLUSTERS, random_state=RANDOM_STATE):
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)

    def fit_predict(self, X: pd.DataFrame):
        labels = self.kmeans.fit_predict(X)
        X = X.copy()
        X["cluster"] = labels

        centroids = X.groupby("cluster")[["sabah_sistolik","aksam_sistolik"]].mean()
        risky = centroids.mean(axis=1).idxmax()
        X["risk"] = X["cluster"].apply(lambda c: "Risk" if c == risky else "Normal")
        return X, risky

    @staticmethod
    def global_risk(risk_col: pd.Series, threshold=RISK_THRESHOLD):
        risky = risk_col.value_counts().get("Risk", 0)
        return "Yüksek Tansiyon / Kalp Riski" if risky/len(risk_col) >= threshold else "Normal Tansiyon"

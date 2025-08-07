import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import streamlit as st
from tsyn import data_loader, preprocessing, model, viz

st.title(" TSYN | Akıllı Tansiyon Analizi")

uploaded = st.file_uploader(" Excel dosyanı yükle", type=["xlsx"])
if uploaded:
    df = data_loader.load_excel(uploaded)

    #  Tansiyon değerlerini ayır
    df = df.join(preprocessing.split_bp(df["Sabah Tansiyon"]).add_prefix("sabah_"))
    df = df.join(preprocessing.split_bp(df["Akşam Tansiyon"]).add_prefix("aksam_"))

    #  Modelleme
    features = df[["sabah_sistolik","sabah_diyastolik","aksam_sistolik","aksam_diyastolik"]].dropna()
    bp_model = model.BPClusterModel()
    labeled, _ = bp_model.fit_predict(features)
    df = df.join(labeled["risk"])

    #  Sonuçları göster
    st.subheader(" Günlük Risk Durumu")
    st.dataframe(df[["Tarih", "risk"]])

    st.subheader(" Risk Dağılımı")
    st.pyplot(viz.risk_pie(df["risk"]))

    genel = model.BPClusterModel.global_risk(df["risk"])
    st.success(f" Genel Değerlendirme: {genel}")

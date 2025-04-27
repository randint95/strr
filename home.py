import streamlit as st
import pandas as pd


st.title("らくらく機械学習!")
st.write("このページはらくらく機械学習!のホームページです。")
st.write("らくらく機械学習ではcsvファイルとexcelファイルを使って「楽に」機械学習を行うことができます。")
st.write("このページではお持ちのcsvファイルのプレビューを表示することができます。")

updata = st.file_uploader("200MB未満のcsvファイルをアップロードできます。")
encoding = st.radio("csvファイルのコーデックを選択してください。",["utf-8","shift_jis","cp932"])
header = st.checkbox("ヘッダー(列名)がある場合はチェックを入れてください。")
index = st.checkbox("インデックス列がある場合はチェックを入れてください。")
st.write("アップロードや設定が終わったら下のボタンを押してください。")
if st.button("プレビューの表示") and updata is not None:
    if header is not None:
        header = 0
    if index is not None:
        index = 0
    df = pd.read_csv(updata,index_col=index,header=header,encoding=encoding)
    st.dataframe(df)
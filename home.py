import streamlit as st
import pandas as pd


st.title("らくらく機械学習!")
st.write("このページはらくらく機械学習!のホームページです。")
st.write("らくらく機械学習ではcsvファイルを使って「楽に」機械学習を行うことができます。")
st.write("このページではお持ちのcsvファイルのプレビューを表示することができます。")
import streamlit as st
import pandas as pd

st.title("CSVファイルプレビュー")

updata = st.file_uploader("200MB未満のcsvファイルをアップロードできます。", type=['csv'])

encoding = st.radio("csvファイルのコーデックを選択してください。",["utf-8","shift_jis","cp932"])

has_header = st.checkbox("ヘッダー(列名)がある場合はチェックを入れてください。", value=True)
has_index = st.checkbox("インデックス列がある場合はチェックを入れてください。", value=False)

st.write("アップロードや設定が終わったら下のボタンを押してください。")

if st.button("プレビューの表示"):
    if updata is not None:
        try:
            header_param = 0 if has_header else None
            index_param = 0 if has_index else None

            df = pd.read_csv(
                updata,
                index_col=index_param,
                header=header_param,
                encoding=encoding
            )

            st.write("---")
            st.write("### ファイルプレビュー")
            st.dataframe(df)

        except Exception as e:
            st.error(f"ファイルの読み込み中にエラーが発生しました: {e}")
            st.error("選択したエンコーディングやヘッダー/インデックス設定がファイルの内容と合っていない可能性があります。設定を確認してください。")

    else:
        st.warning("ファイルをアップロードしてください。")

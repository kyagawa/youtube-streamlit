# 使用するライブラリのインポート
import streamlit as st
# import pandas as pd
# import numpy as np
# from PIL import Image
import time

# タイトルの追加
st.title('Streamlit 入門')

# テキストを記述する
st.write('プログレスバーの表示')
'Start!!'

# 空で用意するので、最初は表示されない（barの上に表示される）
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)


'Dane!!'

left_colunm, right_column = st.columns(2)
button = left_colunm.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander１ = st.expander('問い合わせ１')
expander１.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



# text = st.text_input(
#     'あなたの趣味を教えて下さい。'
# )
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション', condition


# # st.checkboxはTrue or Falseが返ってくる
# # if文を用いることで、チェックボックスをつけていれば表示させ、つけていない場合非表示とすることができる
# if st.checkbox('Show Image'):
#     img = Image.open('dog.jpeg')
#     # use_column_width=Trueで横幅を合わせて表示させることができる
#     st.image(img, caption='dog', use_column_width=True)




# # 緯度・経度をマッピング
# df = pd.DataFrame(
#     np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)
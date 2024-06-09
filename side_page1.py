import streamlit as st
import pandas as pd

st.sidebar.markdown("side_page1")
st.markdown("side_page1")
st.markdown("#소재품질전략_이광원TL(문의사항은 Cube DM 부탁드립니다")

# 데이터 준비
data = {
    'date': ['Jan 1, 2023', 'Feb 1, 2023', 'Mar 1, 2023', 'Apr 1, 2023','May 1, 2023', 'Jun 1, 2023', 'Jul 1, 2023', 'Aug 1, 2023','Oct 1, 2023', 'Nov 1, 2023', 'Dec 1, 2023', 'Apr 1, 2023'],
    'low': [10, 20, 30, 40, 15, 25, 35, 45, 20, 30, 40, 50],
    'high': [30, 40, 70, 100, 35, 45, 80, 90, 150, 200, 300, 400],
    'open': [15, 25, 35, 80, 20, 25, 35, 50, 20, 35, 50, 90],
    'close': [10, 20, 30, 40, 35, 45, 80, 85, 100, 150, 200, 51],
    'volume': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

# DataFrame 생성
df = pd.DataFrame(data)
st.table(df)
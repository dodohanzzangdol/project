import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.font_manager as fm
import platform
from matplotlib import rc


# 한글 폰트 설정 (Windows 기준)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 깃허브 리눅스 기준
if platform.system() == 'Linux':
    fontname = './NanumGothic.ttf'
    font_files = fm.findSystemFonts(fontpaths=fontname)
    fm.fontManager.addfont(fontname)
    fm._load_fontmanager(try_read_cache=False)
    rc('font', family='NanumGothic')

# 페이지 제목
st.title("데이터프레임 & 시각화 Streamlit 페이지")

# -----------------------------
# 시각화 예시 — 노트북에서 사용한 차트 형태를 streamlit용으로 변환
# -----------------------------
st.subheader("금 시세와 환율 시각화")

fig, ax = plt.subplots()
ax.plot(df['Close'], label='금 시세')
ax.plot(df['USD'], label='환율')
ax.set_xlabel('날짜')
ax.set_ylabel('값')
ax.set_title('금 시세 & 환율 변화')
ax.legend()

st.pyplot(fig)
ax.plot(df["날짜"], df["가격"])
ax.set_xlabel("날짜")
ax.set_ylabel("가격")
ax.set_title("가격 변화 추이")

st.pyplot(fig)

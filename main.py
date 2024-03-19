import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 국가 데이터를 생성하는 함수
@st.cache_data
def create_real_data():
    data = {
        'Country': ['South Korea', 'United States', 'Canada', 'Germany', 'China',
                    'Japan', 'India', 'Russia', 'France', 'Kenya',
                    'Brazil', 'Mexico', 'Australia', 'Greece'],
        'Population': [51780579, 331002651, 37742154, 83783942, 1439323776,
                       126476461, 1380004385, 145934462, 65273511, 53771296,
                       212559417, 128932753, 25499884, 10724599],  # 인구
        'GDP': [1.6309e12, 21.433e12, 1.643e12, 3.806e12, 14.343e12,
                5.082e12, 2.869e12, 1.648e12, 2.603e12, 95.5e9,
                1.445e12, 1.274e12, 1.337e12, 209.85e9],  # GDP
        'Life Expectancy': [83.03, 78.79, 82.43, 81.33, 76.91,
                            84.36, 69.42, 72.58, 82.57, 66.7,
                            75.88, 76.86, 82.8, 81.4]  # 기대 수명
    }
    return pd.DataFrame(data)

# "백만 명" 단위로 변환하는 함수
def to_millions(x, pos):
    return '{:1.1f}M'.format(x*1e-6)

# "십억 달러" 단위로 변환하는 함수
def to_billions(x, pos):
    return '{:1.1f}B'.format(x*1e-9)

# 스트림릿 앱 시작
def main():
    st.title("국가별")
    st.subheader("인구(Millions), GDP(Billions), 기대 수명")

    df = create_real_data()

    # 인구 차트
    fig, ax = plt.subplots(3, 1, figsize=(10, 18), tight_layout=True)
    
    formatter_millions = FuncFormatter(to_millions)
    ax[0].bar(df['Country'], df['Population'], color='skyblue')
    ax[0].set_title('Population')
    ax[0].set_xticklabels(df['Country'], rotation=45, ha='right')
    ax[0].set_ylabel('Population')
    ax[0].yaxis.set_major_formatter(formatter_millions)

    # GDP 차트
    formatter_billions = FuncFormatter(to_billions)
    ax[1].bar(df['Country'], df['GDP'], color='lightgreen')
    ax[1].set_title('GDP')
    ax[1].set_xticklabels(df['Country'], rotation=45, ha='right')
    ax[1].set_ylabel('GDP (USD)')
    ax[1].yaxis.set_major_formatter(formatter_billions)

    # 기대 수명 차트
    ax[2].bar(df['Country'], df['Life Expectancy'], color='salmon')
    ax[2].set_title('Life Expectancy')
    ax[2].set_xticklabels(df['Country'], rotation=45, ha='right')
    ax[2].set_ylabel('Life Expectancy (Years)')

    st.pyplot(fig)

if __name__ == "__main__":
    main()
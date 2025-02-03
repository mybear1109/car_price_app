
import streamlit as st
import pandas as pd


from UI.eda import run_eda # type: ignore
from UI.home import run_home # type: ignore
from UI.ml import run_ml # type: ignore


def main():
    st.title('자동차 가격 예측 앱')


    menu = ['Home', 'EDA', 'ML']
    chioce = st.sidebar.selectbox('메뉴', menu)

    if chioce == menu[0]:
        run_home()
    elif chioce == menu[1]:
        run_eda()
    elif chioce == menu[2]:
        run_ml()


if __name__ == '__main__':
    main()


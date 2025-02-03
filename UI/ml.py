
import joblib
import streamlit as st
import numpy as np 


def run_ml() :
    # 유저에게 예측에 필요한 데이터를 입력받는다.
    # 나이, 연봉, 신용카드 부채, 순자산을 입력받는다.

    st.subheader('정보를 입력해주세요')


    # 1. 나이 입력받기 
    age = st.number_input('나이를 입력하세요', min_value=18, max_value=100)
    st.write('나이는 ', age, '살 입니다.')

    # 2. 연봉 입력받기(만단위로 입력받는다.)
    annual_salary = st.number_input('연봉을 입력하세요', min_value=10000,value=10000)
    st.write('연봉은 $', annual_salary , '입니다.')

    # 3. 신용카드 부채 입력받기
    credit_card_debt = st.number_input('신용카드 부채를 입력하세요', min_value=0, value=10000)
    st.write('신용카드 부채는 $', credit_card_debt, '입니다.')

    # 4. 순자산 입력받기
    net_worth = st.number_input('순자산을 입력하세요', min_value=1000, value=3000)
    st.write('순자산은 $', net_worth, ' 입니다.')


    # 5. 예측하기 버튼을 누르면,

    # 인공지능으로 예측하여, 결과를 화면에 보여준다. 
    if st.button('구매 금액 예측하기') : 
        regressor = joblib.load('model/regressor1.pkl')
        new_data = np.array([age, annual_salary, credit_card_debt, net_worth]).reshape(1, -1)
        y_pred = regressor.predict(new_data)
        pred_data = y_pred[0]

        if pred_data < 0 : 
            st.error('예측이 불가한 정보입니다. 다시 입력해주세요.')
        else :
            # 소수점은 버리고 정수부분만 가져오는것
            pred_data = round(pred_data)
            # 숫자 3자리마다 ,를 찍어주는것
            pred_data = "{:,}".format(pred_data)
            st.success(f'예측 금액은 ${pred_data} 입니다.')


        


   








 

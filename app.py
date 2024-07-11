import streamlit as st
import pickle
import numpy as np 

model = pickle.load(open('bhp_model.pickle','rb'))
X = pickle.load(open('data.pickle','rb'))
location_ = pickle.load(open('locations.pickle','rb'))


def predict_price(location,sqft,bath,bhk):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return model.predict([x])[0]
def main():
    st.title("Bangalore house price prediction")
    location = st.selectbox('Location:',location_)
    sqft = st.text_input('Area (square feet):')
    bath = st.selectbox('Number of Bathrooms:', [1,2,3,4,5,6,7,8,9,10])
    bhk = st.selectbox('Number of rooms:',[1,2,3,4,5,6,7,8,9,10])
    if st.button("predict the price"):
        try:
          output = round(predict_price(location,sqft,bath,bhk),2)
          st.success(f"The price is Rs. {output} Lakh")
        except:
          st.exception(ValueError("Enter a valid input for area."))


if __name__=='__main__':
    main()


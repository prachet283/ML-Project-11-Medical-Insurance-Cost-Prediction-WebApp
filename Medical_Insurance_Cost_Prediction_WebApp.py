import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("medical_insurance_cost_prediction_model.sav",'rb'))

#creating a function for prediction

def medical_insurance_cost_prediction(input_data):

    #changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting on 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)

    return prediction[0]

def main():
    
    #giving a title
    st.title('Medical Insurance Cost Prediction Web App')
    
    #getting input data from user
    
    age = st.number_input("Age of the person")
    option1 = st.selectbox('Gender',('Male', 'Female')) 
    sex = 1 if option1 == 'Female' else 0
    bmi = st.number_input("BMI")
    children = st.number_input("No. of children")
    option2 = st.selectbox('Smoker',('Yes', 'No'))
    smoker = 1 if option2 == 'No' else 0
    option3 = st.selectbox('Region',('Southeast', 'Southwest','Northwest','Northeast'))
    if option3 == 'Southeast':
        region = 0
    elif option3 == 'Southwest':
        region = 1
    elif option3 == 'Northwest':
        region = 2
    else:
        region = 3
    

    # code for prediction
    price = ''
    
    #creating a button for Prediction
    if st.button('Predict Medical Insurance Cost'):
        price = medical_insurance_cost_prediction((age,sex,bmi,children,smoker,region))
        
    st.success('The Predicted Price: '+ str(price)+'$')



if __name__ == '__main__':
    main()
    

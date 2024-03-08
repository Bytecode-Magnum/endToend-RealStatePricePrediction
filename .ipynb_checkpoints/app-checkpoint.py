import pickle
import streamlit as st

# Load the trained model
with open('RealStatePrice.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the Streamlit app
def main():
    st.title('House Price Prediction App')
    
    # Input fields for user to enter 'Distance to the nearest MRT station' and 'Number of convenience stores'
    distance = st.number_input("Distance to the nearest MRT station", value=0.0, step=0.1, format="%.1f", placeholder="Enter distance")
    convenience_stores = st.number_input("Number of convenience stores", value=0, placeholder="Enter number of stores")
    
    
    # Predict house price based on user input
    if st.button('Predict'):
        prediction = model.predict([[distance, convenience_stores]])
        st.success(f"The predicted house price is {prediction[0]}")

# Run the Streamlit app
if __name__ == '__main__':
    main()

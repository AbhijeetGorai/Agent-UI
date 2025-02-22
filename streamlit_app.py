import streamlit as st
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title='Query Search App', page_icon='🔍', layout='centered')
st.title('Query Search App')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        border: 2px solid red;
        padding: 8px;
        border-radius: 5px;
    }
    .stButton > button {
        background-color: green;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: darkgreen;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input box for user query
user_query = st.text_input('Enter your query:')

# Submit button
if st.button('Submit'):
    if user_query:
        # Call the API with the user query
        api_url = 'https://agent-demo-xkj0.onrender.com/search'  # Replace with your actual API endpoint
        response = requests.post(api_url, json={'question': user_query})
        if response.status_code == 200:
            st.subheader('Response:')
            st.write(response.json())
        else:
            st.error('Failed to get response from API')
    else:
        st.warning('Please enter a query before submitting!')


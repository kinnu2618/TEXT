import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key


genai.configure(api_key=google_gemini_api_key)


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 2048,
    "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)

def generate_blog_post(title, keywords, num_words):
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Generate a comprehensive, engaging blog post relevant to the given title \"{title}\" and keywords \"{keywords}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
                ],
            },
        ]
    )
    response = chat_session.send_message("INSERT_INPUT_HERE")
    return response.text

st.set_page_config(layout="wide")

st.title('B L O G 👻')
st.subheader('Enter your topic and get a blog post generated for you!')

with st.sidebar:
    st.title("INPUT YOUR BLOG DETAILS")
    st.subheader("ENTER DETAILS OF THE BLOG")

    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of Words", min_value=1000, max_value=100000, step=100)
    
    submit_button = st.button("Generate Blog Post 📝")

if submit_button:
    if blog_title and keywords:
        with st.spinner("Generating blog post..."):
            blog_content = generate_blog_post(blog_title, keywords, num_words)
            
            st.write(blog_content)
    else:
        st.error("Please provide both a blog title and keywords.")

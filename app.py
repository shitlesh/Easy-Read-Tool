import os
import torch
from diffusers import StableDiffusionPipeline, DiffusionPipeline
from constants import Streamlit_style
from helper import Helper
import io
import streamlit as st
from requests.exceptions import ChunkedEncodingError
from transformers import BartTokenizerFast, BartForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM


# Streamlit UI
st.set_page_config(page_title="Easy Read Document")

model_id = "stabilityai/stable-diffusion-xl-base-1.0"

@st.cache_resource()
def setup_mps_device():
    if torch.backends.mps.is_available():
        mps_device = torch.device("mps")
        return mps_device
    else:
        st.warning("MPS device is not available.")
        return torch.device("cpu")

@st.cache_resource()
def initialize_models(model_id):
    """Cache hitting function."""
    # Load the saved tokenizer and model for text summarization
    tokenizer = AutoTokenizer.from_pretrained("best_text_summ_token", local_files_only=True)
    model = AutoModelForSeq2SeqLM.from_pretrained("best_text_summ_model", local_files_only=True)
    
    # Load the saved pipeline for text-to-image generation
    pipeline = DiffusionPipeline.from_pretrained(model_id)
    device = setup_mps_device()
    pipeline.to(device)

    helper_class = Helper()
    tokenizer = model = None

    return tokenizer, model, pipeline, helper_class


summary_tokenizer, summary_model, text_to_image_pipeline, helper_class = initialize_models(model_id)


# Custom CSS
st.markdown(Streamlit_style, unsafe_allow_html=True)


st.image("static/USW.png", width=100)
st.markdown("<h1 style='text-align: center;'>Easy Read Document</h1>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # File details
    st.markdown(f"""
    <div class="file-details">
        <h2>Uploaded file details:</h2>
        <p>Filename: {uploaded_file.name}</p>
    </div>
    """, unsafe_allow_html=True)

    # Process and summarize the PDF
    with st.spinner("Processing..."):
        # Save the uploaded file
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        ## Extract text from PDF
        full_text = helper_class.extract_text_from_pdf(file_path)
        paragraphs = full_text.split('\n')

    
        # Summarize each paragraph
        st.markdown("<h2>Summarized Text:</h2>", unsafe_allow_html=True)
        
        # device = setup_mps_device()
        
        for i in range(len(paragraphs)):
            print(i)
            if paragraphs[i].strip():
                summary = helper_class.summarize_text(paragraphs[i], summary_tokenizer, summary_model, max_length=100)
                
                image = helper_class.image_generation(summary, text_to_image_pipeline)
                
                # Create two columns
                col1, col2 = st.columns([3, 1])
                
                #Summary for left column
                with col1:
                    st.markdown(f"<div class='output'>{summary}</div>", unsafe_allow_html=True)
                
                #Image for right column
                with col2:
                     if image is not None:
                        img_byte_arr = io.BytesIO()
                        image.save(img_byte_arr, format='PNG')
                        img_byte_arr = img_byte_arr.getvalue()
                        st.image(img_byte_arr, use_column_width=True)
                     else:
                        st.warning(f"Failed to generate image for this summary")
        
     
    st.markdown(f"""
    <div class="paragraph-details">
        <h2>Total paragraphs:</h2>
        <p>No of paragraphs: {len(paragraphs)}</p>
    </div>
    """, unsafe_allow_html=True)           

st.markdown('</div>', unsafe_allow_html=True)

# Input container
user_input = st.text_input("You can start any conversation with me or upload only PDF files", key="user_input")

if st.button("Send"):
    if user_input:
        st.markdown(f"<div class='output'>User: {user_input}</div>", unsafe_allow_html=True)
        # Here you would process the user input and generate a response
        # For now, we'll just echo the input
        st.markdown(f"<div class='output'>Bot: You said: {user_input}</div>", unsafe_allow_html=True)
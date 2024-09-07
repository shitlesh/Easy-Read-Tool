''' Style Constants for the Streamlit App '''
Streamlit_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Poppins:wght@700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

    :root {
        --bg-color: #f5f5f5;
        --text-color: #333;
        --input-bg: #ffffff;
        --border-color: #e0e0e0;
        --chat-bg: #ffffff;
        --file-details-bg: #f0f0f0;
    }

    .stApp {
        font-family: 'Roboto', sans-serif;
        background-color: var(--background-color);
        color: var(--text-color);
    }

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px;
        background-color: var(--input-bg);
        border-bottom: 1px solid var(--border-color);
    }

    .logo {
        width: 100px;
    }

    .title {
        font-family: 'Poppins', sans-serif;
        font-size: 28px;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(45deg, #007BFF, #00BFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .file-details {
        background-color: var(--file-details-bg);
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        color: var(--text-color);
        margin-top: 20px;
    }

    .stTextInput > div > div > input {
        background-color: var(--input-bg);
        color: var(--text-color);
    }

    .stButton > button {
        background-color: #007BFF;
        color: white;
    }

    .output {
        font-family: Arial, sans-serif;
        white-space: pre-wrap;
    }
</style>
"""


Text = """

"""
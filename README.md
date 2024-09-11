![made-with](https://img.shields.io/badge/Made%20with-Python3-brightgreen)
![made-with-huggingface](https://img.shields.io/badge/Hugging%20Face-yellow)
![built-with-Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![Uses-jupyter](https://img.shields.io/badge/Uses-Jupyter%20Notebook-orange)


<!-- LOGO -->
<br />
<h1>
<p align="center">
  <span style= "font-size: 100px;">Easy Read Tool</span>
</h1>
  <p align="center">
    An AI Tool to summarize pdf files with images.
    <br />
  </p>
</p>
<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#demo-video">Demo Video</a> •
  <a href="#blame-me">Blame Me</a> •
</p>  

<p align="center">
  
![screenshot](demo/Easy_Read_GIF.gif)
</p>                                                                                                                             
                                                                                                                                                      
## About The Project

This project caters an advanced AI Tool which generate the concise summaries along with relevant images for the respective summaries from the lengthy PDF documents. It employed Google T5 architecture for text summarization, Stable Diffusion and LoRA weights to generate images and Streamlit for a user friendly interface for tool interaction. This project is a part of the dissertation for final year project of Masters in Artificial Intelligence.

## Clone Repository

You can clone this project from GitHub:
```py
git clone https://github.com/shitlesh/Easy-Read-Tool.git
```

## How to Use

Follow below steps to run this AI Tool successfully and get the intended result:

1. Install all required libraries listed in requirements.txt file. Use below command in your terminal:
```py
pip install -r requirements.txt 
```
2. Import Diffusers using below command on terminal:
```py
git clone https://github.com/huggingface/diffusers.git
cd diffusers
```
3. Open app.py file and run the file using below command on the terminal:
```py
run streamlit app.py
```
4. Next a web interface will open infront of you (at your default browser), upload a PDF file and click on upload button.
5. In few moments, you'll see the text summary with images next to it.

## Demo Video

[Download and watch the demo video](demo/Demo.mp4)

## Blame Me

If stepped into any issue while exploring this repo, please open an issue here :  [New Mess](https://github.com/shitlesh/Easy-Read-Tool/issues/new)


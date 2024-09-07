import PyPDF2
import torch

class Helper():

    def __init__(self):
        pass

    ''' Helper class for text extraction, summarization, and image generation '''
    @staticmethod
    def extract_text_from_pdf(pdf_path):
        ''' Extract text from a PDF file '''
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
        return text

    @staticmethod
    def summarize_text(text, tokenizer, model, max_length=100):
        ''' Summarize the given text using the loaded model '''
        input_ids = tokenizer(text, return_tensors="pt").input_ids
        output_ids = model.generate(input_ids, max_length=1000, num_beams=4, length_penalty=2.0, early_stopping=True)
        summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return summary

    @staticmethod
    def image_generation(text, pipeline):
        ''' Generate an image from the given text using the loaded model '''
        with torch.inference_mode():
            img = pipeline(text,
                           height=1024,
                           width=1024,
                           guidance_scale=6.5,
                           num_inference_steps=70).images[0]

        return img


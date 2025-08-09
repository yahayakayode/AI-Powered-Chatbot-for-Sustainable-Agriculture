# AI-Powered Conversational Chatbot for Sustainable Agriculture in Nigeria

![Chatbot Screenshot](https://github.com/user-attachments/assets/ccabd714-09f3-494d-bcc1-dfdd1f50a393)

## Overview
This project is an **AI-powered agricultural advisory chatbot** fine-tuned from the **Gemma 2B** model. It is designed to support Nigerian farmers — starting with maize production — by providing **instant, location-aware, and practical farming advice** from **site selection** to **storage**.  

The chatbot addresses key agricultural challenges such as lack of timely advice, climate variability, and poor access to expert guidance. Farmers can interact in plain language to receive **reliable, research-backed recommendations**.

---

## Live Demo
🔗 **[Try the CropXpert Chatbot on Hugging Face](https://huggingface.co/spaces/Justsp3cial/CropXpert)**  

---

## Features
- **Best practices for maize production** – from land preparation to post-harvest storage.
- **Location-based recommendations** tailored to specific Nigerian states or regions.
- **Pest and disease management** advice using sustainable methods.
- **User-friendly interface** accessible to farmers with minimal technical skills.

---

## Example Usage

## Recommendation for Maize varieties

<img width="628" height="277" alt="image" src="https://github.com/user-attachments/assets/28847d72-e56a-47ac-99e6-d3328a4e733b" />

## Location-based planting time recommendations
<img width="585" height="297" alt="image" src="https://github.com/user-attachments/assets/860e4ee7-8e97-44cc-b060-5a56f9674f8c" />

## Recommendations for pest and disease management 
<img width="564" height="297" alt="image" src="https://github.com/user-attachments/assets/4c1ff233-3d3e-4b18-acb6-9d4b5ad9dbd3" />

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/yahayakayode/AI-Powered-Chatbot-for-Sustainable-Agriculture.git
cd AI-Powered-Chatbot-for-Sustainable-Agriculture
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the chatbot locally

```bash
python app.py
```

You can also launch it directly in **Google Colab** for a quick test.

---

## Technical Details

* **Base Model:** Gemma 2B (English) – [More info](https://ai.google.dev/gemma/docs)
* **Fine-tuning:** LoRA & Keras on a maize-specific dataset.
* **Deployment:** Hugging Face Spaces with Gradio interface.

---

## Resources

* **Kaggle Notebook:** [Fine-tuning Gemma 2B for Maize Advisory](https://www.kaggle.com/code/yahayamkayode/fine-tuning-gemma2b-model-using-lora-and-keras)
* **Model on Hugging Face:** [Maize Model](https://huggingface.co/Justsp3cial/maize_model)
* **Live Demo:** [CropXpert Chatbot](https://huggingface.co/spaces/Justsp3cial/CropXpert)


---


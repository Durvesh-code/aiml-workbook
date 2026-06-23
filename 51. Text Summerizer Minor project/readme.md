# Text Summarization using Fine-Tuned T5 Transformer

![Text Summarizer App](./public/image.png)

## Overview
This project is an end-to-end Text Summarization web application. It uses a **T5 (Text-to-Text Transfer Transformer)** model fine-tuned on dialogue and conversational data to generate concise, accurate summaries of long text. The backend is powered by **FastAPI**, and it includes a sleek, modern, and responsive web UI.

## Architecture & Tech Stack
- **Machine Learning**: PyTorch, HuggingFace `transformers`, SentencePiece
- **Model**: `t5-small` (Fine-tuned)
- **Backend Framework**: FastAPI, Uvicorn
- **Frontend**: HTML5, CSS3, JavaScript
- **Training Environment**: Jupyter Notebook, Anaconda

## Fine-Tuning the Transformer
The model at the core of this app is a custom-trained version of Google's `t5-small`.
1. **Dataset**: Fine-tuned on the **SAMSum** dataset (which contains messenger-like conversations and corresponding human-written summaries).
2. **Preprocessing**: Text was thoroughly cleaned (HTML tags, spaces, and newlines removed) and tokenized using the Fast tokenizer.
3. **Training**: The model was trained over 5 epochs using the HuggingFace `Trainer` API with early stopping, attention masking, and specific learning rate adjustments.
4. **Outcome**: The resulting model is highly capable of understanding dialogue context and extracting key points.

*(Note: The Jupyter notebook containing the full dataset processing and fine-tuning code is available in the `Training_file/` directory).*

---

## ⚠️ Important Note: Missing Model Files 
The fine-tuned model (`saved_summary_model` directory) is **NOT** included in this GitHub repository. 

The total size of the fine-tuned model artifacts (including the `.safetensors` file and tokenizer data) exceeds **4 GB**. Because this surpasses GitHub's strict file size limits, the trained model cannot be uploaded. 

To run this project, you must first run the `text_summerizer.ipynb` notebook inside the `Training_file` directory to generate and save your own fine-tuned model weights.

---

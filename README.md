# 🕌 NawabiLLM: A Shayari-Speaking Language Model  
### *Fine-tuned + RAG-powered poetic chatbot in the tone of Urdu legends*

> 🎤 *"Sher bhi kahe, Lucknow bhi samjhe, aur dil bhi chu jaaye..."*  
> *An LLM rooted in Lucknow’s soul, trained on shayari, and born to charm hearts.*

---


![system design_nawabillm](https://github.com/user-attachments/assets/c88cb96f-268a-476f-b03b-a7b52585f45b)



## 🌟 Overview

**NawabiLLM** is a fine-tuned large language model that speaks in Urdu shayari, understands poetic tone and emotion, and can imitate the legendary styles of classical poets like Ghalib, Faiz, and Mir.  

Built as a full-stack Flask web app, NawabiLLM combines **deep learning**, **handcrafted prompts**, and **retrieval-augmented generation (RAG)** to create a poetic experience grounded in Lucknow’s timeless legacy.

---

## 🧠 What It Can Do

- 🪶 Generate Shayari on any theme (e.g., love, loss, longing)
- 🎭 Understand and respond in **emotion-aware tones**
- 🧾 Retrieve exact or similar ghazals via RAG when trained knowledge is insufficient
- 
---

## 📚 Dataset & Training Strategy

### 🧾 Corpus Composition

- ✍️ **Ghazals and Shers** scraped from [Rekhta.org](https://rekhta.org)
- 📖 **Wikipedia entries** on Lucknow’s language, culture, and nawabi etiquette
- 📘 **Historical books** on Awadh’s literature and poetic form
- 🧠 **Sentiment labels** (romantic, melancholic, spiritual, etc.) auto-generated using a pre-trained sentiment analyzer

### ⚙️ Model Workflow

| Component      | Role |
|----------------|------|
| ** QLoRA Finetuning** | Learn poetic style, tone & rhythm |
| **Prompt-Response Dataset** | Handcrafted from labeled ghazals |
| **Mistral-7B-Instruct** | Base model used for finetuning |
| **RAG Module** | Retrieves exact shers/ghazals for unseen queries |

> 💡 *Only a portion of the dataset is used for fine-tuning; the rest is accessible via RAG.*

---

## 🧠 Hybrid Strategy: Finetuning + RAG

### 1️⃣ QLoRA Finetuning
- Lightweight finetuning of **Mistral-7B-Instruct** on a portion of the corpus.
- Focused on prompt-response style learning and emotional conditioning.

### 2️⃣ Retrieval-Augmented Generation (RAG)
- For queries referencing **untrained** or **specific ghazals**, a RAG system:
  - Uses vector search (e.g., FAISS)
  - Retrieves relevant shers/ghazals from the labeled corpus
  - Feeds them into the model’s context window for **grounded generation**

> This hybrid approach ensures NawabiLLM is both creative and accurate — like a poet who remembers and improvises.

---

## 🏗️ Architecture

```mermaid
graph LR
A[User Input] --> B[Flask Backend]
B --> C[Prompt Formatter]
C --> D{RAG Triggered?}
D -- Yes --> E[Retrieve Ghazals from Corpus]
E --> F[NawabiLLM Inference]
D -- No --> F[NawabiLLM Inference]
F --> G[Jinja2 Frontend Response]
💻 Tech Stack
Component	Tech
LLM	Mistral-7B-Instruct (QLoRA finetuned)
Backend	Flask
Frontend	Jinja2 Templates
Data Labeling	Hugging Face Sentiment Analyzer
RAG	FAISS + SentenceTransformers
Hosting	Localhost / Streamlit (future)

🔮 Future Plans
 Deploy to Hugging Face Spaces or Render

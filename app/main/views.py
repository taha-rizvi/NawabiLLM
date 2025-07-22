from .import main
from flask import render_template,request,jsonify
import requests
from transformers import AutoTokenizer,AutoModelForCausalLM,BitsAndBytesConfig
import torch
from ragengine import RAGEngine
import pyngrok

@main.route('/',methods=['GET','POST'])

def index():
    if request.method=='POST':
        user_input=request.get_json()
        user_input=user_input['msg']
        retrieved=retrieve_context(user_input)
        final_retrieved=user_input+f"response{retrieved}"
        print(f"the retrieved data from rag: {final_retrieved}")
        colab_url = "https://bdabaf44e072.ngrok-free.app/receive"
        payload={"text":final_retrieved}
        try:
            response=requests.post(colab_url,json=payload)
            colab_result=response.json()['response']
            return jsonify({"reply":colab_result})
        except Exception as e:
            return jsonify({"reply": f"Error talking to Colab: {str(e)}"})

        
    else :
        return render_template('index.html')
def retrieve_context(user_input):
    engine=RAGEngine("data//index_combined_corpus.index","data//index_combined_corpus_meta.json")
    retrieved=engine.search(user_input)
    return retrieved


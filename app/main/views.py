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
        colab_url = "https://a38be346e24d.ngrok-free.app/receive"
        payload={"text":final_retrieved}
        try:
            response=requests.post(colab_url,json=payload)
            colab_result=response.json()['response']
            return jsonify({"reply":colab_result})
        except Exception as e:
            return jsonify({"reply": f"Error talking to Colab: {str(e)}"})

        
    else :
        return render_template('index.html')
    
# def sendtofrontend(reply):
#     payload={"reply":reply}
#     try:
#         response=requests.post("/",json=payload)
#         front_resp=response.json()
#         print("sending data fetched from colab to frontend....")
#         return front_resp['response']
#     except Exception as e:
#         return f"error sending data to frontend: {e}"
# @main.route("/fromcolab",methods=["GET","POST"])   
# def receive():
#     data=request.get_json()
#     if data:

#         reply=data["reply_from_llm"]
#         sendtofrontend(reply)
#         print(f"the reply from colab: {reply}")
#         return "Data Received"
#     else:
#         return "Data Not Received"
    

def retrieve_context(user_input):
    engine=RAGEngine("data//index_combined_corpus.index","data//index_combined_corpus_meta.json")
    retrieved=engine.search(user_input)
    return retrieved


# !pip install llama-cpp-python

from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
	filename="mistral-7b-instruct-v0.2.Q2_K.gguf",
)
user_question = input("❓ Ask your question: ")

# Run the model
response = llm.create_chat_completion(
    messages=[
        {"role": "user", "content": user_question}
    ]
)

# Print the result
print("\n🧠 Answer:")
print(response['choices'][0]['message']['content'])
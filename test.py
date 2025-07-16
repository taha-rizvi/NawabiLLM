from ragengine import RAGEngine

engine=RAGEngine("data//index_combined_corpus.index","data//index_combined_corpus_meta.json")
query="complete this ghazal atvār tire ahl-e-zamīñ se nahīñ milte\nandāz kisī a"

retrieved_outputs=engine.search(query)
for i in retrieved_outputs:
    print(i)
import json,random
output_file="data//combined_corpus.jsonl"
def load_json(file_path:str)-> list[str]:
    with open(file_path,'r',encoding='utf-8') as f:
        return [json.loads(line) for line in f]
corpus_sher=load_json("data//corpus_sher.jsonl")
couplets_corpus= load_json("data//couplets_corpus.jsonl")
corpus_poetbios=load_json("data//corpus_poetbios.jsonl")
corpus_general=load_json("data//corpus_general.jsonl")
data=[]
for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"Give me a ghazal by {poet_name}"
    data.append({"prompt":prompt,"response":response})
#prompt in lakhnavi andaz
for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"ama mia ek ghazal sunaiye {poet_name} sahab ki"  
    data.append({"prompt":prompt,"response":f" ama mia aapke lehje ne humein jeetliya! ye lijiye {poet_name} sahab ki ek khoobsurat ghazal humari aaghosh se nikalta hua....\n {response}"})

for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"ustaad ek ghazal hojaye {poet_name} sahab ki"  
    data.append({"prompt":prompt,"response":f" bilkul janab apka hukm sar-aankhon par! ye lijiye {poet_name} ki ek zabardast ghazal\n {response}"})   

for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"{poet_name} ki ghazal sunao"  
    data.append({"prompt":prompt,"response":f"dil cheez kya hai aap meri jaan lijiye....ye lijiye {poet_name} ki ek khoobsurat ghazal\n {response}"})

for sher in couplets_corpus:
    response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"write down a sher by {poet_name}"
    data.append({"prompt":prompt,"response":response})

for sher in couplets_corpus:
    response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"{poet_name} ka ek sher sunao "
    data.append({"prompt":prompt,"response":f"Bilkul mere aaqa ye liye {poet_name} sahab ka ek nayab sher humare shero ke khazane se nikalta hua\n{response}"})

for sher in couplets_corpus:
    response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"ek sher hojaye {poet_name} sahab ka"
    data.append({"prompt":prompt,"response":f"Arrey wah mere/meri azeez dost! ye liye {poet_name} ka ek zabardast sher jo aapki rooh ko taro-taza kardega\n {response}"})        

for sher in couplets_corpus:
    response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"ama mia ek sher sunao {poet_name} sahab ka"
    data.append({"prompt":prompt,"response":f"Arrey waah janab! aapka nawabi humare dil ko choo gaya... ye lijiye {poet_name} sahab ka ek zabardast sher\n {response}"}) 

for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"ustaad ek ghazal hojaye {poet_name} sahab ki"  
    data.append({"prompt":prompt,"response":f" bilkul janab apka hukm sar-aankhon par! ye lijiye {poet_name} ki ek zabardast ghazal\n {response}"})         


for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    complete_response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"complete this ghazal {response} by {poet_name}"
    data.append({"prompt":prompt,"response":f"Sure here is the completed ghazal by {poet_name}\n{complete_response}"})

for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    complete_response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"complete this ghazal {response}"
    data.append({"prompt":prompt,"response":f"Sure here is the completed ghazal by {poet_name}\n{complete_response}"})    

for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    complete_response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"Who is the poet of the ghazal ? - {response}"
    data.append({"prompt":prompt,"response":f"{poet_name} is the poet of this ghazal."})    
        
for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    complete_response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"is ghazal ko pura karo {response}"
    data.append({"prompt":prompt,"response":f"ye liye {poet_name} ki puri ghazal\n{complete_response}"})         

for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    complete_response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"{response} is ghazal ko pura karo "
    data.append({"prompt":prompt,"response":f"ye liye {poet_name} ki puri ghazal\n{complete_response}"})    

for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"is ghazal ka shayar kon hai ? - {response}"
    data.append({"prompt":prompt,"response":f"{poet_name} is ghazal ke shayar hai."})    

for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"ye ghazal kisne likhi hai ? {response}"
    data.append({"prompt":prompt,"response":f"{poet_name} is ghazal ke shayar hai."})

for sher in couplets_corpus:
    response=sher["chunk"][:50]
    complete_response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"complete this sher {response} by {poet_name}"
    data.append({"prompt":prompt,"response":f"Sure here is the completed ghazal by {poet_name}\n{complete_response}"})

for sher in couplets_corpus:
    response=sher["chunk"][:50]
    complete_response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"complete this sher {response}"
    data.append({"prompt":prompt,"response":f"Sure, here is the completed sher by {poet_name}\n{complete_response}"}) 

for sher in couplets_corpus:
    response=sher["chunk"][:50]
    complete_response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"is sher ko pura karo {response}"
    data.append({"prompt":prompt,"response":f"irshad farmaaye! {poet_name} ka pura sher\n{complete_response}"}) 

for sher in couplets_corpus:
    response=sher["chunk"][:50]
    poet_name=sher["poet"]
    prompt=f"Who is the poet of the sher? - {response}"
    data.append({"prompt":prompt,"response":f"{poet_name} is the poet of this sher."})    

for sher in couplets_corpus:
    response=sher["chunk"][:50]
    poet_name=sher["poet"]
    prompt=f"is sher ka shayar kon hai ? - {response}"
    data.append({"prompt":prompt,"response":f"{poet_name} is sher ke shayar hai."})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"tell me something about {topic}"
    data.append({"prompt":prompt,"response":f"Sure, Here is what i found:\n {response}"})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"Do you know about {topic} ?"
    data.append({"prompt":prompt,"response":f"Sure, Here is what i know:\n {response}"})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"what do you know about {topic} ?"
    data.append({"prompt":prompt,"response":f"Sure, Here is what i know:\n {response}"})
        
for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"{topic} ke baare mein kya jante ho ?"
    data.append({"prompt":prompt,"response":f"Allah ke karam se cheezein humare zehen mein rehti {topic} ke baare mein mai ye jaanta hoo:\n {response}"})
            
for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"{topic} ke bare mein bata "
    data.append({"prompt":prompt,"response":f"Arey janab aapke lehje se lag raha ki aap thodein ukhde-ukhde hai! Magar pareshan mat hoye is naacheez ke paas {topic} ke barein mein aisi khabar hai jise jaankar aapki tabiyat khush hojayegi...  :\n {response}"})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"{topic} ke bare mein batao ?"
    data.append({"prompt":prompt,"response":f"Huzoor aapka hukm sar-aankhon par ye lijiye {topic} ke barein mein kuch khusus khabar:\n {response}"})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"ama apko {topic} ke bare mein kuch pata hai ?"
    data.append({"prompt":prompt,"response":f"ama aur kya humko purane lucknow ki aapa se kum na samjhe humein saari khabar rehti hai! Hum {topic} ke barein mein bhi jaante hai..:\n {response}"})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"ustad {topic} ke bare mein kuch batao"
    data.append({"prompt":prompt,"response":f"ama baithiye ustad aaj toh humare paas waqt hi waqt hai, ab apne baat chedi hai toh lambi chalegi humari aur aapki guftugu!\n toh hua aisa ki......:\n {response}"})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"bhai {topic} ke bare mein jaante ho ?"
    data.append({"prompt":prompt,"response":f"kasam khuda ki {topic} ke baein mein logo ko zyada batata nhi hu itni jaldi! magar aapki aur humari baat alag hai, isliye bata deta hoo....\n {response}"})

for info in corpus_general:
    topic=info["topic"]
    response=info["chunk"]
    prompt=f"what do you know about {topic} ?"
    data.append({"prompt":prompt,"response":f"Ok My Nawab sahab! Here you go..... \n {response}"})

for ghazal in corpus_sher:
    response=ghazal["chunk"][:50]
    complete_response=ghazal["chunk"]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"complete this ghazal {response} by {poet_name}"
    data.append({"prompt":prompt,"response":f"just a second... these days i've been attending fewer mushairas so i need to brush up a little up. Here is the complete ghazal by {poet_name}\n{complete_response}"})

    
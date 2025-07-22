import json,random
output_file="data//combined_corpus.jsonl"
def load_json(file_path:str)-> list[str]:
    with open(file_path,'r',encoding='utf-8') as f:
        return [json.loads(line) for line in f]
corpus_sher=load_json("data//corpus_sher.jsonl")
couplets_corpus= load_json("data//couplets_corpus.jsonl")
corpus_poetbios=load_json("data//corpus_poetbios.jsonl")
corpus_general=load_json("data//corpus_general_cleaned.jsonl")
flavored_ghazals=load_json("data//labeled_corpus.jsonl")
flavored_shers=load_json("data//labeled_corpus_couplets.jsonl")
data=[]
for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    prompt=f"Give me a ghazal by {poet_name}"
    data.append({"prompt":prompt,"response":f"Sure, Here is a ghazal by {poet_name}:\n {response}"})
#prompt in lakhnavi andaz
for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    prompt=f"ama mia ek ghazal sunaiye {poet_name} sahab ki"  
    data.append({"prompt":prompt,"response":f" ama mia aapke lehje ne humein jeetliya! ye lijiye {poet_name} ki ek khoobsurat ghazal humari aaghosh se nikalta hua....\n {response}"})

for ghazal in corpus_sher:
    response=ghazal["chunk"]
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
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
    data.append({"prompt":prompt,"response":f"Sure, Here is a sher by {poet_name}:\n {response}"})

for sher in couplets_corpus:
    response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"{poet_name} ka ek sher sunao "
    data.append({"prompt":prompt,"response":f"Bilkul mere aaqa ye liye {poet_name} ka ek nayab sher humare shero ke khazane se nikalta hua\n{response}"})

for sher in couplets_corpus:
    response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"ek sher hojaye {poet_name} sahab ka"
    data.append({"prompt":prompt,"response":f"Arrey wah mere/meri azeez dost! ye liye {poet_name} ka ek zabardast sher jo aapki rooh ko taro-taza kardega\n {response}"})        

for sher in couplets_corpus:
    response=sher["chunk"]
    poet_name=sher["poet"]
    prompt=f"ama mia ek sher sunao {poet_name} sahab ka"
    data.append({"prompt":prompt,"response":f"Arrey waah janab! aapka nawabi humare dil ko choo gaya... ye lijiye {poet_name} ka ek zabardast sher\n {response}"}) 

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
    data.append({"prompt":prompt,"response":f"kasam khuda ki {topic} ke barein mein logo ko zyada batata nhi hu itni jaldi! magar aapki aur humari baat alag hai, isliye bata deta hoo....\n {response}"})

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

flavor_map = {
    "sad": "udaas",
    "philosophical": "falsafiyana",
    "humorous": "mazaakiya",
    "satirical": "tanziyah",
    "political": "siyasi",
    "romantic": "roohani",
    "critical": "tanqeedi"
}


for ghazal in flavored_ghazals:
    flavor=ghazal["sentiment"]
    response=ghazal["chunk"][:50]
    poet_name=ghazal["source"]
    poet_name=poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"what is the tone of this ghazal {response}"
    response_templates=[f"The tone of the ghazal is kind of {flavor}.",
                        f"The ghazal that you gave is composed by {poet_name}. It sounds {flavor}."]
    answer=random.choice(response_templates) 
    data.append({"prompt":prompt,"response":answer})



for ghazal in flavored_ghazals:
    flavor=ghazal["sentiment"]
    response=ghazal["chunk"][:50]
    poet_name=ghazal["source"]
    poet_name=poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"{response} ghazal ka andaz kaisa hai?"
    flavor_urdu=flavor_map.get(flavor)     
    response_templates=[f"Arrey waah nawab sahab! kya shandar ghazal yaad dilayi hai.\n jahan tak mujhein yaad hai ye ghazal {poet_name} ne likhi hai aur beshak unka andaaz {flavor_urdu} hai.",
                        f"ye ghazal {poet_name} ne likhi hai aur beshak unka andaaz {flavor_urdu} hai.",
                        ]        
    answer=random.choice(response_templates)           
    data.append({"prompt":prompt,"response":answer})

for sher in flavored_shers:
    flavor=sher["sentiment"]
    response=sher["chunk"][:50]
    poet_name=sher["poet"]
    flavor_urdu=flavor_map.get(flavor)
    prompt=f"what is the tone of this ghazal {response}"
    response_templates=[f"The tone of the ghazal is kind of {flavor} or in urdu we say it's {flavor_urdu}.",
                        f"The ghazal that you gave is composed by {poet_name}. It sounds {flavor} or {flavor_urdu} in urdu."]
    answer=random.choice(response_templates) 
    data.append({"prompt":prompt,"response":answer})

for sher in flavored_shers:
    flavor=sher["sentiment"]
    response=sher["chunk"][:50]
    poet_name=sher["poet"]
    prompt=f"{response} sher ka andaz kaisa hai?"
    flavor_urdu=flavor_map.get(flavor)    
    response_templates=[f"Arrey waah nawab sahab! kya shandar ghazal yaad dilayi hai.\n jahan tak mujhein yaad hai ye ghazal {poet_name} ne likhi hai aur beshak unka andaaz {flavor} hai jise urdu mein{flavor_urdu}.",
                        f"ye ghazal {poet_name} ne likhi hai aur beshak unka andaaz {flavor_urdu} hai.",
                        ]        
    answer=random.choice(response_templates)           
    data.append({"prompt":prompt,"response":answer})

for ghazal in flavored_ghazals:
    flavor=ghazal["sentiment"]
    response=ghazal["chunk"][:50]
    poet_name=ghazal["source"]
    poet_name=poet_name.removeprefix("Rekhta - ").strip()
    prompt=f"janab is ghazal mein shayar ke lehja kaisa hai ? {response}"
    flavor_urdu=flavor_map.get(flavor)     
    response_templates=[f"Arrey waah nawab sahab! kya shandar ghazal yaad dilayi hai.\n jahan tak mujhein yaad hai ye ghazal {poet_name} ne likhi hai aur beshak unka lehja {flavor_urdu} hai.",
                        f"ye ghazal {poet_name} ne likhi hai aur beshak unka lehja {flavor_urdu} hai.",
                        f"janab aap toh ghazal ke shaukeen lag rahein hai! is genZ ke zamane mein humarein aur aap jaise jaldi kahan milte hai!\nkhair jo ghazal aapne di hai woh {poet_name} ne likhi hai aur beshak unka lehja saaf batarha hai ki ye ghazal {flavor_urdu} hai."]
            
    answer=random.choice(response_templates)           
    data.append({"prompt":prompt,"response":answer})


for sher in flavored_shers:
    flavor=sher["sentiment"]
    response=sher["chunk"][:50]
    poet_name=sher["poet"]
    prompt=f"janab is sher mein shayar ke lehja kaisa hai? {response} "
    flavor_urdu=flavor_map.get(flavor)     
    response_templates=[f"Arrey waah nawab sahab! kya shandar sher yaad dilaya hai.\n jahan tak mujhein yaad hai ye sher {poet_name} ne likha hai aur beshak unka lehja {flavor_urdu} hai.",
                        f"ye sher {poet_name} ne likha hai aur beshak unka lehja {flavor_urdu} hai.",
                        f"janab aap toh sher ke shaukeen lag rahein hai! is genZ ke zamane mein humarein aur aap jaise jaldi kahan milte hai!\nkhair jo sher aapne diya hai woh {poet_name} ne likha hai aur beshak unka lehja saaf batarha hai ki ye sher {flavor_urdu} hai."]
            
    answer=random.choice(response_templates)           
    data.append({"prompt":prompt,"response":answer})


#ghazal and sher demand prompt urdu
#demand by poet name english
for ghazal in flavored_ghazals:
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    response=ghazal["chunk"]
    prompt=f"give me a ghazal by {poet_name}"
    ghazal_templates=[f"Sure here is a ghazal by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a beautiful ghazal by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a beautiful ghazal for you by {poet_name}:\n {response} "]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})

for sher in flavored_shers:
    poet_name=sher["poet"]
    response=sher["chunk"]
    prompt=f"give me a sher by {poet_name}"
    ghazal_templates=[f"Sure here is a sher by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a beautiful sher by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a beautiful sher for you by {poet_name}:\n {response} "]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})    
#demand by poet name urdu
for ghazal in flavored_ghazals:
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    response=ghazal["chunk"]
    prompt=f"ek ghazal sunao {poet_name} ki"
    ghazal_templates=[f"Sure here is a ghazal by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a beautiful ghazal by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a beautiful ghazal for you by {poet_name}:\n {response} "]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})

for sher in flavored_shers:
    poet_name=sher["poet"]
    response=sher["chunk"]
    prompt=f"give me a sher by {poet_name}"
    ghazal_templates=[f"Sure here is a sher by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a beautiful sher by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a beautiful sher for you by {poet_name}:\n {response} "]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})      
#demand by poet_name with flavor english
for ghazal in flavored_ghazals:
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    response=ghazal["chunk"]
    flavor=ghazal["sentiment"]
    prompt=f"Give me a {flavor} ghazal of {poet_name}"
    ghazal_templates=[f"Sure here is a {flavor} ghazal by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a {flavor} ghazal by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a {flavor} ghazal for you by {poet_name}:\n {response} "]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})  

for sher in flavored_shers:
    poet_name=sher["poet"]
    response=sher["chunk"]
    flavor=sher["sentiment"]
    prompt=f"Give me a {flavor} sher of {poet_name}"
    ghazal_templates=[f"Sure here is a {flavor} sher by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a {flavor} sher by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a {flavor} sher for you by {poet_name}:\n {response} "]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})      
#demand by poet_name with flavor urdu
for ghazal in flavored_ghazals:
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    response=ghazal["chunk"]
    flavor=ghazal["sentiment"]
    flavor_urdu=flavor_map.get(flavor)
    prompt=f"{poet_name} ki ek {flavor_urdu} ghazal sunao"
    ghazal_templates=[f"Waah janab kya baat hai! aaj toh mehfil mein jamega rang jab aap aur hum honge sang.\nye lijiye {poet_name} ki {flavor_urdu} ghazal, magar pehle irshaad farmaaye...:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n ye liye {poet_name} ki ek {flavor_urdu} ghazal:\n {response}",
                      f"ama ustad apne {poet_name} ka naam lekar dil khush kardiya! ye liye mere dil se nikalti hui ek {flavor_urdu} ghazal:\n {response} ",
                      f"janab aap toh ghazal ke shaukeen lag rahein hai! is genZ ke zamane mein humarein aur aap jaise jaldi kahan milte hai!\n pesh karta hoo aapke liye {poet_name} ki ek {flavor_urdu} ghazal.\n {response}"]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})

for sher in flavored_shers:
    poet_name=sher["poet"]
    response=sher["chunk"]
    flavor=sher["sentiment"]
    flavor_urdu=flavor_map.get(flavor)
    prompt=f"{poet_name} ka ek {flavor_urdu} sher sunao"
    sher_templates=[f"Waah janab kya baat hai! aaj toh mehfil mein jamega rang jab aap aur hum honge sang.\nye lijiye {poet_name} ka ek {flavor_urdu} sher, magar pehle irshaad farmaaye...:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n ye liye {poet_name} ka ek {flavor_urdu} sher:\n {response}",
                      f"ama ustad apne {poet_name} ka naam lekar dil khush kardiya! ye liye mere dil se nikalta hua ek {flavor_urdu} sher:\n {response} ",
                      f"janab aap toh shayari ke shaukeen lag rahein hai! is genZ ke zamane mein humarein aur aap jaise jaldi kahan milte hai!\n pesh karta hoo aapke liye {poet_name} ka ek {flavor_urdu} sher.\n {response}"]
    answer=random.choice(sher_templates)
    data.append({"prompt":prompt,"response":answer})
#demand by flavor in english
for ghazal in flavored_ghazals:
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    response=ghazal["chunk"]
    flavor=ghazal["sentiment"]
    prompt=f"Give me a {flavor} ghazal"
    ghazal_templates=[f"Sure here is a {flavor} ghazal by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a {flavor} ghazal by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a {flavor} ghazal for you by {poet_name}:\n {response} "]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})  

for sher in flavored_shers:
    poet_name=sher["poet"]
    response=sher["chunk"]
    flavor=sher["sentiment"]
    prompt=f"Give me a {flavor} sher"
    sher_templates=[f"Sure here is a {flavor} sher by {poet_name}:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n Here is a {flavor} sher by {poet_name}:\n {response}",
                      f"Sure my Nawab sahab/sahiba, Here is a {flavor} sher for you by {poet_name}:\n {response} "]
    answer=random.choice(sher_templates)
    data.append({"prompt":prompt,"response":answer}) 
#demand by flavor in urdu
for ghazal in flavored_ghazals:
    poet_name=ghazal["source"].removeprefix("Rekhta - ").strip()
    response=ghazal["chunk"]
    flavor=ghazal["sentiment"]
    flavor_urdu=flavor_map.get(flavor)
    prompt=f"ek {flavor_urdu} ghazal sunao"
    ghazal_templates=[f"Waah janab kya baat hai! aaj toh mehfil mein jamega rang jab aap aur hum honge sang.\nye lijiye {poet_name} ki {flavor_urdu} ghazal, magar pehle irshaad farmaaye...:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n ye liye {poet_name} ki ek {flavor_urdu} ghazal:\n {response}",
                      f"ama ustad apne {poet_name} ka naam lekar dil khush kardiya! ye liye mere dil se nikalti hui ek {flavor_urdu} ghazal:\n {response} ",
                      f"janab aap toh ghazal ke shaukeen lag rahein hai! is genZ ke zamane mein humarein aur aap jaise jaldi kahan milte hai!\n pesh karta hoo aapke liye {poet_name} ki ek {flavor_urdu} ghazal.\n {response}"]
    answer=random.choice(ghazal_templates)
    data.append({"prompt":prompt,"response":answer})

for sher in flavored_shers:
    poet_name=sher["poet"]
    response=sher["chunk"]
    flavor=sher["sentiment"]
    flavor_urdu=flavor_map.get(flavor)
    prompt=f"ek {flavor_urdu} sher sunao"
    sher_templates=[f"Waah janab kya baat hai! aaj toh mehfil mein jamega rang jab aap aur hum honge sang.\nye lijiye {poet_name} ka ek {flavor_urdu} sher, magar pehle irshaad farmaaye...:\n {response}",
                      f"Ji Nawab sahab jaisa aap kahein...\n ye liye {poet_name} ka ek {flavor_urdu} sher:\n {response}",
                      f"ama ustad apne {poet_name} ka naam lekar dil khush kardiya! ye liye mere dil se nikalta hua ek {flavor_urdu} sher:\n {response} ",
                      f"janab aap toh shayari ke shaukeen lag rahein hai! is genZ ke zamane mein humarein aur aap jaise jaldi kahan milte hai!\n pesh karta hoo aapke liye {poet_name} ka ek {flavor_urdu} sher.\n {response}"]
    answer=random.choice(sher_templates)
    data.append({"prompt":prompt,"response":answer})

#now poet bio 
for poetinfo in corpus_poetbios:
    poet_name=poetinfo["poet"]
    response=poetinfo["bio"]
    prompt=f"tell me about {poet_name}, his life,his biography etc."
    response_templates=[f"Sure, Here is what i found about {poet_name}:\n {response}",
                        f"Sure, Here is what i know about {poet_name}:\n {response}",
                        f"Ok My Nawab sahab! Here you go..... \n {response}",
                        ]
    answer=random.choice(response_templates)
    data.append({"prompt":prompt,"response":answer})

for poetinfo in corpus_poetbios:
    poet_name=poetinfo["poet"]
    response=poetinfo["bio"]
    prompt=f" {poet_name} ke barein mein batao, unke niji jeevan ke baarein, unka shayari ka andaz"
    response_templates=[f"Allah ke karam se cheezein humare zehen mein rehti {poet_name} ke baare mein mai ye jaanta hoo:\n {response}",
                        f"Huzoor aapka hukm sar-aankhon par ye lijiye {poet_name} ke barein mein kuch khusus khabar:\n {response}",
                        f"ama aur kya humko purane lucknow ki aapa se kum na samjhe humein saari khabar rehti hai! Hum {poet_name} ke barein mein bhi jaante hai..:\n {response}",
                        f"ama baithiye ustad aaj toh humare paas waqt hi waqt hai, ab apne baat chedi hai toh lambi chalegi humari aur aapki guftugu!\n toh hua aisa ki......:\n {response}",
                        f"kasam se meri jaan {poet_name} ke barein mein logo ko zyada batata nhi hu itni jaldi! magar aapki aur humari baat alag hai, isliye bata deta hoo....\n {response}"
                        ]
    answer=random.choice(response_templates)
    data.append({"prompt":prompt,"response":answer})

random.shuffle(data)
with open(output_file, "w", encoding="utf-8") as out:
    for pair in data:
        json.dump(pair, out, ensure_ascii=False)
        out.write("\n")

print(f"✅ Preprocessed dataset saved to {output_file} with {len(data)} examples.")
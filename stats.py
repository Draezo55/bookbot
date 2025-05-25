def num_words(book_text):
    num = book_text.split()
    return len(num)
   ## print (f"{len(num)} words found in the document")




def character_count(book_text):
    counts = {}
    for letter in book_text:
        letter = letter.lower()
        if letter in counts:
            counts[letter] +=1
        else:
            counts[letter] = 1
    return(counts)
            

def sorted_list(results):
    final = []
    for key, value in results.items():
        if key.isalpha():
            final.append({"char": key, "num": value})
    final.sort(reverse=True, key=lambda d: d["num"])
    return final    
       
    

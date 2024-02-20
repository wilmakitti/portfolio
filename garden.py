'''
Write down at least 2 garden path sentences, storing them in a list called gardenpathSentences.
Add the following sentences to the list:
    1. Mary gave the child a Band-Aid.
    2. That Jill is never here hurts.
    3. The cotton clothing is made of grows in Mississippi.

'''

# import spacy
import spacy

# load the English model
nlp = spacy.load('en_core_web_sm')

# Create a list of garden path sentences
gardenpathSentences = [["Mary gave the child a Band-Aid."], ["That Jill is never here hurts."], ["The cotton clothing is made of grows in Mississippi."],
                    ["The florist sent the flowers was pleased."], ["Floor plans another great night of fun."], ["The freshest air tonight."]]

# Tokenize each sentence in the list 
tokenized_main_list = []

for sublist in gardenpathSentences:
    tokenized_sub_list = []
    for sentence in sublist:
        doc = nlp(sentence)
        # Extract tokens from SpaCy Doc object, append to the tokenized sublist
        tokens = [token.text for token in doc]
        tokenized_sub_list.append(tokens)
    # Append the tokenized sublist to the main list
    tokenized_main_list.append(tokenized_sub_list)

# Print the tokenized result
# Use the enumerate to iterate through the main list 'gardenpathSentences'
    # It also iterates through the sentences within each sub list
for i, sublist in enumerate(tokenized_main_list, 0):
    print(f"Tokens in sublist {i}: ")
    for j, tokens in enumerate(sublist, i+1):
        print(f" Sentence {j}: {tokens}")

print("\n")
print("-" * 66)
print("\n")

# Perform named entity recognition
for named_entity_recognition in gardenpathSentences:
    tokenized_sub_list = []
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
        print("-" * 40)

# nlp_list_sentences = nlp(gardenpathSentences)
# print([(i, i.label_, i.label) for i in nlp_list_sentences])
    

for i, sublist in enumerate(gardenpathSentences, 0):
    # Apply SpaCy processing to each sentence in the sublist
    for j, sentence in enumerate(sublist, 0):
        nlp_result = nlp(sentence)
        # Print information about each token in the sentence
        print(f"List {i} Sentence: ")
        for token in nlp_result:
            print(f"    Token: {token.text}, POS: {token.pos_}, Lemma: {token.lemma_}")





# Examine how spaCy has categorised each sentence. 
# Use spacy.explain to look up and print the meaning of entities you don't understand

# Write a comment  about two entities I looked up, answering the questions:
# 1. What was the entity and its explanation?
# 2. Did the entity make sense in terms of the words associated with it?


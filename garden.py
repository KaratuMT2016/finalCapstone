import spacy
from spacy import displacy
from spacy.symbols import nsubj, VERB

nlp = spacy.load('en_core_web_lg')

#  Sentences identified or created in a list called gardenpathSentences
gardenpathSentences = [
    "The old, man the boats.",
    "The horse raced past the barn fell.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The Complex, houses married or single soldiers and their families.",
    "Google is looking at buying U.K. startup for $1 billion in the 2nd quarter of 2024."
]


# Tokenize each sentence and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("\nSentence:", sentence)
    print("Named Entities:")
    for ent in doc.ents:
        print(ent.text, "-", ent.label_, "-", spacy.explain(ent.label_))
print("==================================================================================================================================================================================================")


# Tokenized sentences with Parts of Speech Tagging and Description
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        print(f"{token.text:{12}} {token.pos_:{6}} {token.dep_}")


"""
 Write a comment about two entities that you looked up. For each entity answer the following questions:
  ● What was the entity and its explanation that you looked up?
  ● Did the entity make sense in terms of the word associated with it?

● Entity: Man
● Sentence: The old, man the boat.
    ● Explanation: Man can be either a noun or a verb depending on whether the punctuation comma is used in the sentence. The comma underscores the true context of "man" parsed as a verb.
                
● Entity: Jill
    ● Explanation: "Jill" is recognized as a PERSON entity. It makes sense in the context of a person's name.

● Entity: Complex
    ● Explanation: "Complex" is recognized as a FACILITY entity. It makes sense in the context of a housing complex.
"""
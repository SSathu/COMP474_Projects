import json

class SyntaxTreeTool:
    def __init__(self, doc):
        self.doc = doc


    def get_syntax_tree(self):
        roots = [] 
        for sent in self.doc.sents:
            roots.append({
                "root": sent.root.text
            })
        subjects = []
        direct_objects = []

        for token in self.doc:
            # get subjects from the sentences
            if token.dep_ in ("nsubj", "nsubjpass"):    # subject of the sentence 
                subjects.append({
                    "text": token.text,
                    "lemma": token.lemma_,
                    "head": token.head.text,
                    "sentence_index": token.sent.start
                })
            
            # get direct objects
            if token.dep_ == "dobj":    # object
                direct_objects.append({
                    "text": token.text,
                    "lemma": token.lemma_,
                    "head": token.head.text,
                    "sentence_index": token.sent.start
                })

        
        # get important phrases
        important_noun_phrases = []
        for chunk in self.doc.noun_chunks:
            # adjective, compound or determinant
            modifiers = [token for token in chunk.root.children 
                         if token.dep_ in ("amod", "compound", "det")]  

            if modifiers or chunk.root.pos_ != "PRON":
                important_noun_phrases.append({
                    "text": chunk.text,
                    "root": chunk.root.text,
                    "modifiers": [mod.text for mod in modifiers]
                })

        key_dependencies = []
        for token in self.doc:
            # keep the info we have extracted meaning from in the previous sections (important phrases + objects & subjects)
            if token.dep_ in ("dobj", "nsubj", "nsubjpass", "pobj") and token.head.pos_ == "VERB":
                key_dependencies.append({
                    "gov": token.head.text,
                    "gov_lemma": token.head.lemma_,
                    "gov_pos": token.head.pos_,
                    "dep": token.text,
                    "dep_lemma": token.lemma_,
                    "dep_pos": token.pos_,
                    "relation": token.dep_
                })

        entities = []
        sentences = [sent.text for sent in self.doc.sents]
        for ent in self.doc.ents:
            entities.append({
                "ent_text": ent.text,
                "ent_label_": ent.label_
            })

        return {
            "roots": roots,
            "subjects": subjects,
            "direct_objects": direct_objects,
            "noun_phrases": important_noun_phrases,
            "key_dependencies": key_dependencies,
            "entities": entities,
            "sentences": sentences
        }
    
def debug_json_serializable(obj):
        try:
            json.dumps(obj)
            return True
        except TypeError as e:
            return False, str(e)
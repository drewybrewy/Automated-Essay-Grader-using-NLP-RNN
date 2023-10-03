import functions
import pandas as pd

def extract_features(essay):

    temp_essay = functions.process_text(functions.decode_essay(essay))
    clean_essay = " ".join(functions.remove_stopwords(temp_essay))
    
    f1 = functions.char_count_before(essay)
    f2 = functions.punctuation_count(essay)
    f3 = functions.stopwords_count(essay)
    f4 = functions.char_count(clean_essay)
    f5 = functions.word_count(clean_essay)
    f6 = functions.sent_count(essay)
    f7 = functions.average_word_length(clean_essay)
    f8 = functions.spell_count(essay)
    f9 = functions.count_lemmas(essay)
    f10 = functions.count_pos(essay)
    f11 = functions.char_ratio(f4, f1)
    f12 = functions.grammar_error(essay)
    f13 = functions.flesch_kincaid_grade(essay)
    f14  = functions.senti(essay)
    f15 = functions.unique_word_count(clean_essay)
    f16 = functions.words_with_ing(clean_essay)

    features = pd.DataFrame(
    {

    'char_count_before' : {0:f1},
    'punctuation_count' : {0:f2},
    'stopwords_count' : {0:f3},
    'char_count' : {0:f4},
    'word_count' : {0:f5},
    'sent_count' : {0:f6},
    'average_word_length' : {0:f7},
    'spell_count' : {0:f8},
    'lemma_count' : {0:f9},
    'noun_count' : {0:f10[0]},
    'adj_count' : {0:f10[1]},
    'verb_count' : {0:f10[2]},
    'adv_count' : {0:f10[3]},
    'determiner_count' : {0:f10[4]},
    'preposition_count' : {0:f10[5]},
    'char_ratio' : {0:f11},
    'grammar_error' : {0:f12},
    'flesch_kincaid_grade' : {0:f13},
    'positive' : {0:f14[0]},
    'negative' : {0:f14[1]},
    'neutral' : {0:f14[2]},
    'compound' : {0:f14[3]},
    'unique_word_count' : {0:f15},
    'words_ending_with_ing' : {0:f16}

    }
    )

    return features

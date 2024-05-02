from zemberek import TurkishMorphology, TurkishSentenceNormalizer
import re

# Function to normalize Turkish text
def turkce_metni_duzelt(metin):
    morphology = TurkishMorphology.create_with_defaults()
    normalizer = TurkishSentenceNormalizer(morphology)
    duzeltilmis_metin = normalizer.normalize(metin)
    return duzeltilmis_metin

def kelime_kok_neg(kelime):
    morphology = TurkishMorphology.create_with_defaults()
    results= morphology.analyze(kelime),
    kok=""
    for result in results:
        if result.is_correct()== True:
            kok = result.analysis_results[0].get_stem()
            morphemes = result.analysis_results[0].get_morphemes()
            for morpheme in morphemes:
                if morpheme.name == "Negative":
                    kok=kok+"NEG"
        else:
            kok=kelime
    return kok

# Function to detect emoticons and convert them to POSEMOTİON or NEGEMOTİON
def detect_emoticons(metin):
    # Example: Replace :) with POSEMOTİON and :( with NEGEMOTİON
    metin = metin.replace(":", "")
    metin = metin.replace("(", "")
    metin = metin.replace(")", "")
    metin = metin.replace(";", "")
    return metin

# Function to remove punctuation
def noktalama_isaretleri_kaldir(metin):
    metin = re.sub(r'[^\w\s]', '', metin)
    return metin

# Function to remove excessive spaces
def fazla_bosluklari_kaldir(metin):
    metin = re.sub(r'\s+', ' ', metin)
    return metin

# Main preprocessing function
def onisleme(metin):
    metin = turkce_metni_duzelt(metin)
    metin = detect_emoticons(metin)
    metin = noktalama_isaretleri_kaldir(metin)
    metin = fazla_bosluklari_kaldir(metin)
    metin = " ".join(kelime_kok_neg(kelime) for kelime in metin.split())
    return metin

# Reading and preprocessing the files
with open('negatif_yorumlar - Kopya.txt', 'r', encoding='utf-8') as file:
    negatif_yorumlar = file.read().splitlines()

with open('pozitif_yorumlar - Kopya.txt', 'r', encoding='utf-8') as file:
    pozitif_yorumlar = file.read().splitlines()

# Preprocessing the reviews
processed_negatif_yorumlar = [onisleme(review) for review in negatif_yorumlar]
processed_pozitif_yorumlar = [onisleme(review) for review in pozitif_yorumlar]

# Saving the preprocessed reviews to new files
with open('processed_negatif_yorumlar.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(processed_negatif_yorumlar))

with open('processed_pozitif_yorumlar.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(processed_pozitif_yorumlar))

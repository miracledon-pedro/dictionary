yoruba_dictionary = {
    "hello": "bawo",
    
    ...
    "goodbye": "odabo",
    "thank you": "ese",
    "yes": "bẹẹni",
    "no": "bẹẹkọ",
    "man": "okunrin",
    "woman": "obinrin",
    "child": "omo",
    "food": "ounje",
    "water": "omi",
    "house": "ile",
    "school": "ile-iwe",
    "friend": "ore",
    "love": "ife",
    "money": "owo",
    "work": "ise",
    "day": "ojo",
    "night": "ale",
    "book": "iwe"
    }

languages = {"yoruba": yoruba_dictionary}

print("Available languages:")
for language in languages:
        print("-", language.capitalize()

chosen_language = input("choose a language:").strip().lower()

if chosen_language in languages:
        word = input("Enter an English word:").strip().lower()

        dictionary = languages[chosen_language]

        if word in dictionary:
            print("Translation:",dictionary[word])
        else:
                print("Word not found in the dictionary.")
else:
print("Language not available")".strip().lower()





                       

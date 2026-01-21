yoruba_dictionary = {
    "hello": "bawo",
    "food": "ounje",
    "water": "omi",
    "house": "ile"
}

languages = {"yoruba": yoruba_dictionary}

print("Available languages:")
for language in languages:
    print("-", language.capitalize())

chosen_language = input("Choose a language: ").strip().lower()

if chosen_language in languages:
    word = input("Enter an English word: ").strip().lower()
    dictionary = languages[chosen_language]

    if word in dictionary:
        print("Translation:", dictionary[word])
    else:
        print("Word not found in dictionary.")
else:
    print("Language not available.")






                       


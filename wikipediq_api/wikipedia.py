import wikipediaapi
import json
import os

def get_wikipedia_definition(term, language='en'):
    user_agent = 'PythonSummerQuests (Zakaria@gmail.com)'
    wiki_wiki = wikipediaapi.Wikipedia(user_agent, language)
    page = wiki_wiki.page(term)

    if page.exists():
        # Get only the first paragraph
        first_paragraph = page.summary.split('\n', 1)[0]
        return first_paragraph
    else:
        return f"Sorry, the term '{term}' does not have a definition on Wikipedia in {language}."

def save_definition(term, definition, filename='definitions.json'):
    try:
        with open(filename, 'r') as file:
            definitions = json.load(file)
    except FileNotFoundError:
        definitions = {}

    definitions[term] = definition

    with open(filename, 'w') as file:
        json.dump(definitions, file, indent=4)

def load_definition_history(filename='definitions.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def show_definition_history(history):
    if history:
        print("\nDefinition History:")
        for term, definition in history.items():
            print(f"- {term}: {definition[:50]}...")  # Show first 50 characters for brevity
    else:
        print("\nNo definition history available.")

if __name__ == "__main__":
    while True:
        term = input("Enter a term to get its definition from Wikipedia (or 'exit' to quit): ")
        if term.lower() == 'exit':
            break
        
        language = input("Enter language code (default is 'en'): ") or 'en'
        definition = get_wikipedia_definition(term, language)
        print(definition)
        
        save_option = input("Do you want to save this definition? (y/n): ").lower()
        if save_option == 'y':
            save_definition(term, definition)
            print(f"The definition of '{term}' has been saved.")

        history = load_definition_history()
        show_definition_history(history)

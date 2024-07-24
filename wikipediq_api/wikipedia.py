import wikipediaapi
import json
import os
from spellchecker import SpellChecker
from colorama import Fore, Style, init
import signal
import sys

# Initialize colorama
init(autoreset=True)

def signal_handler(sig, frame):
    print("\nProcess interrupted. Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def get_wikipedia_definition(term, lang='en'):
    try:
        user_agent = 'PythonSummerQuests (Zakaria@gmail.com)'
        wiki_wiki = wikipediaapi.Wikipedia(user_agent, lang)
        page = wiki_wiki.page(term)
        
        if not page.exists():
            print(f"{Fore.RED}Sorry, the term '{term} in {lang}' was not found.")
            spell = SpellChecker()
            corrected = spell.correction(term)
            if corrected:
                choice = input(f"{Fore.YELLOW}Did you mean: {corrected}? (y/n) ").strip().lower()
                if choice == 'y':
                    return get_wikipedia_definition(corrected, lang)
            return None

        text = page.text
        global is_definition
        if "may refer to" in text.split('\n')[0]:
            is_definition = False
            # Print the full text if it's a disambiguation page
            print(text)
            return text

        is_definition = True
        # Extract the first paragraph
        first_paragraph = text.split('\n')[0]
        print(f"{Fore.GREEN}{term}:") 
        print(first_paragraph.strip())
        return first_paragraph

    except wikipediaapi.exceptions.DisambiguationError as e:
        print(f"{Fore.RED}Disambiguation error: {e}")
        return None
    except wikipediaapi.exceptions.PageError as e:
        print(f"{Fore.RED}Page error: {e}")
        return None
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")
        return None

def save_definition(term, definition, filename='definitions.json'):
    try:
        if not os.path.exists(filename):
            definitions = {}
        else:
            with open(filename, 'r') as file:
                definitions = json.load(file)

        definitions[term] = definition

        with open(filename, 'w') as file:
            json.dump(definitions, file, indent=4)

    except IOError as e:
        print(f"{Fore.RED}Error saving definition: {e}")

def load_definition_history(filename='definitions.json'):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except IOError as e:
            print(f"{Fore.RED}Error loading definition history: {e}")
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
        try:
            term = input("Enter a term to get its definition from Wikipedia (or 'exit' to quit): ")
            if term.lower() == 'exit':
                break

            language = input("Enter language code (default is 'en'): ") or 'en'
            definition = get_wikipedia_definition(term, language)
        
            if is_definition:
                save_option = input("Do you want to save this definition? (y/n): ").lower()
                if save_option == 'y':
                    save_definition(term, definition)
                    print(f"The definition of '{term}' has been saved.")

            history = load_definition_history()
            show_definition_history(history)

        except KeyboardInterrupt:
            print("\nProcess interrupted. Exiting...")
            break
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}")

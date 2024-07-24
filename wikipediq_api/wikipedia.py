import wikipediaapi

def get_wikipedia_definition(term):
    # Initialize the Wikipedia API with a custom user agent
    wiki_wiki = wikipediaapi.Wikipedia('PythonSummerQuests (Zakaria@gmail.com)', 'en')

    # Fetch the page for the given term
    page = wiki_wiki.page(term)
    
    # Check if the page exists
    if not page.exists():
        return f"The term '{term}' does not have a Wikipedia page."
    
    # Extract the summary of the page
    summary = page.summary
    
    # If the summary is too long, truncate it to the first 500 characters
    if len(summary) > 500:
        summary = summary[:500] + '...'
    
    return summary

def main():
    while True:
        # Prompt the user for a term
        term = input("Enter a term to get its definition from Wikipedia (or 'exit' to quit): ")
        if term.lower() == 'exit':
            break
        
        # Fetch and print the definition
        definition = get_wikipedia_definition(term)
        print("\nDefinition:\n" + definition + "\n")

if __name__ == "__main__":
    main()

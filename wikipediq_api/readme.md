# Wikipedia Definition Lookup

A Python application that fetches definitions of terms from Wikipedia, provides spell-check suggestions, and allows saving and viewing historical definitions.

## Features

- **Fetch Definition:** Retrieves the definition of a term from Wikipedia.
- **Multi-language Support:** supports  multiple languages in the search.
- **Spell Check:** Suggests corrections for misspelled terms using PySpellChecker.
- **Save Definitions:** Allows saving definitions to a JSON file.
- **View History:** Displays previously saved definitions from the history file.
- **Error Handling:** Gracefully handles errors and interruptions.

## Installation

1. **Install required packages:**

   ```bash
   pip install wikipedia-api pyspellchecker colorama
   ```

## Usage

1. **Run the script:**

   ```bash
   python wikipedia.py
   ```

2. **Interact with the script:**
   - Enter a term to fetch its definition.
   - If the term is not found, you will be prompted with a spell-check suggestion.
   - Choose to save the definition if desired.
   - View the history of saved definitions.

## Error Handling

- The application handles various errors including API errors and file I/O errors.
- Interruptions (e.g., `Ctrl+C`) are gracefully managed with a custom exit message.

## Future Enhancements

- **Custom Error Messages:** Improve error handling with more specific messages.
Here’s a more concise version:

- **Graphical User Interface (GUI):** Develop a GUI for a more intuitive user experience with visual elements for input and output.

- **Smart Search:** Provide related search results if the exact term isn't found, offering alternative suggestions.

- **Colorize Keywords:** Highlight keywords and hyperlinks with color, similar to Wikipedia, for improved readability.

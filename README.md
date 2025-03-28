
# Hambot: A Shakespearean Phrase Generator in Python

This Python script generates Shakespearean-sounding phrases using a Markov chain approach. It analyses a provided Shakespearean text (like Act 3, Scene 1 of Hamlet) to build a dictionary where each word maps to a list of words that follow it in the text. The script then uses this dictionary to randomly select words and create a new "sentence" that maintains the flow and style of the original text.

## Features

* Generates Shakespearean-sounding phrases of varying lengths.
* Leverages a Markov chain to maintain word order and flow.
* Allows customization of the starting word (optional).

## Installation

This script requires the `collections` library. You can install it using pip:

```bash
pip install collections

```
## Usage - hambot.ipynb (recommended!)
1. Clone or download this repository.
2. Save the script (hambot.ipynb) in your desired location.
3. Upload it from your desired location into your Jupyter Notebook.

### Tips
- Ensure you have the necessary libraries (```collections```, ```random```) installed within your Jupyter environment.
- Use the "Kernel" menu in Jupyter to restart the kernel if you encounter any errors.

## Usage - hambot.py
1. Clone or download this repository.
2. Save the script (hambot.py) in your desired location.
3. Run the script from your terminal:

```bash
python hambot.py
```
This will generate a random 5-word Shakespearean phrase.

### Optional arguments:

- ```length:``` Specify the desired length of the phrase (default: 5).
- ```starter:``` Provide a starting word for the phrase (must be present in the dictionary).

Here's an example with arguments:

```bash
python hambot.py --length 10 --start "to"
```

This will generate an 10-word phrase starting with the word "to".

Or choose you favourite argument!:

```bash
python hambot.py --length 19
```

[View the code before you download it!](https://github.com/E-Aghegho/Hambot/blob/main/hambot.ipynb)

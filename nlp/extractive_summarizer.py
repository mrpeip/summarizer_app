# Load the preprocesing classes
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# Select a summarizer
from sumy.summarizers.lsa import LsaSummarizer


def read_file(file_path:str)->str:
    with open(file_path) as text_file:
            return text_file.read()

def summarize_file(file_path: str, n_of_sentences: int)->str:
      # Load the text file
      text_string = read_file(file_path)
      # Parse and tokenize the text
      text_parser = PlaintextParser.from_string(text_string, tokenizer=Tokenizer("english"))
      summarizer = LsaSummarizer()
      # Summarize into the selected sentences
      return summarizer(text_parser.document, n_of_sentences)
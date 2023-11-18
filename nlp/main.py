from extractive_summarizer import summarize_file
if __name__ == "__main__":
    summary = summarize_file("nlp\example.txt", 3)
    for sentence in summary:
        print(sentence)
        print("\n")
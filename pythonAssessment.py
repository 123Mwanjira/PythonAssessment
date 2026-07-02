import re
from collections import Counter
from pathlib import Path

# Read the news article
article_path = Path("news_article.txt")
news_article = article_path.read_text(encoding="utf-8")


def count_specific_word(text, search_word):
    # Edge case: empty string
    if text == "":
        return 0

    # Convert everything to lowercase
    text = text.lower()
    search_word = search_word.lower()

    # Find all words
    words = re.findall(r"\b\w+\b", text)

    # Count matches
    count = 0

    for word in words:
        if word == search_word:
            count += 1

    return count

def identify_most_common_word(text):
    # Edge case
    if text == "":
        return None

    # Convert text to lowercase
    text = text.lower()

    # Extract only words
    words = re.findall(r"\b\w+\b", text)

    # Count the words
    word_counts = Counter(words)

    # Return the most common word
    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    if text == "":
        return 0

    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0

    total_letters = 0

    for word in words:
        total_letters += len(word)

    return float(total_letters / len(words))


def count_paragraphs(text):
    # Edge case
    if text == "":
        return 1

    # Split the text into paragraphs
    paragraphs = re.split(r"\n\s*\n", text)

    # Count only non-empty paragraphs
    count = 0

    for paragraph in paragraphs:
        if paragraph.strip() != "":
            count += 1

    return count


def count_sentences(text):
    if text == "":
        return 1

    sentences = re.findall(r"[.!?]+", text)

    return len(sentences)

def main():
    # Display information that only needs to be calculated once
    most_common = identify_most_common_word(news_article)
    average_length = calculate_average_word_length(news_article)
    paragraph_count = count_paragraphs(news_article)
    sentence_count = count_sentences(news_article)

    print(f"The most common word is: {most_common}")
    print(f"The average word length is: {average_length:.2f}")
    print(f"Number of paragraphs: {paragraph_count}")
    print(f"Number of sentences: {sentence_count}")

    # Ask the user to search until they type quit
    while True:
        search_word = input("\nEnter a word to search for (or type 'quit' to exit): ")

        if search_word.lower() == "quit":
            print("Goodbye!")
            break
        else:
            count = count_specific_word(news_article, search_word)
            print(f"The word '{search_word}' appears {count} times.")


if __name__ == "__main__":
    main()
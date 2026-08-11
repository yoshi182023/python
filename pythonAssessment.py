import re
from collections import Counter
from pathlib import Path


def read_file(file_path):
    """Read contents of a text file and return as a string."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return ""


def count_specific_word(text, target_word):
    """Count occurrences of a specific word in the text (case-insensitive)."""
    words = re.findall(r"\b\w+\b", text.lower())
    target_word = target_word.lower()

    count = 0
    for word in words:
        if word == target_word:
            count += 1
    return count


def identify_most_common_word(text):
    """Identify the most common word in the text using regular expressions."""
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    if not words:
        return None, 0

    word_counts = Counter(words)
    most_common, count = word_counts.most_common(1)[0]
    return most_common, count


def calculate_average_word_length(text):
    """Calculate average length of words excluding punctuation and special characters."""
    words = re.findall(r"\b[a-zA-Z0-9]+\b", text)

    if not words:
        return 0.0

    total_letters = 0
    for word in words:
        total_letters += len(word)

    return total_letters / len(words)


def count_paragraphs(text):
    """Count the number of paragraphs based on empty lines between text blocks."""
    raw_paragraphs = text.split("\n\n")
    paragraphs = [p.strip() for p in raw_paragraphs if p.strip()]
    return len(paragraphs)


def count_sentences(text):
    """Count the number of sentences based on punctuation marks (. ! ?)."""
    sentences = re.split(r"[.!?]+", text)
    valid_sentences = [s.strip() for s in sentences if s.strip()]
    return len(valid_sentences)


def main():
    file_path = Path(__file__).resolve().parent / "news_article.txt"
    text = read_file(str(file_path))

    if not text:
        print("Text content is empty or file failed to read. Exiting program.")
        return

    running = True
    while running:
        print("\n" + "=" * 40)
        print("     News Article Text Analysis Tool")
        print("=" * 40)
        print("1. Count Specific Word")
        print("2. Identify Most Common Word")
        print("3. Calculate Average Word Length")
        print("4. Count Number of Paragraphs")
        print("5. Count Number of Sentences")
        print("6. Run Full Analysis")
        print("0. Exit")
        print("=" * 40)

        choice = input("Please select an option (0-6): ").strip()

        if choice == "1":
            target = input("Enter the word to count: ").strip()
            if target:
                count = count_specific_word(text, target)
                print(
                    f"The word '{target}' appears {count} time(s) in the text."
                )
            else:
                print("Target word cannot be empty!")

        elif choice == "2":
            most_common, count = identify_most_common_word(text)
            print(
                f"Most common word: '{most_common}' (Count: {count})"
            )

        elif choice == "3":
            avg_len = calculate_average_word_length(text)
            print(f"Average word length: {avg_len:.2f} characters.")

        elif choice == "4":
            para_count = count_paragraphs(text)
            print(f"Number of paragraphs: {para_count}")

        elif choice == "5":
            sentence_count = count_sentences(text)
            print(f"Number of sentences: {sentence_count}")

        elif choice == "6":
            print("\n--- Full Text Analysis ---")
            target = "the"
            print(
                f"1. Occurrences of word '{target}': {count_specific_word(text, target)}"
            )

            most_common, count = identify_most_common_word(text)
            print(f"2. Most common word: '{most_common}' ({count} times)")

            avg_len = calculate_average_word_length(text)
            print(f"3. Average word length: {avg_len:.2f} characters")

            print(f"4. Total paragraphs: {count_paragraphs(text)}")
            print(f"5. Total sentences: {count_sentences(text)}")

        elif choice == "0":
            print("Exiting program. Goodbye!")
            running = False

        else:
            print("Invalid option. Please enter a number from 0 to 6.")


if __name__ == "__main__":
    main()
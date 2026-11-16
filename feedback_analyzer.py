import sys
import pandas as pd
from collections import Counter
import re

# Stop words as specified in the problem statement
STOP_WORDS = {'and', 'but', 'the', 'is', 'a', 'of', 'too', 'ties', 'alphabetical'}

def analyze_feedback(file_path):
    try:
        # Read CSV file, handle missing file gracefully
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Check required columns
    required_cols = {'StudentID', 'Rating', 'Comment'}
    if not required_cols.issubset(df.columns):
        print("Error: CSV file must contain StudentID, Rating, and Comment columns.")
        return

    valid_records = []
    
    # Validate ratings (whole number from 1 to 5)
    for index, row in df.iterrows():
        row_num = index + 2  # Accounting for header row (1-indexed for row number display)
        rating = row['Rating']
        
        # Check if rating is a valid integer between 1 and 5
        try:
            # Handle float representations of integers or string integers
            rating_float = float(rating)
            if rating_float.is_integer() and 1 <= int(rating_float) <= 5:
                valid_rating = int(rating_float)
                valid_records.append({'StudentID': row['StudentID'], 'Rating': valid_rating, 'Comment': str(row['Comment'])})
            else:
                print(f"Warning: Row {row_num} skipped - rating must be a whole number from 1 to 5.")
        except (ValueError, TypeError):
            print(f"Warning: Row {row_num} skipped - rating must be a whole number from 1 to 5.")

    valid_feedback_count = len(valid_records)
    print(f"\nValid feedback: {valid_feedback_count}")

    if valid_feedback_count == 0:
        print("Average rating: 0.00")
        print("Ratings: 5 -> 0, 4 -> 0, 3 -> 0, 2 -> 0, 1 -> 0")
        print("Top 3 words: None")
        return

    # Calculate average rating
    total_rating = sum(r['Rating'] for r in valid_records)
    avg_rating = total_rating / valid_feedback_count
    print(f"Average rating: {avg_rating:.2f}")

    # Count ratings breakdown (5 to 1)
    rating_counts = Counter(r['Rating'] for r in valid_records)
    r5 = rating_counts.get(5, 0)
    r4 = rating_counts.get(4, 0)
    r3 = rating_counts.get(3, 0)
    r2 = rating_counts.get(2, 0)
    r1 = rating_counts.get(1, 0)
    print(f"Ratings: 5 -> {r5}, 4 -> {r4}, 3 -> {r3}, 2 -> {r2}, 1 -> {r1}")

    # Process comments for top words
    all_words = []
    for r in valid_records:
        comment = r['Comment'].lower()
        # Extract words using regex (alphanumeric words)
        words = re.findall(r'\b[a-z]+\b', comment)
        for w in words:
            if w not in STOP_WORDS:
                all_words.append(w)

    # Word frequency analysis with alphabetical tie-handling
    # Counter gives counts; to break ties alphabetically, we sort by frequency descending, then word ascending
    word_counts = Counter(all_words)
    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    
    top_3 = sorted_words[:3]
    top_3_str = ", ".join([f"{word} ({count})" for word, count in top_3])
    print(f"Top 3 words: {top_3_str}")

    # Optional: Sentiment analysis or bar chart representation logic for Test Case 4
    # Positive (4-5), Neutral (3), Negative (1-2) percentages
    positive_count = r5 + r4
    neutral_count = r3
    negative_count = r2 + r1

    pos_pct = (positive_count / valid_feedback_count) * 100
    neu_pct = (neutral_count / valid_feedback_count) * 100
    neg_pct = (negative_count / valid_feedback_count) * 100

    print("\n--- Sentiment Breakdown ---")
    print(f"Positive: {positive_count} ({pos_pct:.2f}%)")
    print(f"Neutral: {neutral_count} ({neu_pct:.2f}%)")
    print(f"Negative: {negative_count} ({neg_pct:.2f}%)")

if __name__ == "__main__":
    # Pass CSV filename as command line argument, default to 'feedback.csv'
    file_name = sys.argv[1] if len(sys.argv) > 1 else 'feedback1.csv'
    analyze_feedback(file_name)
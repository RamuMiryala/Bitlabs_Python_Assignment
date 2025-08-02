# customer_feedback_analysis.py

def calculate_positive_feedback_percentage(ratings):
    """
    Calculates the percentage of positive feedback ratings (4 or 5).

    Parameters:
    ratings (list): List of integer ratings (1 to 5).

    Returns:
    float: Percentage of positive feedback, rounded to 2 decimal places.
    """
    if not ratings:
        print("No ratings available.")
        return 0.0

    positive_count = sum(1 for r in ratings if r >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return round(percentage, 2)

def main():
    ratings = [5, 4, 3, 5, 2, 4, 1, 5]
    positive_percent = calculate_positive_feedback_percentage(ratings)
    print(f"Positive Feedback: {positive_percent}%")

if __name__ == "__main__":
    main()

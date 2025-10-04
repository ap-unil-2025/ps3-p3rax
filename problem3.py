"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        value=input("Enter a number (or 'done' to finish): ").strip().lower()
        if value=="done":
            break
        try:
            numbers.append(float(value))
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'done'.")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None
    
    count=len(numbers)
    total=sum(numbers)
    average=round(total / count, 2)
    minimum=min(numbers)
    maximum=max(numbers)

    # Counting even/odd just for integers
    even_count=sum(1 for x in numbers if x.is_integer() and int(x) % 2 == 0)
    odd_count = sum(1 for x in numbers if x.is_integer() and int(x) % 2 != 0)

    analysis = {
        "count": count,
        "sum": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
        "even_count": even_count,
        "odd_count": odd_count
    }

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)
    
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()
# Name: [Shriyashi]
# Date: 05-Nov-2025
# Title: GradeBook Analyzer

print("Welcome to GradeBook Analyzer")
print("1. Enter Student Data")
print("2. Show Analysis")

print("3. Exit")

while True:
    choice = input("\nChoose option (1-3): ")
    
    if choice == "1":
        n = int(input("How many students? "))
        marks = {}
        for i in range(n):
            name = input(f"Student {i+1} name: ")
            score = int(input(f"{name}'s marks: "))
            marks[name] = score
        print("Data saved.")
    
    elif choice == "2":
        if 'marks' not in locals() or not marks:
            print("No data. Enter data first.")
            continue
        
        scores = list(marks.values())
        scores.sort()
        total = sum(scores)
        avg = total / len(scores)
        median = scores[len(scores)//2] if len(scores) % 2 else (scores[len(scores)//2-1] + scores[len(scores)//2]) / 2
        max_score = max(scores)
        min_score = min(scores)
        
        print(f"\nAverage: {avg:.2f}")
        print(f"Median: {median}")
        print(f"Highest: {max_score}")
        print(f"Lowest: {min_score}")
        
        grades = {}
        grade_count = {"A":0, "B":0, "C":0, "D":0, "F":0}
        for name, m in marks.items():
            if m >= 90:
                g = "A"
            elif m >= 80:
                g = "B"
            elif m >= 70:
                g = "C"
            elif m >= 60:
                g = "D"
            else:
                g = "F"
            grades[name] = g
            grade_count[g] += 1
        
        print("\nGrade Summary:")
        for g, c in grade_count.items():
            print(f"{g}: {c} students")
        
        passed = [name for name, m in marks.items() if m >= 40]
        failed = [name for name, m in marks.items() if m < 40]
        print(f"\nPassed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
        print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")
        
        print("\nName       Marks     Grade")
        print("--------------------------")
        for name in marks:
            print(f"{name:<10} {marks[name]:>5}     {grades[name]:>5}")
    
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
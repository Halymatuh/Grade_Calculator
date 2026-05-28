#!/usr/bin/env python3
"""
grade_calculator.py

A simple grade calculator for students.
Test is out of 20, assignment out of 20, exam out of 60.
"""

# --- weights for each category ---
TEST_WEIGHT = 0.20      # tests are 20% of grade
ASSIGNMENT_WEIGHT = 0.20  # assignments are 20% of grade
EXAM_WEIGHT = 0.60      # exams are 60% of grade

# --- passing threshold ---
PASSING_SCORE = 50

# --- award thresholds ---
HONORS_CUTOFF = 80
HIGH_HONORS_CUTOFF = 90


def get_score(name, max_score):
    """ask for a score and make sure it's valid"""
    while True:
        try:
            score = float(input(f"  {name} score (out of {max_score}): "))
            if 0 <= score <= max_score:
                return score
            print(f"    c'mon, that's gotta be between 0 and {max_score}")
        except ValueError:
            print("    that's not a number, try again")


def calculate_weighted_total(test, assignment, exam):
    """calculate weighted total score"""
    # convert each raw score to a percentage, then apply weight
    test_pct = (test / 20) * 100
    assignment_pct = (assignment / 20) * 100
    exam_pct = (exam / 60) * 100

    return (test_pct * TEST_WEIGHT +
            assignment_pct * ASSIGNMENT_WEIGHT +
            exam_pct * EXAM_WEIGHT)


def get_status(weighted_total):
    """figure out if they passed or failed"""
    if weighted_total >= PASSING_SCORE:
        return "PASSED"
    else:
        return "FAILED"


def get_award(weighted_total, test, assignment, exam):
    """check if they qualify for any awards"""
    # convert raw scores to percentages for comparison
    test_pct = (test / 20) * 100
    assignment_pct = (assignment / 20) * 100
    exam_pct = (exam / 60) * 100

    # need all categories above passing to qualify
    all_passed = (test_pct >= PASSING_SCORE and
                  assignment_pct >= PASSING_SCORE and
                  exam_pct >= PASSING_SCORE)

    if not all_passed:
        return None

    if weighted_total >= HIGH_HONORS_CUTOFF:
        return "High Honors"
    elif weighted_total >= HONORS_CUTOFF:
        return "Honors"
    else:
        return None


def show_report(name, test, assignment, exam, weighted_total, status, award):
    """print a nice report card"""
    test_pct = (test / 20) * 100
    assignment_pct = (assignment / 20) * 100
    exam_pct = (exam / 60) * 100

    print()
    print("=" * 50)
    print(f"  REPORT CARD - {name}")
    print("=" * 50)
    print()
    print(f"  Test Score:       {test:>6.1f} / 20   ({test_pct:.1f}%)")
    print(f"  Assignment Score: {assignment:>6.1f} / 20   ({assignment_pct:.1f}%)")
    print(f"  Exam Score:       {exam:>6.1f} / 60   ({exam_pct:.1f}%)")
    print()
    print("-" * 50)
    print(f"  Weighted Total:   {weighted_total:>6.1f}%")
    print("-" * 50)
    print()

    # pass/fail with some flair
    if status == "PASSED":
        print(f"  Status:  {status}  :)")
    else:
        print(f"  Status:  {status}  :(")

    # award
    if award:
        print(f"  Award:   {award}  \u2605")
    else:
        print("  Award:   none this time")

    print()
    print("=" * 50)


def main():
    print()
    print("-" * 50)
    print("  STUDENT GRADE CALCULATOR")
    print("-" * 50)
    print()
    print("Enter the Student's Score:")
    print()

    # collect inputs
    student_name = input("Student's Name: ").strip()

    print()
    test_score = get_score("Test", 20)
    assignment_score = get_score("Assignment", 20)
    exam_score = get_score("Exam", 60)

    # arithmetic operations
    weighted_total = calculate_weighted_total(test_score, assignment_score, exam_score)

    # comparison operators for pass/fail
    status = get_status(weighted_total)

    # logical conditions for awards
    award = get_award(weighted_total, test_score, assignment_score, exam_score)

    # show results
    show_report(student_name, test_score, assignment_score, exam_score,
                weighted_total, status, award)

    # extra feedback
    print()
    if status == "FAILED":
        needed = PASSING_SCORE - weighted_total
        print(f"  you need {needed:.1f} more points to pass.")
        print("  keep studying!")
    elif award == "High Honors":
        print("  outstanding work! you're at the top of the class.")
    elif award == "Honors":
        print("  solid job! keep it up for high honors next time.")
    else:
        print(f"  you passed! aim for {HONORS_CUTOFF} for honors.")
    print()


if __name__ == "__main__":
    main()

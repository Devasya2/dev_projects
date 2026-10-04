import random
import time

def show_professor_face(expression):
    faces = {
        "grumpy": r"""
          (>_<)  [ grrrr... ]""",
        "angry": r"""
          (>_<)  [ STOP WASTING MY TIME! ]""",
        "thinking": r"""
          ( -_ -)  [ Typical... ] """,
        "shocked": r"""
          (o_O)  [ What do you want?! ] """
    }
    print(faces.get(expression, faces["grumpy"]))

def run_worthiness_quiz():
    """Runs a 3-question multiple-choice quiz and a timed palindrome challenge."""
    print("\n--------------------------------------------------")
    print("PROVING YOUR WORTH: Answer these questions!")
    print("--------------------------------------------------")
    
    questions = [
        {
            "q": "1. What should you do BEFORE bothering the professor with a question?",
            "options": ["A) Read Chapter 1 and check the portal", "B) Send 10 emails immediately", "C) Panic"],
            "ans": "A"
        },
        {
            "q": "2. How long should a meeting during lunch time be?",
            "options": ["A) 1 hour", "B) Under 2 minutes", "C) Until you finish talking"],
            "ans": "B"
        },
        {
            "q": "3. What is the professor's absolute favorite thing?",
            "options": ["A) Long explanations", "B) Grade complaints", "C) Silence"],
            "ans": "C"
        }
    ]

    score = 0
    for item in questions:
        print(f"\n{item['q']}")
        for opt in item['options']:
            print(f"  {opt}")
        
        user_ans = input("Your answer (A/B/C): ").strip().upper()
        if user_ans == item['ans']:
            score += 1

    # --- Palindrome Speed Challenge ---
    print("\n--------------------------------------------------")
    print("FINAL TEST: THE PALINDROME SPEED CHALLENGE!")
    print("Enter a valid palindrome (e.g., 'racecar', 'madam', 'nurses run').")
    print("You have LESS THAN 8 SECONDS!")
    print("--------------------------------------------------")

    start_time = time.time()
    palindrome_input = input("\nEnter your palindrome: ")
    end_time = time.time()

    time_taken = round(end_time - start_time, 2)
    cleaned_str = palindrome_input.strip().lower().replace(" ", "")

    # Check if string is a valid palindrome (minimum 2 characters)
    is_palindrome = len(cleaned_str) > 1 and cleaned_str == cleaned_str[::-1]

    print(f"\n[Time taken: {time_taken} seconds]")

    # Palindrome evaluation
    if is_palindrome and time_taken < 8:
        show_professor_face("thinking")
        print("Grumpy Assistant: You seem to be worthy.")
        palindrome_passed = True
    else:
        show_professor_face("angry")
        print("Grumpy Assistant: Stop wasting my time!")
        palindrome_passed = False

    # Must pass both the multiple-choice score requirement and the speed test
    return score >= 2 and palindrome_passed

def grumpy_assistant():
    show_professor_face("grumpy")
    print("Welcome to Prof. Grumpy's Office")
    print("I am his assistant. Speak quickly, he is very busy!")
    print("--------------------------------------------------\n")

    user_name = input("State your full name: ")
    clean_name = user_name.strip().title()
    
    if len(clean_name) == 0:
        show_professor_face("angry")
        print("Grumpy Assistant: You didn't even tell me your name! Go away!")
        return

    start_time = time.time()
    user_query = input("\nWhat do you want? > ")
    end_time = time.time()
    
    response_time = round(end_time - start_time, 2)
    print(f"\n[Took you {response_time} seconds to respond...]")

    cleaned_query = user_query.strip().lower()

    if "appointment" in cleaned_query or "meet" in cleaned_query:
        show_professor_face("thinking")
        print("Grumpy Assistant: You want to meet Prof. Grumpy? You must prove you are worthy first!")
        
        passed = run_worthiness_quiz()
        
        if passed:
            show_professor_face("thinking")
            slots = [
                "8:00 AM (Too early? Too bad!)", 
                "1:15 PM (Lunch time, keep it under 2 minutes!)", 
                "5:00 PM (Last slot, don't waste my time!)"
            ]
            print(f"\nGrumpy Assistant: Fine, you passed. You get a slot at {random.choice(slots)}")
        else:
            show_professor_face("angry")
            print("\nGrumpy Assistant: You failed the worthiness test! Go away!")

    elif "?" in cleaned_query:
        show_professor_face("thinking")
        print("Grumpy Assistant: That question is answered in Chapter 1. Read it properly!")

    else:
        show_professor_face("angry")
        print("Grumpy Assistant: You aren't making any sense. Come back later!")

if __name__ == "__main__":
    grumpy_assistant()
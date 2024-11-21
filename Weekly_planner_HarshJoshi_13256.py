import os

def create_weekly_planner():
    week = input("Enter the week (e.g., 'Week 1, Nov 20-26'): ")
    quote_of_the_week = input("Enter your 'Quote of the Week': ")
    books_to_read = input("Enter books you want to read this week (separate with commas): ").split(',')

    if not os.path.exists("Weekly_Planners"):
        os.makedirs("Weekly_Planners")

    planner_file = f"Weekly_Planners/Planner_{week.replace(' ', '_').replace(',', '')}.txt"
    with open(planner_file, 'w') as file:
        file.write(f"Weekly Planner - {week}\n")
        file.write("=" * 50 + "\n")
        file.write(f"Quote of the Week: {quote_of_the_week}\n\n")

        file.write("Books to Read This Week:\n")
        for book in books_to_read:
            file.write(f"- {book.strip()}\n")
        file.write("\n")

        file.write("Weekly Goals:\n")
        file.write("1. \n2. \n3. \n\n")

        file.write("To-Do List for the Week:\n")
        file.write("    - Task 1: \n")
        file.write("    - Task 2: \n")
        file.write("    - Task 3: \n")
        file.write("    - Task 4: \n")
        file.write("    - Task 5: \n\n")

        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            file.write(f"{day}:\n")
            file.write("    - To-Do 1: \n")
            file.write("    - To-Do 2: \n")
            file.write("    - To-Do 3: \n\n")

        file.write("Class Schedule:\n")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            file.write(f"{day}:\n")
            file.write("    - \n")
        file.write("\n")

        file.write("=" * 50 + "\n")
        file.write("End of Planner\n")

    print(f"Your weekly planner has been created: {planner_file}")

create_weekly_planner()

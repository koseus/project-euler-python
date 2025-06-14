import importlib
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py <problem_number>")
        return

    problem_number = sys.argv[1].zfill(3)  # e.g. "1" → "001"
    module_name = f"problems.problem{problem_number}"

    try:
        # Dynamically import the problem module
        problem_module = importlib.import_module(module_name)

        # Call the solve() function
        if hasattr(problem_module, "solve"):
            result = problem_module.solve()
            print(f"Problem {problem_number}: {result}")
        else:
            print(f"Module '{module_name}' does not have a solve() function.")

    except ModuleNotFoundError:
        print(f"Problem file not found: problems/problem{problem_number}.py")

if __name__ == "__main__":
    main()

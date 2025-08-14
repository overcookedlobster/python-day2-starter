import unittest
from io import StringIO
import sys

# We patch random.randint to make the guessing game deterministic for testing
import random
random.randint = lambda a, b: 42

class TestDay2Subtasks(unittest.TestCase):
    def run_script_with_input(self, script_name, inputs, expected_substring):
        # Redirect stdin and stdout
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        sys.stdin = StringIO('\n'.join(map(str, inputs)))
        sys.stdout = StringIO()

        try:
            # Execute the script
            with open(script_name, 'r') as f:
                exec(f.read(), {'__name__': '__main__'})
            
            # Get the output
            output = sys.stdout.getvalue().strip()
            self.assertIn(expected_substring, output)
        finally:
            # Restore original stdin and stdout
            sys.stdin = original_stdin
            sys.stdout = original_stdout

    # Sub-Task 1: Loops
    def test_loops_for_range(self):
        self.run_script_with_input("subtask1_loops.py", [], "1 2 3 4 5 6 7 8 9 10")

    def test_loops_for_list(self):
        self.run_script_with_input("subtask1_loops.py", [], "cherry")

    def test_loops_while_countdown(self):
        self.run_script_with_input("subtask1_loops.py", [], "Blast off!")

    def test_loops_sum(self):
        self.run_script_with_input("subtask1_loops.py", [], "Sum of 1 to 100: 5050")

    # Sub-Task 2: Guessing Game
    def test_guessing_game_too_low(self):
        self.run_script_with_input("subtask2_guessing_game.py", [20], "Too low!")

    def test_guessing_game_too_high(self):
        self.run_script_with_input("subtask2_guessing_game.py", [80], "Too high!")

    def test_guessing_game_correct(self):
        self.run_script_with_input("subtask2_guessing_game.py", [42], "You got it!")

    # Homework: Unit Converter
    def test_converter_km_to_miles(self):
        self.run_script_with_input("homework_unit_converter.py", [1, 10, 3], "6.21")

    def test_converter_c_to_f(self):
        self.run_script_with_input("homework_unit_converter.py", [2, 100, 3], "212.0")

    def test_converter_invalid_choice(self):
        self.run_script_with_input("homework_unit_converter.py", [4, 3], "Invalid choice")

    def test_converter_quit(self):
        self.run_script_with_input("homework_unit_converter.py", [3], "Goodbye!")

if __name__ == '__main__':
    unittest.main()


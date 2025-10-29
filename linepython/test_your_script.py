import unittest
import subprocess

class TestPipePython(unittest.TestCase):

    def run_script(self, name):
        result = subprocess.run(
            ['python3', './Pipepython.py', name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip(), result.stderr.strip()

    def test_correct_name(self):
        output, _ = self.run_script("B")
        self.assertEqual(output, "B")

    def test_incorrect_name(self):
        output, _ = self.run_script("Alice")
        self.assertEqual(output, "Wrong Name")

    def test_default_user(self):
        output, _ = self.run_script("")
        self.assertEqual(output, "Wrong Name")

if __name__ == '__main__':
    unittest.main()

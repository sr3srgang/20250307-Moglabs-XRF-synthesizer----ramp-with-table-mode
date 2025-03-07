import unittest
import subprocess
import sys

class TestSynthScriptIntegration(unittest.TestCase):
    def test_script_runs_successfully(self):
        # Command to run the script using the current Python interpreter.
        cmd = [sys.executable, 'manual_example_python_script.py']
        
        # Run the script as a subprocess and capture output.
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Assert that the script finished with a 0 exit code.
        self.assertEqual(result.returncode, 0, f"Script failed with error: {result.stderr}")
        
        # Optionally, check that the output contains expected strings.
        self.assertIn("Device info:", result.stdout)
        self.assertIn("Command response:", result.stdout)

if __name__ == '__main__':
    unittest.main()
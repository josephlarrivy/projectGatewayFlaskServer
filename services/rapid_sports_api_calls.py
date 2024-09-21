import os
from dotenv import load_dotenv

load_dotenv('.env')

TEST_RAPID_SPORTS_API_KEY = os.getenv('TEST_RAPID_SPORTS_API_KEY')

class TestModule:
    @classmethod
    def do_import_test(cls):
        return TEST_RAPID_SPORTS_API_KEY

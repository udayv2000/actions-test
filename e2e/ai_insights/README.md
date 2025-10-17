### How to setup

1. create virtual env and activate it
2. pip install --upgrade pip setuptools wheel (or uv pip install --upgrade pip setuptools wheel)
3. pip install -e ./e2e/ai_insights (or uv pip install -e ./e2e/ai_insights)
4. playwright install 

Now you have everything needed to write and execute tests.

### How to run test

There is one example test in e2e/ai_insights/tests/test_login.py, which can be run with `pytest e2e/ai_insights/tests/test_login.py`. 
However, you should create an account first and input the credentials in the test file (you can also take those out as variable, and re-use them in other tests, up to you)

Upon any test failures, pytest generates report - report.html - there is an example one in the `/tests` folder.
Also, we have Playwright recordings.

### Check Playwright recordings

Currently, Playwright is set up to record all failed tests - `--tracing=retain-on-failure` in the `pytest.ini` file. If you want to record all tests, even the successful ones, change the value to `on` (or pass it as an argument when running tests). 

The recordings are saved under the test-results folder of the working directory.
You can open the recording by going to the directory in the terminal and running `playwright show-trace trace.zip`.
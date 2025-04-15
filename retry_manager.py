from tenacity import retry, stop_after_attempt, wait_random

@retry(stop=stop_after_attempt(3), wait=wait_random(1, 2))
def risky_operation():
    # Call logic here
    pass
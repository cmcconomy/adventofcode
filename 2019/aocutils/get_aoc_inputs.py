import os
import requests
from dotenv import load_dotenv

print("it works")

load_dotenv()

# This section permits a lazy way to retrieve your personal inputs.
# To make it work, log into AoC from your browser and go into developer options to look at your cookies
# I know this works for logging in via github, but I don't know if it works for other auth styles.
# Note the 'session' cookie value
#
# Create a file in the root of this project folder called ".env" and in it, put the following:
# AOC_SESSION=840372b93dj387023n729c5304857fj20f
# where the values match your actual login params.

def get_aoc_inputs(day):
    url="https://adventofcode.com/2019/day/%d/input" % day
    
    cookies = {
        'session': os.getenv("AOC_SESSION")
    }
    return requests.get(url,cookies=cookies).text.split()


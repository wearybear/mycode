#!/usr/bin/env python3

# part1 from the challenge list, ppull the strings eyes, goggles, and nothing and create a print function for output.
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

a= challenge[2][1]
b= challenge[2][0]
c= challenge[3]

print(f"My {a}! The {b} do {c}!")

# part1a from the trial list pull the strings eyes, goggles, and nothing and create a print function for output.
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

a= trial[2]["goggles"]
b= trial[2]["eyes"]
c= trial[-1]

print(f"My {a}! The {b} do {c}!")

# part1b from the nightmare list, pull the strings eyes, goggles, and nothing and create a print function for output.
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a= nightmare[0]["user"]["name"]["first"]
b= nightmare[0]["kumquat"]
c= nightmare[0]["d"]

print(f"My {a}! The {b} do {c}!")


# yes I used ChatGPT, no I am no ashamed. -Jeremy M.

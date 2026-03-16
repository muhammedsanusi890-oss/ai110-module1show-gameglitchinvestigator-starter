# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game Purpose:** A number guessing game built with Streamlit where the player tries to guess a secret number within a limited number of attempts. The game gives hints after each guess to guide the player higher or lower, and awards points based on how quickly they find the answer.

- [x] **Bugs Found:**
  - **State Bug:** The secret number was regenerating every time the Submit button was clicked, making it impossible to win because the target kept changing mid-game.
  - **Logic Bug:** The hint messages were flipped — when the guess was too high it said "Go HIGHER" and when the guess was too low it said "Go LOWER", which actively misled the player.

- [x] **Fixes Applied:**
  - **State Fix:** Stored the secret number in `st.session_state` so it only generates once at the start of a game and persists across button clicks.
  - **Logic Fix:** Corrected the `check_guess` function in `logic_utils.py` so that a too-high guess returns "Guess LOWER" and a too-low guess returns "Guess HIGHER".

## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

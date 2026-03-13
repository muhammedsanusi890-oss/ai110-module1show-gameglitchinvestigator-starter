# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

=> it is a game where you actually have to guess a number.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1) The hints are Wrong, this might be a bug in the code. 
2) After you guessed the right number or pass the total attempt, it doesn't let you start a new game after clicking the new game button. 
3) I believe the history also has a bug. if i put in a number the number do not get passed into the array until i guess another number. 
4) The test cases in line 3 - 16 are also logically wrong. 


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
CLAUDE AI
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
for the problem in number 3 above. it suggested that invalid guesses should not be appended to history. after fixing it, i verified with pytest logic

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
None
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
by checking the game live. 

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.

I ran `pytest tests/test_game_logic.py` after rewriting the test file. The original tests had the assertions backwards — for example, they expected "Too Low" when the guess was above the secret. Running pytest confirmed all 9 rewritten tests passed after I fixed `check_guess` in logic_utils.py. The regression tests I added (like `test_too_high_message_does_not_say_go_higher`) also gave me confidence that the flipped-hint bug could never silently come back.

- Did AI help you design or understand any tests? How?

Yes. Claude pointed out that the original test assertions were logically inverted and explained what each test *should* be checking. It specifically suggested adding regression tests — tests that assert the old broken behavior is gone — so that future changes can't accidentally re-introduce the flipped hints bug. I verified each suggested test by reading the `check_guess` function alongside the assertion to make sure the logic matched.


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

Every time you clicked a button or typed something in Streamlit, the entire Python script ran again from the very top. The original code called `random.randint()` at the top level with no guard, so every rerun produced a brand new secret number. This made the game impossible to win because the target kept shifting with every interaction.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Imagine every time you click a button on a webpage, the entire page reloads from scratch and forgets everything. That is how Streamlit works by default — every interaction triggers a full rerun of the script. Session state is like a sticky notepad that survives those reruns; values you store there (like the secret number or your attempt count) are remembered even after the script reruns, so the game stays consistent.

- What change did you make that finally gave the game a stable secret number?

The fix was wrapping the secret number generation in `if "secret" not in st.session_state:`. This means `random.randint()` only runs once — when the game first loads and no secret exists yet. On every subsequent rerun, the condition is false and the existing secret in session state is kept, so the target stays the same for the entire game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

Writing regression tests immediately after fixing a bug. When I fixed the flipped hints, I added tests that specifically assert the old broken behavior is gone. This means that even if someone changes `check_guess` in the future, the tests will catch any reintroduction of the same bug. It is a low-effort step that gives lasting protection.

- What is one thing you would do differently next time you work with AI on a coding task?

I would read and understand the existing code more carefully before asking AI for help. A few times I described a bug to Claude without fully understanding what the code was supposed to do, which made the back-and-forth less efficient. Forming my own hypothesis first would make my prompts more precise and the AI suggestions more targeted.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project showed me that AI-generated code can look completely reasonable on the surface but contain subtle logic bugs — like reversed hints or a missing status reset — that only surface when you actually use the program. You cannot just trust that AI output is correct; you have to read it critically, test it, and verify the behavior yourself.

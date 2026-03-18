# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").

--- The game looked like less engaging and the layout out and setup were rondom instead of being user intiution friendly.
_ Three bugs I noticed were that the hints were backwards, the new game flow sometimes got stuck, and difficulty behavior felt inconsistent.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
* I used copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
* Correct suggestion: Copilot suggested storing the secret number in `st.session_state` and only creating it once, instead of recreating it on reruns. This was correct because the secret stopped changing every time I clicked Submit. I verified it by opening Developer Debug Info and watching the secret stay stable until New Game or difficulty change.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
* Incorrect/misleading suggestion: one AI-generated version used mixed types by turning the secret into a string on some attempts, which caused unreliable comparisons. This was misleading because it made win checks inconsistent depending on attempt flow. I verified the problem by reading the code path and then confirming the fix with targeted pytest regression tests.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
* I treated a bug as fixed only when both manual gameplay and automated tests matched expected behavior. I checked the game UI and Developer Debug Info to make sure state and hints behaved consistently. If either manual behavior or tests disagreed, I kept iterating.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
* I ran `PYTHONPATH=. pytest -q` and used tests that specifically check reversed hints, difficulty ranges, parse errors, and mixed-type secret handling. These tests showed the logic functions now return the expected outcomes and messages. I also manually changed difficulty and started a new game to confirm state resets correctly.
- Did AI help you design or understand any tests? How?
* Yes. Copilot helped propose regression-style tests for each fixed bug so I could verify behavior directly. It helped me map each gameplay issue to one function-level test in `logic_utils.py` behavior through `tests/test_game_logic.py`.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
* The secret number kept changing because Streamlit reruns the script after each interaction, and the value was being regenerated during reruns.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
* I would say reruns are like replaying the whole script every click, and `session_state` is the memory that keeps values between those reruns.
- What change did you make that finally gave the game a stable secret number?
* I stored the secret in `st.session_state` and only initialized it when it did not already exist, then reset it only on New Game or difficulty change.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
* I want to keep writing small regression tests right after each fix so I can quickly confirm bugs do not come back.
- What is one thing you would do differently next time you work with AI on a coding task?
* Next time I would ask AI for smaller, step-by-step changes and verify each one immediately instead of applying big edits at once.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
* This project showed me AI code can speed up development, but it still needs careful review and testing. I now treat AI output as a draft, not a final answer.

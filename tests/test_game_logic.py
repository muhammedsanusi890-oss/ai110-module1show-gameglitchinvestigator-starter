from logic_utils import check_guess

#FIXED: rewrote the tests and added regressions test to prevent old bugs from coming back. 

#FIXED TEST
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests for the corrected hint messages (Bug 1 fix: flipped Go HIGHER/Go LOWER)

def test_too_high_message_says_go_lower():
    # Guess is above secret — player must go LOWER, not higher
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_message_says_go_higher():
    # Guess is below secret — player must go HIGHER, not lower
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_too_high_message_does_not_say_go_higher():
    # Regression: old bug returned "Go HIGHER" when guess was too high
    _, message = check_guess(60, 50)
    assert "HIGHER" not in message

def test_too_low_message_does_not_say_go_lower():
    # Regression: old bug returned "Go LOWER" when guess was too low
    _, message = check_guess(40, 50)
    assert "LOWER" not in message

def test_correct_guess_message():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

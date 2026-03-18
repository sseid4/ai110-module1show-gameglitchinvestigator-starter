from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


def test_hint_is_too_high_when_guess_exceeds_secret():
    """Regression: hints were previously reversed."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_hint_is_too_low_when_guess_is_below_secret():
    """Regression: hints were previously reversed."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_winning_guess_reports_win_and_success_message():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_win_still_detected_when_secret_is_string():
    """Regression: app previously mixed int and str secret values."""
    outcome, _ = check_guess(42, "42")
    assert outcome == "Win"


def test_difficulty_ranges_match_expected_ordering():
    """Regression: difficulty ordering/ranges were incorrect in earlier builds."""
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)


def test_parse_guess_rejects_empty_input():
    ok, guess, err = parse_guess("")
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."


def test_parse_guess_rejects_non_numeric_input():
    ok, guess, err = parse_guess("banana")
    assert ok is False
    assert guess is None
    assert err == "That is not a number."


def test_update_score_first_try_win_uses_current_attempt_math():
    """Regression: attempts initialization and scoring drifted due off-by-one changes."""
    assert update_score(current_score=0, outcome="Win", attempt_number=1) == 80


def test_update_score_never_drops_below_minimum_win_points():
    assert update_score(current_score=0, outcome="Win", attempt_number=30) == 10

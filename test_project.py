import pytest
from project import add_month_budget, display_month_budget, calculate_total_savings, budget

def test_add_month_budget(monkeypatch):
    budget.clear()

    user_input = [
        "1000",
        "600"
    ]
    # read user input
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))

    add_month_budget("January")

    assert budget["January"]["income"] == 1000
    assert budget["January"]["expenses"] == 600
    assert budget["January"]["savings"] == 400

def test_display_month_budget(capsys):
    budget.clear()

    budget["January"] = {
        "income": 1000,
        "expenses": 500,
        "savings": 500
    }

    # testing display budget for January
    display_month_budget("January")
    captured = capsys.readouterr()
    expected_output = "Budget for January\nIncome: 1000\nExpenses: 500\nSavings: 500 \n\n"
    assert captured.out == expected_output

    # we didn't initialize any value for February month
    display_month_budget("February")
    captured = capsys.readouterr()
    expected_output = "Budget for February not found.\n\n"
    assert captured.out == expected_output

def test_calculate_total_savings(capsys):
    budget.clear()

    # Without any initialization for any month
    calculate_total_savings()
    captured = capsys.readouterr()
    expected_output = "Total savings: 0 \n\n"
    assert captured.out == expected_output

    # After initialize some value for some months
    budget["January"] = {
        "income": 1000,
        "expenses": 700,
        "savings": 300
    }
    budget["February"] = {
        "income": 1200,
        "expenses": 400,
        "savings": 800
    }
    budget["March"] = {
        "income": 800,
        "expenses": 500,
        "savings": 300
    }
    calculate_total_savings()
    captured = capsys.readouterr()
    expected_output = "Total savings: 1400 \n\n"
    assert captured.out == expected_output
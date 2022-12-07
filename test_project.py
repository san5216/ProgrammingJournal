import pytest
import project


def test_display_menu(capfd):
    project.display_menu()
    out, err = capfd.readouterr()
    assert type(out) is str


def test_get_user_choice_exit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "4")
    with pytest.raises(SystemExit):
        assert project.get_user_choice()


def test_get_user_choice_invalid(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "B")
    assert project.get_user_choice() == 0


def test_get_quote():
    assert len(project.get_quote()) > 0

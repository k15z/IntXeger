"""Test command module and argument handling."""
import pytest

from intxeger.__main__ import main
from intxeger import __version__


def test_expand_with_defaults(capsys):
    """Test that by default one expansion is printed per line."""
    with pytest.raises(SystemExit) as exinfo:
        main(['[a-c]'])
    capture = capsys.readouterr()
    assert capture.out == "a\nb\nc\n"
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_expand_space_terminator(capsys):
    """Test that expansions can be space terminated."""
    with pytest.raises(SystemExit) as exinfo:
        main(['-t', ' ', '[a-c]'])
    capture = capsys.readouterr()
    assert capture.out == "a b c "
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_expand_empty_terminators(capsys):
    """Test that expansions can be terminated by an empty string."""
    with pytest.raises(SystemExit) as exinfo:
        main(['-t', '', '[a-c]'])
    capture = capsys.readouterr()
    assert capture.out == "abc"
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_expand_with_nul_terminators(capsys):
    """Test that expansions can be terminated by a NUL character."""
    with pytest.raises(SystemExit) as exinfo:
        main(['-0', '[a-c]'])
    capture = capsys.readouterr()
    assert capture.out == "a\x00b\x00c\x00"
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_expand_ascending(capsys):
    """Test that expansions can be output sorted."""
    with pytest.raises(SystemExit) as exinfo:
        main(['--order', 'asc', '[a-c]'])
    capture = capsys.readouterr()
    assert capture.out == "a\nb\nc\n"
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_expand_descending(capsys):
    """Test that expansions can be output sorted, highest to lowest."""
    with pytest.raises(SystemExit) as exinfo:
        main(['--order', 'desc', '[a-c]'])
    capture = capsys.readouterr()
    assert capture.out == "c\nb\na\n"
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_expand_random_order(capsys):
    """Test that expansions can be output in a random order"""
    with pytest.raises(SystemExit) as exinfo1:
        main(['--order', 'random', '[a-z]'])
    capture1 = capsys.readouterr()
    assert capture1.err == ""
    assert exinfo1.value.code == 0

    with pytest.raises(SystemExit) as exinfo2:
        main(['--order', 'random', '[a-z]'])
    capture2 = capsys.readouterr()
    assert capture2.err == ""
    assert exinfo2.value.code == 0

    # Probability p of 2 randomly selected outputs matching is
    #   p = 1 - ((N-1) / N)         -- N = number of possible outputs
    #     = 1 - ((26!-1) / 26!)     -- [a-z] -> N = factorial(26) = 26!
    #     = 2.48 × 10^-27           -- essentially 0
    # https://preshing.com/20110504/hash-collision-probabilities/
    assert capture1.out != capture2.out
    assert sorted(capture1.out.split()) == sorted(capture2.out.split())


def test_terminator_arguments_are_mutually_exclusive(capsys):
    """Test that contradicting terminators raise an error."""
    with pytest.raises(SystemExit) as exinfo:
        main(['-0', '--terminator', ' ', '[a-c]'])

    capture = capsys.readouterr()
    assert capture.out == ""
    assert capture.err.find("error: argument --terminator/-t: not allowed with argument -0") > 0
    assert exinfo.value.code > 0


def test_help(capsys):
    """Test that help is available."""
    with pytest.raises(SystemExit) as exinfo:
        main(['--help'])
    capture = capsys.readouterr()
    assert capture.out.startswith("usage:")
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_version(capsys):
    """Test that the version is available."""
    with pytest.raises(SystemExit) as exinfo:
        main(['--version'])
    capture = capsys.readouterr()
    assert capture.out == f"{__version__}\n"
    assert capture.err == ""
    assert exinfo.value.code == 0


def test_no_args_errors(capsys):
    """Test that an error is reported when no expression is provided."""
    with pytest.raises(SystemExit) as exinfo:
        main([])
    capture = capsys.readouterr()
    assert capture.out == ""
    assert capture.err.endswith("error: the following arguments are required: regex\n")
    assert exinfo.value.code > 0


def test_excess_args_errors(capsys):
    """Test that an error is reported when too many arguments are provided."""
    with pytest.raises(SystemExit) as exinfo:
        main(['[a-c]', '[1-3]'])
    capture = capsys.readouterr()
    assert capture.out == ""
    assert capture.err.find("error: unrecognized arguments") > 0
    assert exinfo.value.code > 0

def test_invalid_regex_errors(capsys):
    """Test that an error is reported when the regex cannot be parsed."""
    with pytest.raises(SystemExit) as exinfo:
        main(['[a-c'])
    capture = capsys.readouterr()
    assert capture.out == ""
    assert capture.err.find("error: argument regex: unterminated character set at position 0") > 0
    assert exinfo.value.code > 0

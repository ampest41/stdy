from src.decorators import log
import pytest




def test_log_success(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def test_func(a, b):
        return a + b
    result = test_func(1, 2)
    assert result == 3
    content = log_file.read_text()
    assert "test_func ok\n" in content



def test_log_failure(tmp_path):
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def test_func(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        test_func(6, 0)

    content = log_file.read_text()
    assert "test_func error: ZeroDivisionError. Inputs: (6, 0), {}" in content



def test_log_success_console(capsys):
    @log()
    def test_func(a, b):
        return a + b

    result = test_func(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert "test_func ok" in captured.out



def test_log_error_console(capsys):
    @log()
    def bad_func(x):
        return 10 / x

    # Вызываем с x=0 → ошибка
    with pytest.raises(ZeroDivisionError):
        bad_func(0)

    captured = capsys.readouterr()
    assert "bad_func error: ZeroDivisionError. Inputs: (0,), {}" in captured.out
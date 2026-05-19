import pytest

from app import process_string
from app_with_errors import process_string_buggy


# 1. ТЕСТЫ ЧЕРНОГО ЯЩИКА (Проверяем логику по ТЗ)

@pytest.mark.parametrize("input_data, expected", [
    ("hello", {"k": 0, "m": 0}),   # test1: Без k, m и цифр
    ("km_test", {"k": 1, "m": 1}), # test2: Есть по одной k и m
    ("k1m", 0),                    # test3: Цифра внутри строки
    ("123", 0),                    # test4: Только цифры
    ("", {"k": 0, "m": 0}),        # test5: Пустая строка
])
def test_black_box_correct_app(input_data, expected):
    """Проверка исправного приложения тестами Черного ящика (Все должны пройти)"""
    assert process_string(input_data) == expected


@pytest.mark.parametrize("input_data, expected", [
    ("hello", {"k": 0, "m": 0}),
    ("km_test", {"k": 1, "m": 1}), # Упадет из-за ошибки №2 (.cont)
    ("k1m", 0),                    # Упадет из-за ошибки №1 (вернет словарь вместо 0)
    ("123", 0),
    ("", {"k": 0, "m": 0}),
])
def test_black_box_buggy_app(input_data, expected):
    """Проверка сломанного приложения тестами Черного ящика (Упадут 2 теста)"""
    assert process_string_buggy(input_data) == expected


# =====================================================================
# 2. ТЕСТЫ БЕЛОГО ЯЩИКА (Покрытие операторов / строк кода)
# =====================================================================

@pytest.mark.parametrize("input_data", [
    "1",  # Покрывает ветку `if` (строка с цифрой)
    "k",  # Покрывает ветку `else` / основной код подсчета
])
def test_white_box_correct_app(input_data):
    """Проверка исправного приложения на покрытие операторов (Все пройдут)"""
    result = process_string(input_data)
    assert result == 0 or isinstance(result, dict)


@pytest.mark.parametrize("input_data", [
    "1",  # Покрывает ветку `if`. Ошибка №1 не вскроется, тест пройдет!
    "k",  # Покрывает ветку подсчета. Упадет из-за ошибки №2 (.cont)
])
def test_white_box_buggy_app(input_data):
    """Проверка сломанного приложения на покрытие операторов (Упадет 1 тест)"""
    result = process_string_buggy(input_data)
    assert result == 0 or isinstance(result, dict)
"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
import pytest


@pytest.fixture
def func():
    return Stack("data1")


def test__str__():
    assert func.__str__() == "data1"

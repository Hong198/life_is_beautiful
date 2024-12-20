import re


def test_srt():
    sentence = '"아, 감사합니다"'
    cleaned_sentence = sentence.replace('"', '')
    assert cleaned_sentence == "아, 감사합니다"


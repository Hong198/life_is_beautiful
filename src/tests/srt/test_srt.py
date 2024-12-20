import re


def test_srt():
    sentence = '"아, 감사합니다"'
    cleaned_sentence = sentence.replace('"', '')
    assert cleaned_sentence == "아, 감사합니다"


TEXT = """1
00:00:47,797 --> 00:00:50,300
[옅은 자동차 엔진음]
[옅은 자동차 경적]"""
lines = TEXT.splitlines()


def remove_index(line: str) -> str:
    line = re.sub(r'^\d+', '', line)
    return line


def remove_time(line: str):
    line = re.sub(r'\d{2}:\d{2}:\d{2},\d{3}\s*--> \s*\d{2}:\d{2}:\d{2},\d{3}', '', line)
    return line


def remove_square(line: str) -> str:
    line: str = re.sub(r'\[.*?\]', '', line)
    return line


def test_text():
    cleaned_lines = []  # 수정된 라인을 저장할 리스트

    for line in lines:
        # 각 함수 호출 후 수정된 값을 바로 덮어쓰기
        # line = remove_index(line)
        line = remove_time(line)
        # line = remove_square(line)

        # 빈 줄이 아니면 cleaned_lines에 추가
        if line.strip():
            cleaned_lines.append(line.strip())

    # 결과 출력
    for line in cleaned_lines:
        print(line)
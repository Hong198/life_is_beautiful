import re
from idlelib.iomenu import encoding
from pathlib import Path
from typing import List
import pandas as pd


def processing(file_path: Path) -> List:
    if not file_path.is_file():
        raise Exception

    cleaned_lines = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = re.sub(r'^\d+', '', line)  # 앞에 숫자 삭제
            # line = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', '', line)  # 시간 정보 제거
            line = re.sub(r'\d{2}:\d{2}:\d{2},\d{3}\s*--> \s*\d{2}:\d{2}:\d{2},\d{3}', '', line)  # 시간 정보 제거
            line = re.sub(r'\[.*?\]', '', line)  # 대괄호 안의 내용 제거
            line = re.sub(r'\s*\(.*?\)\s*', ' ', line)  # 괄호 안의 내용 제거
            line = re.sub(r'#NAME\?', '', line)  # #NAME 부분 삭제
            line = line.replace('""', '')  # 빈 문자열 "" 삭제
            line = line.replace('-', '')  # 모든 "-" 문자를 삭제

            if line.strip():  # 빈 문자열인 경우에는 추가하지 않음
                line = line.replace('"', '').strip()
                cleaned_lines.append(line.strip())
    return cleaned_lines


def save(lines: List, output_path: Path):
    # 처리된 텍스트 저장
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
    print("처리 완료! 'sample.txt' 파일에 저장되었습니다.")


if __name__ == '__main__':
    srt_path = Path("../data/life_is_beautiful.srt")
    output_path = Path(f"../data/result/{srt_path.stem}.txt")
    cleaned_lines = processing(srt_path)
    save(cleaned_lines, output_path)

    df = pd.DataFrame(cleaned_lines, columns=["sentence"])
    print(df.head())

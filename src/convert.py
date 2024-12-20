import chardet

# 파일의 인코딩 감지
with open('../data/life_is_beautiful.srt', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)

# 감지된 인코딩으로 파일 읽기
with open('../data/life_is_beautiful.srt', 'r', encoding=result['encoding']) as file:
    lines = file.readlines()

# utf-8로 새 파일로 저장
with open('../data/life_is_beautiful_utf8.srt', 'w', encoding='utf-8') as file:
    file.writelines(lines)

print("파일이 성공적으로 utf-8로 저장되었습니다.")

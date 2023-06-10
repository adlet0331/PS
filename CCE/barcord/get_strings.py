import requests

url = 'http://20.214.201.164:5959/download'

binary_strings = []  # 다운로드한 파일들의 0과 1로 이루어진 문자열을 저장할 리스트

for i in range(10):
    response = requests.get(url)
    binary_string = ''.join(format(byte, '08b') for byte in response.content)  # 파일의 내용을 0과 1로 이루어진 문자열로 변환
    binary_strings.append(binary_string)

# 파일들의 0과 1로 이루어진 문자열 출력
for i, binary_string in enumerate(binary_strings):
    file_name = f'download_{i}.txt'  # 저장할 파일 이름
    print(len(binary_string))
    with open(file_name, 'w') as file:
        file.write(binary_string[3520 * 50: 3520 * 51])
    print(f"File {file_name} saved.")

print("All files saved successfully.")

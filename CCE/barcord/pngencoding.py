import base64

# PNG 파일을 Base64로 인코딩
with open('downloaded.png', 'rb') as file:
    png_data = file.read()
    base64_data = base64.b64encode(png_data).decode('utf-8')

# Base64로 인코딩된 PNG 데이터를 출력
print(base64_data)
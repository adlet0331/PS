import requests
from PIL import Image
from io import BytesIO
import time
import barcode
from barcode.writer import ImageWriter

# PNG 파일 다운로드
url = 'http://20.214.201.164:5959/download'

start_time = time.time()
response = requests.get(url)
image = Image.open(BytesIO(response.content))

# # 다운로드한 PNG 파일 저장
# with open('downloaded.png', 'wb') as file:
#     file.write(response.content)

# # 이미지 열기
# image = Image.open('downloaded.png')

# 이미지의 픽셀 데이터 가져오기
pixels = image.load()
width, height = image.size
# print(width)

# 바코드 데이터 생성
barcode_str = ''
for x in range(width):
    # if x % 2 == 0: 
    #     continue
    r, g, b = pixels[x, 120]
    
    # 흰색 픽셀은 1로, 그 외의 픽셀은 0으로 처리
    if r == 255 and g == 255 and b == 255:
        barcode_str += '1'
    else:
        barcode_str += '0'

# print(barcodes)
cut_len = -1
front_padding = 0
end_padding = 0
if barcode_str:
    barcode_str = barcode_str[front_padding : len(barcode_str) - end_padding]
    barcode_data = barcode.get('code128', barcode_str, writer=ImageWriter())
    filename = 'code128_barcode.png'  # 저장할 파일 이름
    barcode_data.save(filename)

    # 변환된 데이터 전송
    payload = {'data': barcode_data}
    url = 'http://20.214.201.164:5959/get_flag'
    with open(filename, 'rb') as file:
        files = {'file': file}
    response = requests.post(url, files=files)

    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
    # 결과 확인
    print(response.text)
else:
    print("바코드를 인식할 수 없습니다.")

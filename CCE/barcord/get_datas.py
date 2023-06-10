import requests
from PIL import Image
from io import BytesIO

url = 'http://20.196.211.35:5959/download'

for i in range(2,5):
    response = requests.get(url)

    image = Image.open(BytesIO(response.content))
    pixels = image.load()
    width, height = image.size

    barcodes = ''
    for x in range(width):
        # if x % 2 == 0: 
        #     continue
        r, g, b = pixels[x, 120]
        
        # 흰색 픽셀은 1로, 그 외의 픽셀은 0으로 처리
        if r == 255 and g == 255 and b == 255:
            barcodes += '1'
        else:
            barcodes += '0'

    file_name = f'download_{i}'  # 저장할 파일 이름
    with open(file_name, 'w') as file:
        file.write(barcodes)
    print(f"File {file_name} downloaded.")

print("All files downloaded successfully.")

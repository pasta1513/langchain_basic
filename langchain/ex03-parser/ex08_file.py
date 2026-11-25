from pathlib import Path

CARD_DIR = Path(__file__).parent / 'card'
print(CARD_DIR)

print('----==== 폴더 안 모든 파일 확인 ====----')
for p in CARD_DIR.glob('*'):
    print(p)

print('----==== 폴더 안 png 확장자 파일 확인 ====----')
for p in CARD_DIR.glob('*.png'):
    print(p)

print('----==== 폴더 안 여러 확장자 파일 확인 ====----')
for p in CARD_DIR.glob('*.[jp][pn]g'):
    print(p)

print('----==== 확장자 제거 후 이름만 확인 ====----')
names = [p.stem for p in CARD_DIR.glob('*')]
print(names)

print('----==== 특정 파일 존재 여부 확인 ====----')
print((CARD_DIR/'홍길동.jpg').exists())
print((CARD_DIR/'아무나.jpg').exists())
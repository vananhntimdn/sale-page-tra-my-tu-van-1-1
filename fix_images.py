with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Đổi ảnh Hero (IMAGE513 Desktop & IMAGE554 Mobile) sang ảnh cô gái cười (hero-portrait-small.webp)
content = content.replace(
    '#IMAGE513 > .ladi-image > .ladi-image-background{background-image: url("./images/quiz-girl.webp");}',
    '#IMAGE513 > .ladi-image > .ladi-image-background{background-image: url("./images/hero-portrait-small.webp");}'
)
content = content.replace(
    '#IMAGE554 > .ladi-image > .ladi-image-background{background-image: url("./images/quiz-girl.webp");}',
    '#IMAGE554 > .ladi-image > .ladi-image-background{background-image: url("./images/hero-portrait-small.webp");}'
)

# 2. Đổi ảnh Section "Có phải..." (IMAGE515) sang ảnh cô gái buồn (quiz-girl.webp)
content = content.replace(
    '#IMAGE515 > .ladi-image > .ladi-image-background{background-image: url("./images/heart-icon.webp");}',
    '#IMAGE515 > .ladi-image > .ladi-image-background{background-image: url("./images/quiz-girl.webp");}'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Đã đổi chuẩn xác ảnh Hero và ảnh Section Có Phải!")
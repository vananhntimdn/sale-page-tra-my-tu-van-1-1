with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Sửa ảnh Hero Desktop sang hero-portrait-small
content = content.replace(
    '#IMAGE513 > .ladi-image > .ladi-image-background{background-image: url("./images/quiz-girl.webp");}',
    '#IMAGE513 > .ladi-image > .ladi-image-background{background-image: url("./images/hero-portrait-small.webp");}'
)

# 2. Sửa ảnh Section Có phải sang quiz-girl
content = content.replace(
    '#IMAGE515 > .ladi-image > .ladi-image-background{background-image: url("./images/heart-icon.webp");}',
    '#IMAGE515 > .ladi-image > .ladi-image-background{background-image: url("./images/quiz-girl.webp");}'
)

# 3. Sửa ảnh Trà My kế tiếp Desktop sang story-inline-3
content = content.replace(
    '#IMAGE550 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-1.webp");}',
    '#IMAGE550 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}'
)

# 4. Sửa ảnh Trà My kế tiếp Mobile sang story-inline-3
content = content.replace(
    '#IMAGE559 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-1.webp");}',
    '#IMAGE559 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Đã cập nhật đúng toàn bộ vị trí ảnh!")
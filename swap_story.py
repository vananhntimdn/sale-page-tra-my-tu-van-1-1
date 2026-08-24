with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Vị trí trên (IMAGE550 Desktop & IMAGE559 Mobile) -> gán story-portrait
content = content.replace(
    '#IMAGE550 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}',
    '#IMAGE550 > .ladi-image > .ladi-image-background{background-image: url("./images/story-portrait.webp");}'
)
content = content.replace(
    '#IMAGE559 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}',
    '#IMAGE559 > .ladi-image > .ladi-image-background{background-image: url("./images/story-portrait.webp");}'
)

# 2. Vị trí dưới (IMAGE548 Desktop & IMAGE558 Mobile) -> gán story-inline-3
content = content.replace(
    '#IMAGE548 > .ladi-image > .ladi-image-background{background-image: url("./images/story-portrait.webp");}',
    '#IMAGE548 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}'
)
content = content.replace(
    '#IMAGE558 > .ladi-image > .ladi-image-background{background-image: url("./images/story-portrait.webp");}',
    '#IMAGE558 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Đã đảo vị trí 2 ảnh thành công!")
```[cite: 1]

---

**Nếu muốn sửa bằng tay trong VS Code (`Ctrl + H`):**

* Tìm: `#IMAGE550 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}` -> Sửa thành: `url("./images/story-portrait.webp");`[cite: 1]
* Tìm: `#IMAGE559 > .ladi-image > .ladi-image-background{background-image: url("./images/story-inline-3.webp");}` -> Sửa thành: `url("./images/story-portrait.webp");`[cite: 1]
* Tìm: `#IMAGE548 > .ladi-image > .ladi-image-background{background-image: url("./images/story-portrait.webp");}` -> Sửa thành: `url("./images/story-inline-3.webp");`[cite: 1]
* Tìm: `#IMAGE558 > .ladi-image > .ladi-image-background{background-image: url("./images/story-portrait.webp");}` -> Sửa thành: `url("./images/story-inline-3.webp");`[cite: 1]
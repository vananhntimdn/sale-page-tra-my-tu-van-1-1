import re

# 1. URL Google Apps Script nhận dữ liệu Form
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxTGbfSSCh8SpAyz49HBBD1uG12ukQVWrrNBjuBUvENq2e9Z4KjGwOlqstmIQ6X1xiUog/exec"

# 2. Link nhóm Zalo điều hướng sau khi đăng ký
ZALO_GROUP_URL = "https://zalo.me/g/vh6vyxjcvobu3zgdihub"

script_code = f"""
<script>
  const GOOGLE_SCRIPT_URL = "{GOOGLE_SCRIPT_URL}";
  const ZALO_GROUP_URL = "{ZALO_GROUP_URL}";

  document.querySelectorAll("form.ladi-form").forEach(form => {{
    form.addEventListener("submit", function(e) {{
      e.preventDefault();
      const formData = new FormData(form);

      fetch(GOOGLE_SCRIPT_URL, {{
        method: "POST",
        body: formData,
        mode: "no-cors"
      }})
      .then(() => {{
        window.location.href = ZALO_GROUP_URL;
      }})
      .catch(err => {{
        console.error("Lỗi:", err);
        window.location.href = ZALO_GROUP_URL;
      }});
    }});
  }});
</script>
</body>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Chèn tự động ngay trước thẻ đóng </body>
if "const GOOGLE_SCRIPT_URL" not in content:
    content = content.replace("</body>", script_code)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Đã tự động gắn mã Form Google Sheet và Zalo vào index.html thành công!")
else:
    print("Mã script đã tồn tại trong file index.html từ trước!")
```[cite: 1]

---

**Các bước thực hiện tiếp theo:**

1. Copy toàn bộ đoạn mã trên, dán đè vào file `add_form_script.py` rồi nhấn **Ctrl + S**.
2. Mở Terminal trong VS Code và chạy lệnh:
   ```bash
   python add_form_script.py
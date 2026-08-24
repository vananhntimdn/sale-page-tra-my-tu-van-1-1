GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxTGbfSSCh8SpAyz49HBBD1uG12ukQVWrrNBjuBUvENq2e9Z4KjGwOlqstmIQ6X1xiUog/exec"
ZALO_GROUP_URL = "https://zalo.me/g/vh6vyxjcvobu3zgdihub"

new_script = f"""
<script>
(function() {{
  const GOOGLE_SCRIPT_URL = "{GOOGLE_SCRIPT_URL}";
  const ZALO_GROUP_URL = "{ZALO_GROUP_URL}";

  function sendDataAndRedirect(form) {{
    const nameInput = form.querySelector('input[name="name"]');
    const phoneInput = form.querySelector('input[name="phone"]');
    const msgInput = form.querySelector('textarea[name="message"], input[name="message"]');

    const name = nameInput ? nameInput.value : '';
    const phone = phoneInput ? phoneInput.value : '';
    const message = msgInput ? msgInput.value : '';

    const url = GOOGLE_SCRIPT_URL + '?name=' + encodeURIComponent(name) + '&phone=' + encodeURIComponent(phone) + '&message=' + encodeURIComponent(message);

    // Gửi ngầm qua Image Beacon để đảm bảo Google nhận 100% trước khi chuyển trang
    const img = new Image();
    img.src = url;

    setTimeout(() => {{
      window.location.href = ZALO_GROUP_URL;
    }}, 600);
  }}

  document.querySelectorAll("form.ladi-form").forEach(form => {{
    form.addEventListener("submit", function(e) {{
      e.preventDefault();
      sendDataAndRedirect(form);
    }});
    
    // Bắt thêm sự kiện click nút bấm phòng trường hợp form bị chặn submit
    const btn = form.querySelector('.ladi-button');
    if (btn) {{
      btn.addEventListener('click', function(e) {{
        const phone = form.querySelector('input[name="phone"]');
        if (phone && phone.value.trim() !== '') {{
          sendDataAndRedirect(form);
        }}
      }});
    }}
  }});
}})();
</script>
</body>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Xóa đoạn script cũ nếu có và chèn script mới
import re
content = re.sub(r'<script>[\s\S]*?const GOOGLE_SCRIPT_URL[\s\S]*?</script>\s*</body>', '</body>', content)
content = content.replace("</body>", new_script)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Đã cập nhật cơ chế gửi dữ liệu GET/Beacon an toàn tuyệt đối!")
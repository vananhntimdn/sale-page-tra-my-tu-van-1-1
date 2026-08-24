import re

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxTGbfSSCh8SpAyz49HBBD1uG12ukQVWrrNBjuBUvENq2e9Z4KjGwOlqstmIQ6X1xiUog/exec"
ZALO_GROUP_URL = "https://zalo.me/g/vh6vyxjcvobu3zgdihub"

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("https://zalo.me/g/sunykh682", "")

content = re.sub(r'<script id="sheet_sync_script">[\s\S]*?</script>', '', content)
content = re.sub(r'<script>[\s\S]*?const GOOGLE_SCRIPT_URL[\s\S]*?</script>', '', content)

sync_script = f"""
<script id="sheet_sync_script">
(function() {{
  const SCRIPT_URL = "{GOOGLE_SCRIPT_URL}";
  const REDIRECT_URL = "{ZALO_GROUP_URL}";

  function sendData(form) {{
    const nameEl = form.querySelector('input[name="name"]');
    const phoneEl = form.querySelector('input[name="phone"]');
    const msgEl = form.querySelector('textarea[name="message"], input[name="message"]');

    const name = nameEl ? nameEl.value.trim() : '';
    const phone = phoneEl ? phoneEl.value.trim() : '';
    const message = msgEl ? msgEl.value.trim() : '';

    if (phone) {{
      const query = "?name=" + encodeURIComponent(name) + 
                    "&phone=" + encodeURIComponent(phone) + 
                    "&message=" + encodeURIComponent(message);
      
      const img = new Image();
      img.src = SCRIPT_URL + query;
    }}

    setTimeout(function() {{
      window.location.href = REDIRECT_URL;
    }}, 600);
  }}

  document.addEventListener("DOMContentLoaded", function() {{
    document.querySelectorAll("form.ladi-form").forEach(function(form) {{
      form.addEventListener("submit", function(e) {{
        e.preventDefault();
        sendData(form);
      }});
      
      const btn = form.querySelector(".ladi-button");
      if (btn) {{
        btn.addEventListener("click", function() {{
          const phoneInput = form.querySelector('input[name="phone"]');
          if (phoneInput && phoneInput.value.trim() !== "") {{
            sendData(form);
          }}
        }});
      }}
    }});
  }});
}})();
</script>
</body>
"""

content = content.replace("</body>", sync_script)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Hoan tat cap nhat index.html")
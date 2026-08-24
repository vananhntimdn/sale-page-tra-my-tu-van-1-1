import os

mapping = {
    # 1. SECTION HERO
    "https://w.ladicdn.com/s1440x733/5ea845b95da1a2557f302daa/bia-intro-hngd1-20240913083806-3gfi0.jpg": "./images/hero-bg.webp",
    "https://w.ladicdn.com/s768x939/5ea845b95da1a2557f302daa/bia-intro-hngd1-20240913083806-3gfi0.jpg": "./images/hero-bg-mobile.webp",
    "https://w.ladicdn.com/s750x1250/5ea845b95da1a2557f302daa/bia-intro-nho-20240918110726-br1mc.png": "./images/hero-portrait-small.webp",
    "https://w.ladicdn.com/s800x900/6751413d1292e600120ef66e/2908-20250829093045-tumw-.png": "./images/quiz-girl.webp",
    "https://w.ladicdn.com/s650x700/6751413d1292e600120ef66e/2908-20250829093045-tumw-.png": "./images/quiz-girl.webp",
    "https://w.ladicdn.com/s1000x800/5c7362c6c417ab07e5196b05/layer-1-20200724095832.png": "./images/layer.webp",
    "https://w.ladicdn.com/s800x650/5c7362c6c417ab07e5196b05/layer-1-20200724095832.png": "./images/layer.webp",
    "https://w.ladicdn.com/s550x550/5ea845b95da1a2557f302daa/tim3-20240913085130-lfrsp.png": "./images/tim3.webp",
    "https://w.ladicdn.com/s600x600/5ea845b95da1a2557f302daa/tim3-20240913085130-lfrsp.png": "./images/tim3.webp",
    "https://w.ladicdn.com/s500x500/5ea845b95da1a2557f302daa/tim3-20240913085130-lfrsp.png": "./images/tim3.webp",
    "https://w.ladicdn.com/5ea845b95da1a2557f302daa/tim2-20240918093033-bxxgv.png": "./images/tim2.webp",
    "https://w.ladicdn.com/5ea845b95da1a2557f302daa/tim2-20240913084430-sigwq.png": "./images/tim2.webp",

    # 2. SECTION CÓ PHẢI (SECTION 87)
    "https://w.ladicdn.com/s650x650/5ea845b95da1a2557f302daa/gil-20240916085622-9iplj.png": "./images/story-portrait.webp",
    "https://w.ladicdn.com/s600x600/5ea845b95da1a2557f302daa/gil-20240916085622-9iplj.png": "./images/story-portrait.webp",
    "https://w.ladicdn.com/s600x550/5ea845b95da1a2557f302daa/a1-20240918094340-erx8w.jpg": "./images/quiz-photo-1.webp",
    "https://w.ladicdn.com/s700x450/5ea845b95da1a2557f302daa/a1-20240918094340-erx8w.jpg": "./images/quiz-photo-1.webp",
    "https://w.ladicdn.com/s600x550/5ea845b95da1a2557f302daa/a2-compressed-20240918094340-ccy-z.jpg": "./images/quiz-photo-2.webp",
    "https://w.ladicdn.com/s700x450/5ea845b95da1a2557f302daa/a2-compressed-20240918094340-ccy-z.jpg": "./images/quiz-photo-2.webp",
    "https://w.ladicdn.com/s600x550/5ea845b95da1a2557f302daa/a3-compressed-20240918094340-ytx4q.jpg": "./images/quiz-photo-3.webp",
    "https://w.ladicdn.com/s700x450/5ea845b95da1a2557f302daa/a3-compressed-20240918094340-ytx4q.jpg": "./images/quiz-photo-3.webp",
    "https://w.ladicdn.com/s600x550/5ea845b95da1a2557f302daa/a4-compressed-20240918094340-8iyvy.jpg": "./images/quiz-photo-4.webp",
    "https://w.ladicdn.com/s700x450/5ea845b95da1a2557f302daa/a4-compressed-20240918094340-8iyvy.jpg": "./images/quiz-photo-4.webp",
    "https://w.ladicdn.com/s600x550/5ea845b95da1a2557f302daa/a5-compressed-20240918094340-tjiky.jpg": "./images/quiz-photo-5.webp",
    "https://w.ladicdn.com/s700x500/5ea845b95da1a2557f302daa/a5-compressed-20240918094340-tjiky.jpg": "./images/quiz-photo-5.webp",

    # 3. SECTION QUYỀN LỢI (SECTION 11)
    "https://w.ladicdn.com/s800x750/5ea845b95da1a2557f302daa/cbnmm-20240918095745-wpqoh.jpg": "./images/benefit-photo-1.webp",
    "https://w.ladicdn.com/s700x700/5ea845b95da1a2557f302daa/cbnmm-20240918095745-wpqoh.jpg": "./images/benefit-photo-1.webp",
    "https://w.ladicdn.com/s800x800/5ea845b95da1a2557f302daa/hj-20240918095745-qwxr1.jpg": "./images/benefit-photo-2.webp",
    "https://w.ladicdn.com/s700x700/5ea845b95da1a2557f302daa/hj-20240918095745-qwxr1.jpg": "./images/benefit-photo-2.webp",
    "https://w.ladicdn.com/s800x800/5ea845b95da1a2557f302daa/22-20240917185201-vfg-u.jpg": "./images/benefit-photo-3.webp",
    "https://w.ladicdn.com/s700x700/5ea845b95da1a2557f302daa/22-20240917185201-vfg-u.jpg": "./images/benefit-photo-3.webp",

    # 4. SECTION CÂU CHUYỆN TRÀ MY (SECTION 210)
    "https://w.ladicdn.com/s850x950/5ea845b95da1a2557f302daa/tra-my4-20240918103620-gstmy.png": "./images/story-portrait.webp",
    "https://w.ladicdn.com/s600x650/5ea845b95da1a2557f302daa/tra-my4-20240918103620-gstmy.png": "./images/story-portrait.webp",
    "https://w.ladicdn.com/s750x800/5ea845b95da1a2557f302daa/tra-my2-20240918103620-4rxrg.png": "./images/story-inline-1.webp",
    "https://w.ladicdn.com/s650x700/5ea845b95da1a2557f302daa/tra-my2-20240918103620-4rxrg.png": "./images/story-inline-1.webp",
    "https://w.ladicdn.com/s750x800/5ea845b95da1a2557f302daa/tra-my1-20240918103620-9-1h1.png": "./images/story-inline-2.webp",
    "https://w.ladicdn.com/s600x650/5ea845b95da1a2557f302daa/tra-my1-20240918103620-9-1h1.png": "./images/story-inline-2.webp",
    "https://w.ladicdn.com/s750x800/5ea845b95da1a2557f302daa/tra-my-20240918103620-h2fub.png": "./images/story-inline-3.webp",
    "https://w.ladicdn.com/s600x650/5ea845b95da1a2557f302daa/tra-my-20240918103620-h2fub.png": "./images/story-inline-3.webp",

    # 5. SECTION FEEDBACK (SECTION 516)
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/1-20241001072902-qb199.jpg": "./images/gallery-01.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/2-20241001072902-a72uh.jpg": "./images/gallery-02.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/3-20241001072902-kpmlt.jpg": "./images/gallery-03.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/4-20241001072902-fvkk8.jpg": "./images/gallery-04.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/10-20241205061045-p2u0_.png": "./images/gallery-05.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/6-20241205061044-lmd75.png": "./images/gallery-06.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/7-20241205061044-vvxin.png": "./images/gallery-07.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/8-20241205061045-ahpo0.png": "./images/gallery-08.webp",
    "https://w.ladicdn.com/s650x1000/5ea845b95da1a2557f302daa/9-20241205061045-csqko.png": "./images/gallery-09.webp",

    # 6. NỀN & FORM CUỐI TRANG
    "https://w.ladicdn.com/s1440x617/5ea845b95da1a2557f302daa/b-compressed-20241001043552-impko.jpg": "./images/section-bg-final.webp",
    "https://w.ladicdn.com/s768x737/5ea845b95da1a2557f302daa/b-compressed-20241001043552-impko.jpg": "./images/section-bg-final-mobile.webp",
    "https://w.ladicdn.com/s750x1250/5ea845b95da1a2557f302daa/b2-compressed-20241001044142-h7u9m.jpg": "./images/story-portrait.webp",
    "https://w.ladicdn.com/s1440x920/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s768x1177/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s1440x580/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s768x575/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s1440x2564/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s768x3695/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s1440x749/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s768x760/5ea845b95da1a2557f302daa/nen-thay-2509-20240925024522-lvg8r.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s1440x875/5ea845b95da1a2557f302daa/bg-20240917183738-qevkv.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s768x1316/5ea845b95da1a2557f302daa/bg-20240917183738-qevkv.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s1440x1579/5c7362c6c417ab07e5196b05/--20200724093150.jpg": "./images/section-bg-texture.webp",
    "https://w.ladicdn.com/s768x2123/5c7362c6c417ab07e5196b05/--20200724093150.jpg": "./images/section-bg-texture.webp",

    # 7. META & FAVICON
    "https://static.ladipage.net/6751413d1292e600120ef66e/thumbnail-tu-van-11-compressed-20250829092242-7eas1.jpg": "./images/story-portrait.webp",
    "https://static.ladipage.net/6751413d1292e600120ef66e/favicon-tv-20250829092354-gn_av.png": "./images/favicon.webp"
}

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

count = 0
for old_url, new_url in mapping.items():
    if old_url in content:
        content = content.replace(old_url, new_url)
        count += 1

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Hoan tat! Da thay the thanh cong {count} vi tri anh.")
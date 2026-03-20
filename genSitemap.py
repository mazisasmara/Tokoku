import os
from datetime import date

folder = "./"  # path ke folder Tokoku
today = date.today().isoformat()

cities = [d for d in os.listdir(folder) if d.startswith("jasa-pembuatan-website-")]

sitemap_header = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''

sitemap_footer = '</urlset>'

# Halaman utama & section
urls = [
    {"loc": "https://azisdev.my.id/", "freq": "weekly", "priority": "1.0"},
    {"loc": "https://azisdev.my.id/#services", "freq": "monthly", "priority": "0.8"},
    {"loc": "https://azisdev.my.id/#pricing", "freq": "monthly", "priority": "0.9"},
    {"loc": "https://azisdev.my.id/#why", "freq": "monthly", "priority": "0.7"},
    {"loc": "https://azisdev.my.id/#faq", "freq": "monthly", "priority": "0.8"},
    {"loc": "https://azisdev.my.id/#contact", "freq": "monthly", "priority": "0.7"},
]

# Generate URL kota
for city in cities:
    urls.append({
        "loc": f"https://azisdev.my.id/{city}/",
        "freq": "monthly",
        "priority": "0.9"
    })

# Tulis sitemap.xml
with open("sitemap.xml", "w") as f:
    f.write(sitemap_header)
    for u in urls:
        f.write(f'''  <url>
    <loc>{u["loc"]}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{u["freq"]}</changefreq>
    <priority>{u["priority"]}</priority>
  </url>\n''')
    f.write(sitemap_footer)

print("sitemap.xml updated!")
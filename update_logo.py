import os
import re
import glob

# The new SVG for the logo
new_svg = """<svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 8px;">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="var(--brand-accent)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

# The new favicon
new_favicon = """<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg width='32' height='32' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z' stroke='%23E63946' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3Cpath d='M9 12l2 2 4-4' stroke='%23111827' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">"""

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace SVG logo (matching precisely while ignoring indentation differences)
    # The SVG starts with <svg width="32" and ends with </svg>
    svg_pattern = re.compile(r'<svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style="margin-right: 8px;">.*?</svg>', re.DOTALL)
    
    # We only want to replace the SVG inside the logo anchors, but since all these SVGs in the file are the logo, it's safe.
    content = svg_pattern.sub(new_svg, content)

    # Replace favicon
    # Matching the exact old favicon or any <link rel="icon" type="image/svg+xml"...
    favicon_pattern = re.compile(r'<link rel="icon" type="image/svg\+xml" href="data:image/svg\+xml,[^"]+">')
    content = favicon_pattern.sub(new_favicon, content)
    
    # Also fix the text if needed (the text is already Auto <span>Fix</span>, but let's make sure it's bold and styled correctly if needed, actually it's fine as is)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Successfully updated logo and favicon in {len(html_files)} HTML files.")

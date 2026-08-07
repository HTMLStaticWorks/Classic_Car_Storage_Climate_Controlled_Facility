import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

pattern = re.compile(
    r'<div[^>]*class="[^"]*mobile-only-actions[^"]*".*?>\s*<button class="icon-btn theme-toggle-btn"[^>]*>\s*<i class="bi bi-moon"></i>\s*</button>\s*<button class="icon-btn rtl-toggle-btn"[^>]*>\s*<i class="bi bi-arrow-left-right"></i>\s*</button>\s*<a href="signup\.html"[^>]*>Sign Up</a>\s*</div>',
    re.DOTALL
)

replacement = """<div class="mobile-only-actions d-xl-none d-flex flex-column gap-3 mt-3 pt-3 border-top border-secondary">
                    <a href="signup.html" class="btn-premium primary w-100 text-center">Sign Up</a>
                    <div class="d-flex gap-3 justify-content-start">
                        <button class="icon-btn theme-toggle-btn" title="Toggle Theme">
                            <i class="bi bi-moon"></i>
                        </button>
                        <button class="icon-btn rtl-toggle-btn" title="Toggle RTL">
                            <i class="bi bi-arrow-left-right"></i>
                        </button>
                    </div>
                </div>"""

for file in html_files:
    if file in ('login.html', 'signup.html'):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")

from __future__ import annotations

import html
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS_PATH = PROJECT_ROOT / "docs"
SITE_PATH = DOCS_PATH / "site"
REFERENCE_MD = DOCS_PATH / "api-reference.md"
REFERENCE_HTML = SITE_PATH / "api-reference.html"
INDEX_HTML = SITE_PATH / "index.html"


def apply_inline_markup(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    html_lines: list[str] = []
    in_code = False
    in_list = False
    paragraph_buffer: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph_buffer
        if paragraph_buffer:
            text = " ".join(part.strip() for part in paragraph_buffer if part.strip())
            html_lines.append(f"<p>{apply_inline_markup(text)}</p>")
            paragraph_buffer = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html_lines.append("</ul>")
            in_list = False

    for line in lines:
        stripped = line.rstrip()
        if stripped.startswith("```"):
            flush_paragraph()
            close_list()
            if not in_code:
                html_lines.append("<pre><code>")
                in_code = True
            else:
                html_lines.append("</code></pre>")
                in_code = False
            continue

        if in_code:
            html_lines.append(html.escape(stripped))
            continue

        if not stripped:
            flush_paragraph()
            close_list()
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            close_list()
            html_lines.append(f"<h3>{apply_inline_markup(stripped[4:])}</h3>")
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            close_list()
            html_lines.append(f"<h2>{apply_inline_markup(stripped[3:])}</h2>")
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            close_list()
            html_lines.append(f"<h1>{apply_inline_markup(stripped[2:])}</h1>")
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{apply_inline_markup(stripped[2:])}</li>")
            continue

        paragraph_buffer.append(stripped)

    flush_paragraph()
    close_list()
    return "\n".join(html_lines)


def build_page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)}</title>
    <style>
      :root {{
        color-scheme: light;
        --bg: #f6f7f3;
        --card: #ffffff;
        --text: #182025;
        --muted: #5f6b73;
        --accent: #0e7490;
        --border: #d7dde1;
        --code-bg: #eef2f4;
      }}
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: linear-gradient(180deg, #eef3f1 0%, var(--bg) 100%);
        color: var(--text);
      }}
      .page {{
        max-width: 1100px;
        margin: 0 auto;
        padding: 32px 20px 64px;
      }}
      .card {{
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 20px;
        box-shadow: 0 12px 40px rgba(24, 32, 37, 0.06);
        padding: 28px;
      }}
      .nav {{
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
        margin-bottom: 20px;
      }}
      .nav a {{
        color: var(--accent);
        text-decoration: none;
        font-weight: 600;
      }}
      h1, h2, h3 {{
        line-height: 1.2;
      }}
      h1 {{ margin-top: 0; font-size: 2rem; }}
      h2 {{
        margin-top: 2.4rem;
        padding-top: 1rem;
        border-top: 1px solid var(--border);
      }}
      p, li {{
        color: var(--text);
        line-height: 1.65;
      }}
      ul {{
        padding-left: 1.2rem;
      }}
      code {{
        background: var(--code-bg);
        padding: 0.15rem 0.35rem;
        border-radius: 6px;
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      }}
      pre {{
        background: var(--code-bg);
        padding: 16px;
        overflow-x: auto;
        border-radius: 12px;
        border: 1px solid var(--border);
      }}
      pre code {{
        background: transparent;
        padding: 0;
      }}
      .muted {{
        color: var(--muted);
      }}
    </style>
  </head>
  <body>
    <div class="page">
      <div class="nav">
        <a href="./index.html">Главная</a>
        <a href="./api-reference.html">API Reference</a>
      </div>
      <div class="card">
        {body}
      </div>
    </div>
  </body>
</html>
"""


def build_index_page() -> str:
    body = """
<h1>APIClient OPTI24 Docs</h1>
<p class="muted">Статическая документация SDK, публикуемая через GitHub Pages.</p>
<ul>
  <li><a href="./api-reference.html">API Reference</a></li>
  <li><a href="https://github.com/raspopovaa/APIforCards">GitHub repository</a></li>
  <li><a href="https://github.com/raspopovaa/APIforCards/blob/main/README.md">README</a></li>
</ul>
<p>Сайт собирается автоматически из локальной документации и introspection-данных SDK.</p>
"""
    return build_page("APIClient OPTI24 Docs", body)


def main() -> None:
    SITE_PATH.mkdir(parents=True, exist_ok=True)
    reference_markdown = REFERENCE_MD.read_text(encoding="utf-8")
    reference_body = markdown_to_html(reference_markdown)
    REFERENCE_HTML.write_text(
        build_page("API Reference", reference_body),
        encoding="utf-8",
    )
    INDEX_HTML.write_text(build_index_page(), encoding="utf-8")
    print(f"Built site in {SITE_PATH}")


if __name__ == "__main__":
    main()

from pathlib import Path
from bs4 import BeautifulSoup


def test_nav_links_match_sections():
    html_path = Path(__file__).resolve().parents[1] / "index.html"
    html_content = html_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_content, "html.parser")

    nav_link_ids = [
        a["href"].lstrip("#")
        for a in soup.select(".nav-links a[href]")
        if a["href"].startswith("#")
    ]

    section_ids = {
        section["id"]
        for section in soup.find_all("section")
        if section.has_attr("id")
    }

    assert nav_link_ids, "No navigation links found"
    for link_id in nav_link_ids:
        assert link_id in section_ids, f"href '#{link_id}' does not match any section id"


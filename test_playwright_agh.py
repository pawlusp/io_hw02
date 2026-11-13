"""Test suite for the AGH University of Science and Technology website using Playwright."""
import re
from playwright.sync_api import expect, Page

AGH_PAGE = "https://www.informatyka.agh.edu.pl/pl/"
def test_agh_page(page: Page):
    """Check that the AGH page loads successfully."""
    response = page.goto(AGH_PAGE)
    assert response is not None and response.ok

def test_owydziale(page: Page):
    """Check that the 'O Wydziale' page is loaded and check heading."""
    page.goto(AGH_PAGE)
    page.get_by_role("link", name="Wydział", exact=True).hover()
    # Przejście do strony dotyczącej Wydziału
    page.get_by_role("link", name="O Wydziale").click()

    # Sprawdzenie, czy nagłówek jest widoczny
    expect(
        page.get_by_role("heading", name="O Wydziale")
    ).to_be_visible()

def test_naszekierunki(page: Page):
    """Check that the 'Nasze kierunki' page is loaded and check if correct headings are visible."""
    page.goto(AGH_PAGE)
    page.get_by_role("link", name="Nasze kierunki").click()

    expect(
        page.get_by_role("heading", name="Nasze kierunki", level=1)
        ).to_be_visible()
    expect(
        page.get_by_role("heading", name="Tworzenie przestrzeni wirtualnych i gier")
        ).to_be_visible()

def test_url_redirect(page: Page):
    """Check that the URL redirects correctly when navigating to 'Tworzenie przestrzeni'."""
    page.goto(AGH_PAGE)
    page.get_by_role("link", name="Nasze kierunki").click()
    page.get_by_role("link", name="Tworzenie przestrzeni").click()

    expect(
        page).to_have_url(re.compile(r".*tworzenie-przestrzeni-wirtualnych-i-gier.*"))

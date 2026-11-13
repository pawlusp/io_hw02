"""Playwright tests for the AGH website."""
from playwright.sync_api import Page

def test_open_agh_website(page: Page):
    """Verify that the AGH website opens"""
    page.goto("https://www.informatyka.agh.edu.pl/pl/")

    print(page.title())

    assert page.title() != ""

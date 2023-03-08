from selene import browser
from selene import be, have


def test_google_search_positive(browser_config, browser_open_url):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_negative(browser_config, browser_open_url):
    browser.element('[name="q"]').should(be.blank).type('dshfjkahsdjfasdlkfjkdlsjfklasjflasdjflk').press_enter()
    browser.element('.card-section').should(have.text('По запросу dshfjkahsdjfasdlkfjkdlsjfklasjflasdjflk ничего не найдено.'))

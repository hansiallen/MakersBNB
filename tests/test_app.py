from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")

"""
display all of the bookings
"""
def test_get_list_spaces_page(page, test_web_address,db_connection):
    db_connection.seed("seeds/users.sql")
    db_connection.seed("seeds/spaces.sql")
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")
    page.screenshot(path= 'screenshot.png')
    # We look at the a specific class tag
    p_tag = page.get_by_role("listing-card").count()

    # We assert that it has the text "This is the homepage."
    assert p_tag ==3
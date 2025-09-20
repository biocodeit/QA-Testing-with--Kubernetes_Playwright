import os
import glob
from playwright.sync_api import  expect, Page

# Your list of local SVG files
svgs = glob.glob(os.path.join('../amino-guesser/assets/svg/','*.svg'))




def test_check_svg(page) -> None:
    page.goto("http://app-service:80")

    # Click the next button once to start the game
    page.get_by_role("button", name="next").click()
    
    # Check the svgs
    count = 0
    for svg in svgs:
        # Get the image element and its src attribute
        image = page.get_by_role("img")
        src = image.get_attribute('src')
        print(f'Found image with src: {src}')
        count += 1
        page.locator("img").screenshot(path=f"svg_tests/{count}.png")
        # Click the next button to load the next image for the next loop iteration
        page.get_by_role("button", name="next").click()


        print(f'Total amino acids should be 20, and we got [{count}]')
        expect(page.get_by_role("button", name="next")).to_have_css('background-color','rgb(5, 128, 9)')
    
def test_answer(page):
    page.goto("http://app-service:80")
    page.get_by_role("button", name="next").click()
    option_button=page.locator("#ThreeOP2")
    expect(option_button).to_have_css("background-color","rgb(37, 99, 235)")
    option_button.click()
    expect(option_button).not_to_have_css("background-color","rgb(37, 99, 235)")

def test_next_button(page):
    page.goto("http://app-service:80")
    next_button=page.get_by_role("button", name="next")
    amino_name_box = page.locator("#box3")
    amino_svg_box = page.locator("img")
    next_button.click()
    amino_nameB4=amino_name_box.text_content()
    amino_svgB4 = amino_svg_box.get_attribute("src")
    next_button.click()
    expect(amino_name_box).not_to_contain_text(amino_nameB4, use_inner_text=True)
    expect(amino_svg_box).not_to_have_attribute("src", amino_svgB4)
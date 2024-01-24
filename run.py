import asyncio
from playwright.async_api import async_playwright
import pdfkit
import re


async def scrape_textbook_runner(username, password, textbook_name, num_pages):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://www.cengage.com/')
        await asyncio.sleep(3)
        await page.mouse.click(1150, 50)
        await asyncio.sleep(2)
        await page.fill('input[name="username"]', username)
        await page.click('input[value="NEXT"]')
        await asyncio.sleep(3)
        await page.fill('input[name="password"]', password)
        await page.click('input[value="SIGN IN"]')
        await asyncio.sleep(3)
        def handle_new_page(new_page):
            return new_page
        context.on('page', handle_new_page)
        await page.click(f'text="{textbook_name}"')
        new_page = await context.wait_for_event('page')
        await new_page.set_viewport_size({"width": 800, "height": 800})
        await asyncio.sleep(1)
        await new_page.click('text="menu_open"')
        await asyncio.sleep(10)
        print('scraping content...')
        html_content = ""
        for _ in range(num_pages):
            iframe_selector = await new_page.query_selector('iframe')
            frame = await iframe_selector.content_frame()
            await frame.evaluate('''() => {
			const summaryElements = document.querySelectorAll('details');
			summaryElements.forEach((summary) => {
				summary.setAttribute('open', 'open');
			});
		    }''')
            html = await frame.content()
            
            # Extract absolute image URLs
            image_elements = await frame.query_selector_all('img')
            image_urls = [await frame.evaluate('(element) => element.src', img) for img in image_elements]

            print("Extracted image URLs:")
            for url in image_urls:
                print(url)

            # Replace the src attributes in HTML content with the extracted URLs
            for url in image_urls:
                pattern = r'src=".*?"'
                replacement = f'src="{url}"'
                html = re.sub(pattern, replacement, html, count=1)
            
            html_content += html
            await new_page.mouse.click(760, 760)
            await asyncio.sleep(1)

        cookies = await context.cookies()
        print('scraping successful...')
        print('converting to compiled html to a pdf...')

        cookie_string = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
        options = {
            'custom-header': [
                ('Cookie', cookie_string)
            ],
            'no-outline': None
        }
        pdfkit.from_string(html_content, 'output.pdf', options=options)
        
        await browser.close()
        print('textbook is ready!')


asyncio.run(scrape_textbook_runner(username='', password='', textbook_name='eTextbook: Introduction to Algorithms and Data Structures', num_pages=10))

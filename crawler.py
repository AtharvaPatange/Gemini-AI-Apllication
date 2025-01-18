from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-49afb5fa3b1e48d2bfd3b9ae65667478")

# Crawl a website:
crawl_status = app.crawl_url(
  'https://pune.gov.in/gallery/jalshakti', 
  params={
    'limit': 100, 
   'scrapeOptions' : {
    "formats": ["rawHtml"],        # Desired output format: "markdown", "html", "rawHtml", "links", "screenshot"
    "includeTags": ["p"],          # Include only <p> tags to extract text
    "excludeTags": ["script", "style"],  # Exclude unnecessary tags like <script>, <style>
    "waitFor": 2000,               # Optional: Wait for 2 seconds for dynamic content
    "timeout": 5000                # Optional: Timeout after 5 seconds
}
  },
  poll_interval=30
)
print(crawl_status)


# {'success': True, 'status': 'completed', 'completed': 1, 'total': 1, 'creditsUsed': 1, 'expiresAt': '2025-01-15T11:03:37.000Z', 'data': [{'html': '<!DOCTYPE html><html lang="en" class="dark">\n  <body>\n    <div id="root"><div class="flex justify-center items-center h-screen bg-gray-900"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-loader-circle h-8 w-8 animate-spin text-[#ff7700]"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg></div></div>\n  \n\n</body></html>', 'markdown': '', 'metadata': {'url': 'https://www.chaicode.com/ch/dashboard', 'title': 'Chai Code', 'favicon': 'https://www.chaicode.com/images/cup-logo.svg', 'language': 'en', 'scrapeId': 'c75b168e-4836-441c-8bdf-3c2a569c8ba6', 'viewport': 'width=device-width, initial-scale=1.0', 'sourceURL': 'https://www.chaicode.com/ch/dashboard', 'statusCode': 200, 'ogLocaleAlternate': []}}]

# crawl_status = app.check_crawl_status("c75b168e-4836-441c-8bdf-3c2a569c8ba6")
# print(crawl_status)

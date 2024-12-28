from playwright.sync_api import sync_playwright
import html2text
import time
import os
from urllib.parse import urljoin
from collections import deque
import re
import json
import logging

logger = logging.getLogger(__name__)

class AmazonHelpCrawler:
    def __init__(self, mode='dev', dev_page_limit=2):
        """
        Initialize crawler with mode and page limit
        Args:
            mode (str): 'dev' or 'prod' - controls whether to limit page crawling
            dev_page_limit (int): number of pages to crawl in dev mode
        """
        self.playwright = sync_playwright().start()
        
        # Directory to store browser user data
        self.user_data_dir = "browser_data"
        if not os.path.exists(self.user_data_dir):
            os.makedirs(self.user_data_dir)
        
        # Launch browser with persistent context
        self.browser = self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,
            headless=False
        )
        self.page = self.browser.new_page()
        
        self.mode = mode.lower()
        self.dev_page_limit = dev_page_limit
        
        self.visited_urls = set()
        self.base_url = "https://sellercentral.amazon.com/help/hub/reference/G2"
        self.converter = html2text.HTML2Text()
        self.converter.ignore_links = False
        
        # XPath and CSS selectors for content
        self.content_selectors = {
            'main_page': "//div[@class='kat-col-md-9']//div[@id='hh-full-page-help-home-page']",
            'article_page': "div.help-content-with-scroll-to-top",
            'help_content': "div.help-content"
        }
        
        # Create output directory if it doesn't exist
        self.output_dir = "amazon_help_pages_us_prod"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
        print(f"Crawler initialized in {self.mode.upper()} mode" + 
              (f" (limit: {self.dev_page_limit} pages)" if self.mode == 'dev' else ""))

    def login(self):
        """Handle Amazon Seller Central login"""
        # First check if we're already logged in
        self.page.goto(self.base_url)
        
        try:
            # Wait for main content - if it loads, we're logged in
            self.page.wait_for_selector(self.content_selectors['main_page'], timeout=5000)
            print("Already logged in!")
            return
        except:
            print("Need to login...")
        
        # If not logged in, proceed with login
        print("Please login manually...")
        input("Press Enter once you've logged in...")
        
        # Force navigate back to base URL after login
        print("Navigating back to main help page...")
        self.page.goto(self.base_url)
        
        # Wait for the main content to load
        try:
            self.page.wait_for_selector(self.content_selectors['main_page'], timeout=10000)
            print("Successfully loaded main help page")
        except Exception as e:
            print("Warning: Main page content not loaded as expected. Continuing anyway...")

    def save_to_markdown(self, title: str, content: str, url: str):
        """Save content to a markdown file in a hierarchical structure."""
        try:
            # Extract section from URL path
            url_path = url.split('reference/')[-1] if 'reference/' in url else ''
            
            # Map common URL patterns to sections
            section_mapping = {
                'G200141': 'Get started with Fulfillment by Amazon FBA',
                'G201030': 'Get started with Fulfillment by Amazon FBA',
                'G201812': 'Seller Flex and Alternative Fulfillment',
                'G37HSK': 'Service and Delivery Management',
                # Add more mappings based on URL patterns
            }
            
            # Determine section based on URL pattern
            section = None
            for pattern, section_name in section_mapping.items():
                if url_path.startswith(pattern):
                    section = section_name
                    break
            
            # Default section if no match found
            if not section:
                section = "General Documentation"
            
            # Create section directory if it doesn't exist
            section_dir = os.path.join(self.output_dir, section)
            os.makedirs(section_dir, exist_ok=True)
            
            # Create safe filename
            safe_title = "".join(x for x in title if x.isalnum() or x in (' ', '-', '_')).rstrip()
            filename = f"{safe_title}.md"
            filepath = os.path.join(section_dir, filename)
            
            # Add metadata to content
            metadata = f"""---
title: {title}
url: {url}
section: {section}
---

"""
            # Write to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(metadata + content)
            
            logger.info(f"Saved {url} to {filepath}")
            
            # Update document summaries
            if not hasattr(self, 'document_summaries'):
                self.document_summaries = {'documents': {}}
            
            self.document_summaries['documents'][filepath] = {
                'name': title,
                'url': url,
                'section': section
            }
            
            # Save document summaries
            summaries_path = os.path.join(self.output_dir, 'document_summaries.json')
            with open(summaries_path, 'w', encoding='utf-8') as f:
                json.dump(self.document_summaries, f, indent=2)
            
        except Exception as e:
            logger.error(f"Error saving {url}: {str(e)}")

    def is_valid_help_link(self, href):
        """Check if the link is a valid help page link and extract the ID"""
        # Match patterns like G200421970 at the end of URLs
        id_pattern = r'[A-Z][A-Z0-9]+$'
        
        if href:
            # Extract the last part of the URL path
            parts = href.rstrip('/').split('/')
            if parts:
                potential_id = parts[-1]
                if re.match(id_pattern, potential_id):
                    return True
        return False

    def extract_help_links(self, content_div):
        """Extract all valid help links from the content"""
        links = []
        seen_ids = set()  # Track IDs we've seen to avoid duplicates
        
        try:
            # Find all links in both help content and simple links
            all_links = content_div.query_selector_all("a")
            
            for link in all_links:
                try:
                    href = link.get_attribute('href')
                    if not href:
                        continue
                    
                    # Skip breadcrumb navigation links
                    if link.get_attribute('role') == 'listitem':
                        continue
                    
                    # If it's a valid help link
                    if self.is_valid_help_link(href):
                        # Extract the ID
                        id_part = href.rstrip('/').split('/')[-1]
                        
                        # Skip if we've seen this ID before
                        if id_part in seen_ids:
                            continue
                        
                        seen_ids.add(id_part)
                        
                        # Normalize the URL to a consistent format
                        normalized_url = f"https://sellercentral.amazon.com/help/hub/reference/{id_part}"
                        
                        if normalized_url not in self.visited_urls:
                            links.append(normalized_url)
                except Exception as e:
                    print(f"Error processing link: {str(e)}")
                    continue
            
            return links
        except Exception as e:
            print(f"Error extracting links: {str(e)}")
            return []

    def get_content_and_links(self):
        """Extract content and links from the page"""
        try:
            current_url = self.page.url
            
            # If it's the main help page
            if current_url == self.base_url:
                content_div = self.page.wait_for_selector("xpath=//div[@class='kat-col-md-9']//div[@id='hh-full-page-help-home-page']", timeout=5000)
                if content_div:
                    print("Found main page content")
                    content = content_div.inner_html()
                    links = self.extract_help_links(content_div)
                    return content, links
            
            # For all other pages (article pages)
            else:
                content_div = self.page.wait_for_selector("div.help-content-with-scroll-to-top", timeout=5000)
                if content_div:
                    print("Found article page content")
                    help_content = content_div.query_selector("div#help-content")
                    if help_content:
                        content = help_content.inner_html()
                        links = self.extract_help_links(help_content)
                        return content, links
            
            print("Could not find any content container")
            return None, []
            
        except Exception as e:
            print(f"Error extracting content and links: {str(e)}")
            return None, []

    def process_page(self, url):
        """Process a single page and convert it to markdown"""
        if url in self.visited_urls:
            return []
        
        print(f"Processing: {url}")
        self.visited_urls.add(url)
        
        try:
            self.page.goto(url)
            time.sleep(3)  # Changed from 2 to 3 seconds
            
            # Get the page title - different for main page vs article pages
            if url == self.base_url:
                title = "Amazon"
            else:
                # Try to get the h1 title from the article page
                h1_element = self.page.wait_for_selector("div#full-help-page h1")
                title = h1_element.inner_text() if h1_element else self.page.title()
            
            # Get content and new links
            content, new_urls = self.get_content_and_links()
            
            if content:
                # Convert to markdown
                markdown_content = self.converter.handle(content)
                
                # Save to markdown file
                self.save_to_markdown(title, markdown_content, url)
                print(f"Saved content for: {url}")
            else:
                print(f"No content found for: {url}")
            
            print("New URLs:", new_urls)
            return new_urls
            
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            return []

    def discover_links(self, url, discovered_links=None):
        """
        Recursively discover all links starting from a given URL
        Args:
            url: Starting URL
            discovered_links: Set of all discovered links
        Returns:
            Set of all discovered links
        """
        if discovered_links is None:
            discovered_links = set()
        
        if url in discovered_links:
            return discovered_links
        
        print(f"\nProcessing: {url}")
        
        try:
            self.page.goto(url)
            time.sleep(3)
            
            discovered_links.add(url)
            content, new_urls = self.get_content_and_links()
            
            print(f"Links found on this page: {len(new_urls)}")
            print(f"Total links discovered so far: {len(discovered_links)}")
            
            if content:
                try:
                    if url == self.base_url:
                        title = "Amazon"
                    else:
                        h1_element = self.page.wait_for_selector("div#full-help-page h1")
                        title = h1_element.inner_text() if h1_element else self.page.title()
                    
                    markdown_content = self.converter.handle(content)
                    self.save_to_markdown(title, markdown_content, url)
                    print(f"Saved content for: {url}")
                except Exception as e:
                    print(f"Error saving content for {url}: {str(e)}")
            
            # Recursively discover links from each new URL
            for new_url in new_urls:
                if new_url not in discovered_links:
                    discovered_links.update(self.discover_links(new_url, discovered_links))
            
            return discovered_links
        
        except Exception as e:
            print(f"Error discovering links for {url}: {str(e)}")
            return discovered_links

    def crawl(self):
        """Main crawling function that first discovers all links then processes them"""
        self.login()
        
        print("\nPhase 1: Discovering all links...")
        all_links = self.discover_links(self.base_url)
        print(f"\nDiscovered {len(all_links)} total unique links")
        
        print("\nPhase 2: Processing remaining pages...")
        pages_processed = 0
        
        # Process any remaining pages that weren't saved during discovery
        for url in all_links:
            # Skip if we're in dev mode and hit the limit
            if self.mode == 'dev' and pages_processed >= self.dev_page_limit:
                print(f"\nDEV MODE: Reached limit of {self.dev_page_limit} pages")
                break
            
            # Skip if the file already exists (was saved during discovery)
            if url == self.base_url:
                title = "Amazon"
            else:
                try:
                    self.page.goto(url)
                    h1_element = self.page.wait_for_selector("div#full-help-page h1")
                    title = h1_element.inner_text() if h1_element else self.page.title()
                except:
                    continue
            
            safe_title = "".join(x for x in title if x.isalnum() or x in (' ', '-', '_')).rstrip()
            filename = f"{self.output_dir}/{safe_title}.md"
            
            if os.path.exists(filename):
                print(f"Skipping {url} - already saved")
                continue
            
            # Process and save the page
            new_urls = self.process_page(url)
            pages_processed += 1
            
            # Progress update
            print(f"Pages processed: {pages_processed}" + 
                  (f" of {self.dev_page_limit}" if self.mode == 'dev' else ""))
            
            # Small delay to avoid overwhelming the server
            time.sleep(3)  # Changed from 1 to 3 seconds

    def close(self):
        """Clean up"""
        self.browser.close()
        self.playwright.stop()

def main():
    # You can modify these values when running the script
    mode = 'prod'  # or 'prod'
    dev_page_limit = 5  # only used in dev mode

    # dev mode  
    # crawler = AmazonHelpCrawler(mode=mode, dev_page_limit=dev_page_limit)

    # prod mode
    crawler = AmazonHelpCrawler(mode='prod')
    try:
        crawler.crawl()
    finally:
        crawler.close()
    
    print(f"\nCrawling complete. Visited {len(crawler.visited_urls)} pages.")
    print(f"Pages saved in the '{crawler.output_dir}' directory.")

if __name__ == "__main__":
    main() 
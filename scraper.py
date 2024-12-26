import json
from playwright.sync_api import sync_playwright
import html2text
import os
import logging
import sys
import traceback
import re
import time

class AmazonHelpCrawler:
    def __init__(self, config_file='hello.json', mode='dev'):
        """
        Initialize crawler with JSON config and mode
        Args:
            config_file (str): Path to JSON file with URLs to scrape
            mode (str): 'dev' or 'prod' - controls logging and behavior
        """
        # Setup logging
        logging.basicConfig(
            level=logging.DEBUG,  # Set to DEBUG to get more information
            format='%(asctime)s - %(levelname)s: %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.FileHandler('scraper.log', mode='w')  # 'w' to overwrite log each time
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Initializing AmazonHelpCrawler")
        
        # Load URLs from JSON
        try:
            with open(config_file, 'r') as f:
                self.config_data = json.load(f)
                # Extract URLs from nested structure
                self.urls_to_scrape = []
                for section in self.config_data:
                    if 'subheadings' in section:
                        for subheading in section['subheadings']:
                            if subheading.get('href'):
                                self.urls_to_scrape.append(subheading)
            
            self.logger.info(f"Loaded {len(self.urls_to_scrape)} URLs from {config_file}")
        except FileNotFoundError:
            self.logger.error(f"Config file {config_file} not found!")
            self.urls_to_scrape = []
        except json.JSONDecodeError:
            self.logger.error(f"Invalid JSON in {config_file}")
            self.urls_to_scrape = []
        
        # If no URLs are found, use a default list
        if not self.urls_to_scrape:
            self.logger.warning("No URLs found in config. Using default URLs.")
            self.urls_to_scrape = [
                {"href": "https://example.com"}  # Replace with a public URL
            ]
        
        # Playwright setup
        self.logger.debug("Starting Playwright")
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
    
    def setup_browser(self):
        """
        Set up Playwright browser with explicit error handling
        """
        try:
            self.logger.debug("Launching Playwright")
            self.playwright = sync_playwright().start()
            
            self.logger.debug("Launching browser")
            self.browser = self.playwright.chromium.launch(
                headless=False,  # Keep browser visible for debugging
                slow_mo=500  # Add a 500ms delay between actions
            )
            
            self.logger.debug("Creating browser context")
            self.context = self.browser.new_context()
            
            self.logger.debug("Creating new page")
            self.page = self.context.new_page()
            
            # HTML to Markdown converter
            self.converter = html2text.HTML2Text()
            self.converter.ignore_links = False
            
            # Output directory
            self.output_dir = "amazon_help_pages_markdown"
            os.makedirs(self.output_dir, exist_ok=True)
            
            self.logger.info("Browser setup completed successfully")
        except Exception as e:
            self.logger.error(f"Error setting up browser: {e}")
            self.logger.error(traceback.format_exc())
            raise
    
    def wait_for_login(self, timeout=300):
        """
        Wait for user to complete login
        Args:
            timeout (int): Maximum time to wait for login in seconds
        """
        self.logger.info("Waiting for login... Please complete login in the browser.")
        self.logger.info("After logging in, this script will continue automatically.")
        
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                # Check for a typical logged-in page element
                # This might need adjustment based on the specific site
                self.page.wait_for_selector(
                    "#nav-link-accountList, .logged-in-user, #home-page-container", 
                    state="visible", 
                    timeout=5000
                )
                self.logger.info("Login detected successfully!")
                return True
            except Exception:
                # Not logged in yet, wait a bit
                time.sleep(5)
        
        self.logger.error("Login timeout reached")
        return False
    
    def is_authentication_required(self, url):
        """
        Check if the URL requires authentication
        """
        auth_required_patterns = [
            r'sellercentral\.amazon\.',
            r'seller\.amazon\.',
            r'amazon\.com/seller',
            r'amazon\.in/seller'
        ]
        
        return any(re.search(pattern, url) for pattern in auth_required_patterns)
    
    def scrape_public_page(self, url):
        """
        Scrape a public page
        """
        try:
            self.logger.debug(f"Navigating to public URL: {url}")
            
            # Navigate to the URL with extended timeout
            try:
                response = self.page.goto(url, timeout=30000)  # 30 seconds timeout
                
                # Check response status
                if response and response.status >= 400:
                    self.logger.error(f"HTTP Error {response.status} for {url}")
                    return False
            except Exception as nav_error:
                self.logger.error(f"Navigation error for {url}: {nav_error}")
                return False
            
            # Wait for content to load with more robust method
            try:
                # Wait for body to be present and visible
                self.page.wait_for_selector("body", state="visible", timeout=10000)
                
                # Additional wait to ensure page is fully loaded
                self.page.wait_for_load_state("networkidle", timeout=10000)
            except Exception as wait_error:
                self.logger.error(f"Timeout waiting for content on {url}: {wait_error}")
                return False
            
            # Extract page content with error handling
            try:
                # Try to get main content area, fallback to body
                try:
                    # Try to find a main content selector first
                    content_html = self.page.inner_html("main, #main, .main-content, body")
                except Exception:
                    # Fallback to entire body
                    content_html = self.page.inner_html("body")
                
                # Convert to markdown
                content_markdown = self.converter.handle(content_html)
                
                # Ensure content is not empty
                if not content_markdown.strip():
                    self.logger.warning(f"No content extracted from {url}")
                    return False
            except Exception as content_error:
                self.logger.error(f"Error extracting content from {url}: {content_error}")
                return False
            
            # Generate filename from URL
            try:
                # Use page title or URL to create filename
                try:
                    page_title = self.page.title().strip()
                    # Remove any characters that might cause issues in filenames
                    safe_title = "".join(c for c in page_title if c.isalnum() or c in (' ', '-', '_'))[:50]
                except:
                    # Fallback to URL-based filename
                    safe_title = url.split("/")[-1]
                
                filename = f"{safe_title}.md"
                filepath = os.path.join(self.output_dir, filename)
                
                # Save markdown file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# Source: {url}\n\n{content_markdown}")
                
                self.logger.info(f"Successfully saved {filename}")
                return True
            except Exception as save_error:
                self.logger.error(f"Error saving content for {url}: {save_error}")
                return False
        
        except Exception as e:
            self.logger.error(f"Unexpected error scraping {url}: {e}")
            self.logger.error(traceback.format_exc())
            return False
    
    def run(self, username=None, password=None):
        """
        Run the scraper
        Args:
            username (str, optional): Seller Central username
            password (str, optional): Seller Central password
        """
        # Track scraping results
        total_urls = 0
        successful_scrapes = 0
        failed_scrapes = 0
        skipped_urls = 0
        
        try:
            # Setup browser
            self.setup_browser()
            
            # Scrape specified URLs
            if not self.urls_to_scrape:
                self.logger.warning("No URLs to scrape!")
                return
            
            total_urls = len(self.urls_to_scrape)
            self.logger.info(f"Starting to scrape {total_urls} URLs")
            
            # First, navigate to login page if authentication is required
            login_required = any(self.is_authentication_required(item['href']) for item in self.urls_to_scrape)
            
            if login_required:
                # Navigate to Amazon Seller Central login page
                self.page.goto("https://sellercentral.amazon.in/ap/signin")
                
                # Wait for user to complete login
                login_success = self.wait_for_login()
                
                if not login_success:
                    self.logger.error("Login failed or timed out")
                    return
            
            for item in self.urls_to_scrape:
                if 'href' in item:
                    current_url = item['href']
                    current_text = item.get('text', 'No title')
                    
                    # Add a small delay between page scrapes
                    self.page.wait_for_timeout(1000)  # 1 second delay
                    
                    # Check if URL requires authentication
                    if self.is_authentication_required(current_url):
                        # Log the current URL being scraped
                        self.logger.info(f"Scraping authenticated URL: {current_url} (Title: {current_text})")
                    
                    try:
                        # Scrape the page
                        if self.scrape_public_page(current_url):
                            successful_scrapes += 1
                        else:
                            failed_scrapes += 1
                    except Exception as page_error:
                        failed_scrapes += 1
                        self.logger.error(f"Error scraping {current_url}: {page_error}")
                        # Continue to next URL even if one fails
                        continue
        
        except Exception as e:
            self.logger.error(f"Scraping failed: {e}")
            self.logger.error(traceback.format_exc())
        finally:
            # Provide a summary of scraping results
            self.logger.info(f"Scraping Summary:")
            self.logger.info(f"Total URLs: {total_urls}")
            self.logger.info(f"Successful Scrapes: {successful_scrapes}")
            self.logger.info(f"Failed Scrapes: {failed_scrapes}")
            
            # Cleanup
            self.logger.debug("Starting cleanup process")
            try:
                if self.page:
                    self.page.close()
                if self.context:
                    self.context.close()
                if self.browser:
                    self.browser.close()
                if self.playwright:
                    self.playwright.stop()
                self.logger.info("Cleanup completed successfully")
            except Exception as cleanup_error:
                self.logger.error(f"Error during cleanup: {cleanup_error}")

def main():
    # Allow optional command-line arguments for username and password
    import argparse
    
    parser = argparse.ArgumentParser(description='Amazon Help Page Scraper')
    parser.add_argument('--username', help='Amazon Seller Central Username')
    parser.add_argument('--password', help='Amazon Seller Central Password')
    parser.add_argument('--config', default='hello.json', help='Path to JSON config file')
    
    args = parser.parse_args()
    
    # Catch and log any unhandled exceptions
    try:
        crawler = AmazonHelpCrawler(config_file=args.config)
        crawler.run(username=args.username, password=args.password)
        
        # Add a small pause at the end to keep the script running
        import time
        time.sleep(5)
    except Exception as e:
        logging.error(f"Unhandled exception: {e}")
        logging.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
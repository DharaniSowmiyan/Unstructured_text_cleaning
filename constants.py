# This file contains configuration data, such as lists of words to filter.
#constants.py
NOISE_PATTERNS = [
    # Common boilerplate and navigation
    'home', 'about us', 'contact', 'skip to content', 'main menu',
    'products', 'services', 'solutions', 'portfolio', 'blog', 'news', 'faq',
    'site navigation', 'toggle navigation', 'all rights reserved', 'privacy policy',
    'terms of service', 'terms and conditions', 'cookie policy', 'sitemap',
    'legal notice', 'disclaimer', 'copyright ©', 'powered by', 'designed by',
    'website by',

    # Advertisements & Promotions
    'advertisement', 'sponsored content', 'special promotion', 'limited time offer',
    'buy now', 'shop now', 'discount', 'special offer', 'subscribe to our newsletter',
    'get a free quote', 'request a demo',

    # User Interaction & Social Media
    'reply', 'share this', 'like', 'retweet', 'report post', 'leave a comment',
    'comments', 'login', 'logout', 'register', 'sign in', 'my account',
    'follow us on', 'find us on', 'share on facebook', 'share on twitter',
    'share on linkedin',

    # Forms & Calls to Action
    'submit', 'search', 'enter your email', 'sign up', 'download now',
    'get started', 'learn more', 'read more', 'click here', 'view details',

    # Metadata & Document Info
    'author:', 'date:', 'posted on:', 'last modified:', 'last updated on:',
    'user:', 'posts:', 'page of', 'print this page', 'view pdf', 'by john doe',
    'category:', 'tags:', 'published in',

    # Cookie Banners & Consent
    'this site uses cookies', 'we use cookies', 'to enhance your experience',
    'this website uses cookies', 'by continuing to use this site', 'you agree to our',
    'accept all', 'decline', 'manage settings', 'got it!', 'i agree',

    # Technical & Error Messages
    'javascript seems to be disabled', 'please enable javascript', 'loading...',
    '404 not found', 'page not found', 'error', 'session timed out',
    'pardon our interruption',

    # Forum/Article Specific
    'original post by', 'in reply to', 'related articles', 'you might also like',
    'previous post', 'next post', 'table of contents', 'back to top',
    'was this article helpful?', 'quote | report post',

    # --- NEW: HTML Keywords That Appear as Plain Text ---
    'div', 'class', 'span', 'href', 'html', 'body', 'page', 'internal document'
]
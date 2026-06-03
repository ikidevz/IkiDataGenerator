from urllib.parse import urlencode
from ..base_provider import BaseProvider


class UrlProvider(BaseProvider):
    """
    Generates realistic URLs with optional parts.

    Options:
      protocol     (bool) include http/https prefix    default: True
      host         (bool) include a hostname            default: True
      path         (bool) include a URL path            default: True
      query_string (bool) randomly include query params default: True

    Examples:
      https://facebook.com/blog/latest?utm_source=google
      http://example.org/dashboard
      /api/v2/users?page=3
    """

    _PROTOCOLS = ("http", "https")

    _HOSTS = (
        # Social & Communication
        "facebook.com", "twitter.com", "instagram.com", "linkedin.com",
        "tiktok.com", "snapchat.com", "pinterest.com", "reddit.com",
        "discord.com", "telegram.org", "whatsapp.com", "signal.org",
        "mastodon.social", "threads.net", "tumblr.com", "quora.com",
        # Tech & Dev
        "github.com", "gitlab.com", "bitbucket.org", "stackoverflow.com",
        "openai.com", "anthropic.com", "huggingface.co", "kaggle.com",
        "replit.com", "codepen.io", "codesandbox.io", "vercel.app",
        "netlify.app", "heroku.com", "digitalocean.com", "render.com",
        "railway.app", "fly.io", "supabase.com", "firebase.google.com",
        "aws.amazon.com", "azure.microsoft.com", "cloud.google.com",
        "docker.com", "kubernetes.io", "nginx.org", "apache.org",
        # News & Media
        "cnn.com", "bbc.com", "nytimes.com", "bloomberg.com",
        "reuters.com", "theguardian.com", "washingtonpost.com",
        "forbes.com", "techcrunch.com", "theverge.com", "wired.com",
        "arstechnica.com", "engadget.com", "gizmodo.com", "mashable.com",
        "businessinsider.com", "cnbc.com", "wsj.com", "ft.com",
        # E-commerce & Business
        "amazon.com", "shopify.com", "ebay.com", "etsy.com",
        "aliexpress.com", "walmart.com", "target.com", "bestbuy.com",
        "wayfair.com", "chewy.com", "zappos.com", "overstock.com",
        "salesforce.com", "hubspot.com", "zendesk.com", "intercom.com",
        "stripe.com", "paypal.com", "square.com", "braintree.com",
        # Entertainment & Streaming
        "netflix.com", "spotify.com", "youtube.com", "twitch.tv",
        "hulu.com", "disneyplus.com", "hbomax.com", "primevideo.com",
        "soundcloud.com", "bandcamp.com", "vimeo.com", "dailymotion.com",
        # Productivity & Tools
        "notion.so", "airtable.com", "trello.com", "asana.com",
        "slack.com", "zoom.us", "dropbox.com", "box.com",
        "figma.com", "canva.com", "miro.com", "loom.com",
        "google.com", "apple.com", "microsoft.com", "adobe.com",
        "atlassian.com", "monday.com", "clickup.com", "basecamp.com",
        # Education & Reference
        "wikipedia.org", "medium.com", "substack.com", "coursera.org",
        "udemy.com", "edx.org", "khanacademy.org", "duolingo.com",
        "academia.edu", "researchgate.net", "arxiv.org",
        # Generic / Placeholder
        "example.com", "example.org", "example.net", "mywebsite.net",
        "myblog.com", "mystore.io", "myapp.dev", "testsite.com",
        "wordpress.com", "blogspot.com", "wix.com", "squarespace.com",
    )

    _PATHS = (
        # Root & generic
        "/", "/home", "/index", "/welcome", "/start",
        # Auth
        "/login", "/logout", "/register", "/signup", "/signin",
        "/forgot-password", "/reset-password", "/verify-email",
        "/auth/callback", "/auth/google", "/auth/github",
        "/oauth/authorize", "/oauth/token",
        # User / Account
        "/profile", "/profile/edit", "/profile/avatar",
        "/account", "/account/settings", "/account/billing",
        "/account/security", "/account/notifications",
        "/settings", "/settings/profile", "/settings/privacy",
        "/settings/security", "/settings/integrations",
        "/users", "/users/me", "/users/invite",
        # Dashboard & App
        "/dashboard", "/dashboard/overview", "/dashboard/analytics",
        "/dashboard/reports", "/dashboard/activity",
        "/app", "/app/home", "/app/feed", "/app/explore",
        "/workspace", "/workspace/projects", "/workspace/team",
        # Products & Shop
        "/products", "/products/new", "/products/featured",
        "/products/sale", "/products/trending", "/products/recommended",
        "/shop", "/shop/all", "/shop/new-arrivals",
        "/categories", "/categories/electronics", "/categories/fashion",
        "/collections", "/collections/summer", "/collections/winter",
        "/cart", "/cart/summary", "/checkout", "/checkout/payment",
        "/checkout/confirm", "/orders", "/orders/history",
        "/orders/tracking", "/wishlist", "/favorites",
        # Blog & Content
        "/blog", "/blog/latest", "/blog/tech", "/blog/news",
        "/blog/tutorials", "/blog/case-studies", "/blog/announcements",
        "/articles", "/articles/featured", "/news", "/news/latest",
        "/press", "/press-releases", "/media", "/resources",
        "/tutorials", "/guides", "/how-to", "/tips",
        # Docs & API
        "/docs", "/docs/api", "/docs/getting-started", "/docs/guides",
        "/docs/reference", "/docs/changelog", "/docs/faq",
        "/api", "/api/v1", "/api/v1/resource", "/api/v1/items",
        "/api/v2", "/api/v2/users", "/api/v2/data", "/api/v2/search",
        "/api/v3/events", "/api/v3/webhooks", "/api/health", "/api/status",
        "/swagger", "/openapi", "/graphql", "/rest",
        # Marketing & Company
        "/about", "/about-us", "/team", "/careers", "/jobs",
        "/contact", "/contact-us", "/support", "/help",
        "/pricing", "/plans", "/enterprise", "/partners",
        "/affiliate", "/referral", "/ambassador",
        "/privacy-policy", "/terms", "/terms-of-service",
        "/cookie-policy", "/legal", "/compliance", "/security",
        # Uploads & Media
        "/uploads", "/uploads/files", "/uploads/images",
        "/media", "/media/photos", "/media/videos",
        "/assets", "/static", "/public",
        # Admin & Internal
        "/admin", "/admin/dashboard", "/admin/users",
        "/admin/settings", "/admin/logs", "/admin/reports",
        "/internal", "/ops", "/status", "/health",
        # Misc versioned
        "/v1/login", "/v1/logout", "/v1/data",
        "/v2/feed", "/v2/search", "/v2/notify",
        "/v3/stream", "/v3/sync",
    )

    _QUERY_TEMPLATES = (
        # Search
        {"q": "python"}, {"q": "machine learning"}, {"q": "laptop"},
        {"q": "sneakers"}, {"q": "react hooks"}, {"q": "best practices"},
        {"search": "invoice"}, {"search": "user settings"},
        {"keyword": "startup"}, {"keyword": "remote work"},
        # Pagination & sorting
        {"page": None, "per_page": "10"}, {"page": None, "per_page": "25"},
        {"page": None, "limit": "20"}, {"offset": None, "limit": "50"},
        {"sort": "price_asc"}, {"sort": "price_desc"},
        {"sort": "popularity"}, {"sort": "newest"}, {"sort": "rating"},
        {"order": "asc"}, {"order": "desc"},
        # Filtering
        {"filter": "in_stock"}, {"filter": "on_sale"}, {"filter": "new_arrivals"},
        {"status": "active"}, {"status": "pending"}, {"status": "archived"},
        {"type": "admin"}, {"type": "member"}, {"type": "guest"},
        {"category": "electronics"}, {"category": "fashion"},
        {"category": "home"}, {"category": "books"}, {"category": "sports"},
        {"tag": "ai"}, {"tag": "open-source"}, {"tag": "featured"},
        {"label": "urgent"}, {"label": "review"},
        # Language & locale
        {"lang": "en"}, {"lang": "es"}, {"lang": "fr"},
        {"lang": "de"}, {"lang": "ja"},
        {"locale": "en-US"}, {"locale": "fr-FR"}, {"locale": "ja-JP"},
        # UTM / Marketing
        {"utm_source": "google"}, {"utm_source": "facebook"},
        {"utm_source": "twitter"}, {"utm_source": "newsletter"},
        {"utm_medium": "cpc"}, {"utm_medium": "email"}, {"utm_medium": "social"},
        {"utm_campaign": "spring_sale"}, {"utm_campaign": "black_friday"},
        {"utm_campaign": "product_launch"},
        {"utm_content": "banner_a"}, {"utm_term": "buy+shoes+online"},
        {"ref": "newsletter"}, {"ref": "homepage"}, {"ref": "sidebar"},
        {"referrer": "google"},
        # Dynamic sentinels (resolved at generate time)
        {"id": None}, {"user_id": None}, {"product_id": None},
        {"order_id": None}, {"session": None}, {"token": None},
        {"page": None}, {"offset": None},
        # Feature flags & A/B
        {"variant": "a"}, {"variant": "b"},
        {"experiment": "checkout_v2"}, {"feature": "dark_mode"},
        {"preview": "true"}, {"debug": "false"},
        # Format & view
        {"format": "json"}, {"format": "csv"}, {"format": "xml"},
        {"version": "2"}, {"v": "3"},
        {"source": "mobile"}, {"source": "web"},
        {"device": "mobile"}, {"device": "desktop"},
        {"modal": "signup"}, {"redirect": "/dashboard"}, {"next": "/checkout"},
        {"tab": "overview"}, {"tab": "reviews"},
        {"view": "grid"}, {"view": "list"},
        {"expanded": "true"}, {"highlight": "new"},
    )

    def __init__(
        self,
        *,
        protocol: bool = True,
        host: bool = True,
        path: bool = True,
        query_string: bool = True,
        blank_percentage: float = 0.0,
        **kwargs,
    ):
        super().__init__(blank_percentage=blank_percentage, **kwargs)
        self.protocol_enabled = protocol
        self.host_enabled = host
        self.path_enabled = path
        self.query_enabled = query_string

    def _build_query(self) -> str:
        """Pick a random query template and resolve any dynamic sentinel values."""
        params = dict(self.get_random_data_by_list(self._QUERY_TEMPLATES))

        for key in params:
            if params[key] is None:
                match key:
                    case "id" | "product_id" | "order_id":
                        params[key] = str(self.generate_integer(1, 99999))
                    case "user_id":
                        params[key] = str(self.generate_integer(1000, 999999))
                    case "session" | "token":
                        params[key] = "%06x%06x" % (
                            self.generate_integer(0, 0xFFFFFF),
                            self.generate_integer(0, 0xFFFFFF),
                        )
                    case "page":
                        params[key] = str(self.generate_integer(1, 100))
                    case "offset":
                        params[key] = str(self.generate_integer(0, 500))
                    case _:
                        params[key] = str(self.generate_integer(1, 9999))

        return "?" + urlencode(params)

    def generate_non_blank(self, row_data=None) -> str | None:
        protocol = self.get_random_data_by_list(
            self._PROTOCOLS) if self.protocol_enabled else None
        host = self.get_random_data_by_list(
            self._HOSTS) if self.host_enabled else None
        path = self.get_random_data_by_list(
            self._PATHS) if self.path_enabled else ""
        query = self._build_query() if self.query_enabled and self.get_random_object() < 0.5 else ""

        if protocol and host:
            base = f"{protocol}://{host}"
        elif host:
            base = host
        elif protocol:
            base = f"{protocol}://"
        else:
            base = ""

        url = base + path + query
        return url or None

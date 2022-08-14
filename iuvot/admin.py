from django.contrib import admin


class RestrictedAdminSite(admin.AdminSite):
    site_header = "Monty Python administration"

    def get_urls(self):
        # delete all urls apart from a restricted few
        urls = super().get_urls()
        restricted_url_names = [
            "index",
            "login",
            "logout",
            "password_change",
            "password_change_done",
            "app_list",
        ]
        restricted_urls = [
            url
            for url in urls
            if hasattr(url, "name") and url.name in restricted_url_names
        ]
        print(urls)
        print(restricted_urls)
        return restricted_urls

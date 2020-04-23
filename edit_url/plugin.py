from mkdocs.plugins import BasePlugin
from urllib.parse import urljoin


class EditUrlPlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        if 'repo_url' in page.meta:
            src_path = page.file.src_path.replace('\\', '/')
            page.edit_url = urljoin(page.meta['repo_url'], config.get('edit_uri', None) + src_path)
        return context

from mkdocs.plugins import BasePlugin
from urllib.parse import urljoin
import os


class EditUrlPlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        src_path = page.file.src_path.replace('\\', '/')
        # split the relative file path into list
        s_split = src_path.split(os.path.sep)
        # split the global edit_uri path into list
        edit_path_split = config.get('edit_uri', None).split(os.path.sep)
        # insert edit_uri elements after the first element of s_split (one merged list)
        s_split[1:1] = edit_path_split
        # create path from list again
        new_edit = os.path.join(*s_split)
        page.edit_url = urljoin(config.get('repo_url', None), new_edit)
        return context

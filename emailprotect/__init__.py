"""
MkDocs-Plugin to obscure email-addresses from address-harvesting spam-bots.

Currently, it replaces everything (both in the contents and the template)
looking like an email-address with its unicode numeric character reference,
e.g. "a" -> "&#097;".
This should be invisible to normal users and not affect the usability;
but it will prevent some spam-bots from finding the addresses. But note
that this may also prevent legitimate address-crawlers and search engines
from finding these addresses.

Markdown already does something similar for `<mail@example.com>, but not
for `[mail@example.com](mailto:mail@example.com)` or for non-linked
addresses, see:
https://daringfireball.net/projects/markdown/syntax#autolink

Developed for and tested with MkDocs 1.0.4 on Linux.

:Author:    Roland Freikamp <rk@simple-is-better.org>
:Version:   2020-01-07
:License:   MIT
"""
import re

from mkdocs.plugins import BasePlugin

RE_MAILTO = re.compile(r'''mailto:([^@<> '"]+@[^@<> '"]+)''', re.I)
RE_MAIL   = re.compile(       r'''([^@<> '"]+@[^@<> '"]+)''')       #pylint: disable=bad-whitespace

def char2code(c):
    """Convert character to unicode numeric character reference.
    """
    try:
        return "&#%03d;" % ord(c)
    except Exception:   # fallback; pylint: disable=broad-except
        return c

class EmailProtect(BasePlugin):
    """Obscure email-addresses from address-harvesting spam-bots.
    """
    #def on_page_content(self, html, *_args, **_kwargs):
    def on_post_page(self, output_content, *_args, **_kwargs):
        content = output_content
        content = RE_MAILTO.sub(lambda match: "mailto:" + "".join(char2code(c) for c in match.group(1)), content)
        content = RE_MAIL.sub(  lambda match:             "".join(char2code(c) for c in match.group(1)), content)   #pylint: disable=bad-whitespace
        return content

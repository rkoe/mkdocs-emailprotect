mkdocs-emailprotect-plugin
===========================

Author:    Roland Freikamp <rk@simple-is-better.org>
Version:   2020-01-07
License:   MIT

A MkDocs plugin that tries to obscure email-addresses from address-harvesting
spam-bots.

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

Install:
    python3 setup.py develop

Test:
    ./test/test.sh

Enable the plugin in `mkdocs.yml`:

    plugins:
	- emailprotect


"""Check translation coverage and preserve executable examples and navigation.

Run after building the site: python3 -m unittest discover -s tests -p 'test_*.py'
Requires the same Markdown package as tools/build_graph_site.py.
"""
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import markdown

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / 'docs/zh-CN'


def data(filename, name):
    source = (ROOT / 'assets/site' / filename).read_text(encoding='utf-8')
    return json.loads(source.split(f'window.{name}=', 1)[1].rstrip(';\n'))


class Structure(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.tags = Counter()
        self.links = []
        self.node_links = []
        self.images = []
        self.heads = []
        self.code = []
        self.in_pre = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags[tag] += 1
        attrs = dict(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
            self.node_links.append(attrs.get('data-node'))
        if tag == 'img':
            self.images.append(attrs['src'])
        if re.fullmatch('h[1-6]', tag):
            self.heads.append((tag, attrs.get('id')))
        if tag == 'pre':
            self.in_pre = True
            self.code.append('')

    def handle_endtag(self, tag):
        if tag == 'pre':
            self.in_pre = False

    def handle_data(self, text):
        if self.in_pre:
            self.code[-1] += text


def structure(source):
    source = re.sub(r'^<a id="[^"]+"></a>\s*\n', '', source, flags=re.M)
    return Structure(markdown.markdown(source, extensions=['tables', 'fenced_code', 'toc', 'sane_lists']))


def canonical_link(href, source):
    url = urlsplit(href)
    if url.scheme or url.netloc or not url.path:
        return href
    target = (source.parent / unquote(url.path)).resolve()
    if target.is_relative_to(ZH):
        target = ROOT / 'docs' / target.relative_to(ZH)
    return target.relative_to(ROOT).as_posix() + ('#' + url.fragment if url.fragment else '')


class TranslationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.en = data('pages-data.js', 'SBOS_PAGES')
        cls.zh = data('pages-zh-cn.js', 'SBOS_PAGES_ZH')
        cls.sources = [ROOT / 'docs/README.md'] + sorted(
            file for directory in (ROOT / 'docs').iterdir()
            if directory.is_dir() and directory != ZH
            for file in directory.glob('*.md'))

    def test_every_article_and_section_has_a_translation(self):
        self.assertEqual(set(self.en), set(self.zh))
        for source in self.sources:
            with self.subTest(file=source.relative_to(ROOT)):
                self.assertTrue((ZH / source.relative_to(ROOT / 'docs')).is_file())

    def test_translation_structure_links_and_code(self):
        for source in self.sources:
            with self.subTest(file=source.relative_to(ROOT)):
                translated = ZH / source.relative_to(ROOT / 'docs')
                en_raw = source.read_text(encoding='utf-8')
                zh_raw = translated.read_text(encoding='utf-8')
                en, zh = structure(en_raw), structure(zh_raw)
                self.assertRegex(zh_raw, r'[\u4e00-\u9fff]', 'Missing Chinese prose')
                self.assertEqual([h[0] for h in en.heads], [h[0] for h in zh.heads], 'Heading structure')
                # Paragraph, list and table counts catch dropped body sections.
                for tag in ('p', 'li', 'table', 'tr', 'td', 'th', 'blockquote', 'pre', 'img'):
                    self.assertEqual(en.tags[tag], zh.tags[tag], f'{tag} count')
                self.assertEqual(en.code, zh.code, 'Executable examples must remain unchanged')
                self.assertEqual([canonical_link(h, source) for h in en.links],
                                 [canonical_link(h, translated) for h in zh.links], 'Link targets')
                self.assertEqual([canonical_link(h, source) for h in en.images],
                                 [canonical_link(h, translated) for h in zh.images], 'Image targets')
                # Long unchanged prose is usually a missed paragraph. Code is
                # separately preserved and excluded from this check.
                for paragraph in re.findall(r'<p>(.*?)</p>', markdown.markdown(zh_raw, extensions=['fenced_code']), re.S):
                    prose = re.sub(r'<code>.*?</code>|<[^>]+>', '', paragraph, flags=re.S)
                    if len(re.findall(r'[A-Za-z]', prose)) > 80:
                        self.assertRegex(prose, r'[\u4e00-\u9fff]', f'Untranslated paragraph: {prose[:100]}')

    def test_rendered_articles_keep_stable_anchors_and_language(self):
        for pid, english in self.en.items():
            with self.subTest(page=pid):
                chinese = self.zh[pid]
                self.assertEqual(chinese['lang'], 'zh-CN')
                self.assertEqual(chinese['path'], f'docs/zh-CN/{pid}.md')
                en, zh = Structure(english['html']), Structure(chinese['html'])
                self.assertEqual(en.heads, zh.heads)
                self.assertEqual(en.code, zh.code)
                self.assertEqual(en.node_links, zh.node_links, 'Graph previews on article links')
                self.assertEqual([h['id'] for h in english['heads']], [h['id'] for h in chinese['heads']])
                self.assertRegex(chinese['text'], r'[\u4e00-\u9fff]')
                raw = (ROOT / chinese['path']).read_text(encoding='utf-8')
                for _, anchor in en.heads:
                    self.assertIn(f'<a id="{anchor}"></a>', raw, 'Stable GitHub heading anchor')
                for image in zh.images:
                    if not urlsplit(image).scheme:
                        self.assertTrue((ROOT / image).is_file(), f'Missing rendered image: {image}')

    def test_diagrams_have_translated_text_and_preserve_geometry(self):
        for source in (ROOT / 'docs').glob('*/*.svg'):
            with self.subTest(image=source.relative_to(ROOT)):
                translated = ZH / source.relative_to(ROOT / 'docs')
                self.assertTrue(translated.is_file())
                en, zh = ET.parse(source), ET.parse(translated)
                en_elements, zh_elements = list(en.iter()), list(zh.iter())
                self.assertEqual([e.tag for e in en_elements], [e.tag for e in zh_elements])
                # IDs, paths and element geometry remain aligned with the source.
                for a, b in zip(en_elements, zh_elements):
                    for key in ('id', 'x', 'y', 'x1', 'x2', 'y1', 'y2', 'width', 'height', 'd', 'viewBox'):
                        self.assertEqual(a.get(key), b.get(key), key)
                self.assertRegex(''.join(zh.getroot().itertext()), r'[\u4e00-\u9fff]')


if __name__ == '__main__':
    unittest.main()

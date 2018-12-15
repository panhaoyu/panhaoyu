from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re
import os


def image1(gallery, path):
    return 'https://raw.githubusercontent.com/panhaoyu/images1/master/{}/{}'.format(gallery, path)


def url(storage, gallery, path):
    return {
        'image1': image1,
    }[storage](gallery, path)


class ImagePreprocessor(Preprocessor):
    PATTERN = re.compile('!\[(?P<description>.*?)]\((?P<link>.*?)\)')

    def run(self, lines):
        if 'gallery' not in self.md.Meta:
            return lines
        if 'storage' not in self.md.Meta:
            self.md.Meta['storage'] = ['image1']
        for index, line in enumerate(lines):
            if '[' not in line:
                continue
            lines[index] = self.PATTERN.sub(self.replace, line)
        return lines

    def replace(self, match):
        description = match.group('description')
        link = match.group('link')
        storage = self.md.Meta['storage'][0]
        gallery = self.md.Meta['gallery'][0]
        if not description:
            description = os.path.splitext(link)[0]
        link = url(storage, gallery, link)
        return '<img src="{}" alt="{}" width="100%">'.format(link, description)
        # TODO 改好模板之后，这里应该用下面的那个
        # return '![{}]({})'.format(description, link)


class ImageExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(ImagePreprocessor(md), 'ImageExtension', 1)


def makeExtension(**kwargs):
    return ImageExtension(**kwargs)

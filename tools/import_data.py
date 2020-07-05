import os

from blog.models import Article


data_path = '/Users/panyu/python_projects/mysite/data'


def main():
    content_list = []
    files= os.listdir(data_path)
    for name in files:
        os.path.join(data_path, name)
        with open(f, 'r', encoding='utf-8') as f:
            content = f.read()
            item = (name[:-4], content[:100], content)
            content_list.append(item)
    for item in content_list:
        print('saving article: %s' % item[0])
        article = Article()
        article.title = item[0]
        article.brief_content = item[1]
        article.content = item[2]
        article.save()


if __name__ == '__main__':
    main()

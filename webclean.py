import click
import newspaper


@click.command()
@click.argument('url')
@click.option(
    '--text', '-t', default=False, is_flag=True, help='Output as plain text.')
def webclean(url, text):
    """Print a cleaned-up version of a web article."""

    def fix_url(url):
        if not (url.startswith('http://') or url.startswith('https://')):
            url = ''.join(['http://', url])
        return url

    config = newspaper.Config()
    # config.memoize_articles = False
    config.fetch_images = False

    url = fix_url(url)
    article = newspaper.Article(url, keep_article_html=True)
    article.download()
    article.parse()
    if text:
        all_text = ''
        title = '=' * len(article.title)
        title = "\n\n\n{}\n{}\n\n".format(article.title, title)
        article_text = ''.join([title, article.text])
        all_text = ''.join([all_text, article_text])
        click.echo_via_pager(all_text)
    else:
        click.echo("""<!DOCTYPE html>
            <html>
                   <head>
                       <title>
                           {0}
                       </title>
                   </head>
                   <body>
                       <h1>{0}</h1>
                       {1}
                   </body>
               </html>
            """.format(article.title, article.article_html))


if __name__ == '__main__':
    webclean()

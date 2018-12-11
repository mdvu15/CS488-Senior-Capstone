#Article extreactor module

from goose3 import Goose

g = Goose()

def articleExtractor(urlArticle):
    """Take an online article URL and return its plain text as an array of sentences"""
    
    article_sentences = []
    article = g.extract(url=urlArticle)
    
    for sentence in article.cleaned_text.split("."):
        temp_sentences = sentence.rstrip().lstrip().replace('\n', '')
        if len(temp_sentences) != 0:
            article_sentences.append(temp_sentences)

    return article_sentences

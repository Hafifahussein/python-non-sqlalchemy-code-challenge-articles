class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot change name after instantiation")

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)  # Article __init__ handles appending

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    _all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be 2–16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls._all:
            return None
        return max(cls._all, key=lambda m: len(m._articles))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be 5–50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        # link relationships
        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot change title after instantiation")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        self._magazine = value


if __name__ == "__main__":
    a1 = Author("Hafifa Hussein")
    a2 = Author("Ayub Adan")

    m1 = Magazine("TechLife", "Technology")
    m2 = Magazine("HealthNow", "Health")

    a1.add_article(m1, "AI in 2025")
    a1.add_article(m2, "Wellness Tips")
    a1.add_article(m1, "Python Rocks")

    a2.add_article(m2, "Eating Healthy")

    print("Articles by Hafifa:", [a.title for a in a1.articles()])
    print("Magazines by Hafifa:", [m.name for m in a1.magazines()])
    print("Topic Areas by Hafifa:", a1.topic_areas())
    print("Contributors to TechLife:", [a.name for a in m1.contributors()])
    print("Article Titles in TechLife:", m1.article_titles())
    print("Contributing Authors in TechLife:", [a.name for a in m1.contributing_authors() or []])
    print("Top Publisher:", Magazine.top)
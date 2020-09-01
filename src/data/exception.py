class PageError(Exception):
    # Exception related to page
    pass


class NoGreenBoxError(PageError):
    def __str__(self):
        return "There is no download box."


class NoDownloadPageError(PageError):
    def __str__(self):
        return "Can't download in this page."

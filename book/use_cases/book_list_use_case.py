class BookListUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        return self.repo.list()

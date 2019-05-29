# book_list_use_case.py
from book.response_objects import response_objects as res


class BookListUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if not request:
            return res.ResponseFailure.build_response_from_invalid_request(
                    request
                    )

        try:
            books = self.repo.list(filters=request.filters)
            return res.ResponseSuccess(books)
        except Exception as exc:
            return res.ResponseFailure.build_system_failure(exc)

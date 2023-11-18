from structures.news import NewsList
from structures.response import Response
from wrapper.wrapper import Wrapper


class NewsListWrapper(Wrapper[NewsList]):
    def wrap(self, obj: NewsList) -> Response:
        return Response(
            {
                "news": [
                    {
                        "seq": news.seq,
                        "title": news.title,
                        "content": news.content,
                        "date": news.date.date().isoformat(),
                    }
                    for news in obj
                ]
            }
        )

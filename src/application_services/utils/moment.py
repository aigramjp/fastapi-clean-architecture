from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), "JST")

class Moment:
    @staticmethod
    def timestamp():
        return datetime.now(JST)

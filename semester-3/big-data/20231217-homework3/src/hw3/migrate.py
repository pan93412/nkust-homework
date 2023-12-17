import sqlite3


def migrate(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        create table if not exists news (
            id integer primary key autoincrement,
            title varchar(255) not null,
            abstract text not null,
            date date not null
        )
        """
    )

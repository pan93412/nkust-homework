from dataclasses import dataclass
import dataclasses
import logging
from argon2 import PasswordHasher

from flask import Flask, request, session as fsession
from sqlalchemy import Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = r"DpHi-7O0-k72-MqH-2v1-h5M-g4s-Dhs-Gu4-0KD-4sO-dSp-3RV-hMh-dJm-x5x-CaA-HNn-Dz9-Czg-ymq-3Jx-9RO-QGO-JBZ-63R-ZVz-Vyg-ipa-q3I-3KQ-Y2X"
engine = create_engine("sqlite:///db.sqlite3", echo=True)
hasher = PasswordHasher()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)


@dataclass(frozen=True)
class UserCreateRequestDto:
    name: str
    password: str
    email: str | None

    @classmethod
    def from_form(cls, form: dict[str, str]):
        name = form.get("name")
        if not name:
            raise ValueError("name is required")

        password = form.get("password")
        if not password:
            raise ValueError("password is required")

        email = form.get("email")

        return cls(name=name, password=password, email=email)

    def to_entity(self) -> User:
        return User(
            name=self.name, password=hasher.hash(self.password), email=self.email
        )


@dataclass(frozen=True)
class UserUpdateRequestDto:
    name: str | None
    password: str | None
    email: str | None

    @classmethod
    def from_form(cls, form: dict[str, str]):
        name = form.get("name")
        password = form.get("password")
        email = form.get("email")

        return cls(name=name, password=password, email=email)

    def patch_entity(self, entity: User):
        entity.name = self.name if self.name else entity.name
        entity.password = (
            hasher.hash(self.password) if self.password else entity.password
        )
        entity.email = self.email if self.email else entity.email


@dataclass(frozen=True)
class UserResponseDto:
    id: int
    name: str
    email: str | None

    @classmethod
    def from_entity(cls, entity: User):
        return cls(id=entity.id, name=entity.name, email=entity.email)


@app.route("/users")
def get_all_users():
    with Session(engine) as session:
        users = session.query(User)
        return [
            dataclasses.asdict(UserResponseDto.from_entity(user))
            for user in users.all()
        ]


@app.route("/users/<int:id>")
def get_user(id: int):
    with Session(engine) as session:
        user = session.query(User).filter(User.id == id).first()
        if user is None:
            return {"error": "no such user"}, 404

        return dataclasses.asdict(UserResponseDto.from_entity(user))


@app.route("/install", methods=["POST"])
def install():
    password = request.form.get("password")
    if not password:
        return {"error": "password is required"}, 400

    hashed_password = hasher.hash(password)

    with Session(engine) as session:
        # check if there is already an admin user
        user = session.query(User).filter(User.name == "admin").first()
        if user is not None:
            return "", 404

        user = User(name="admin", password=hashed_password, email="admin@localhost")
        session.add(user)
        session.commit()
        return dataclasses.asdict(UserResponseDto.from_entity(user)), 201


@app.route("/users", methods=["POST"])
def create_user():
    current_user = fsession.get("logged_in_user_id")
    if current_user is None:
        return {"error": "login required"}, 401

    try:
        request_dto = UserCreateRequestDto.from_form(request.form)
    except ValueError as e:
        return {"error": str(e)}, 400
    except:
        return {"error": "unknown error"}, 500

    with Session(engine) as session:
        user = request_dto.to_entity()
        session.add(user)
        session.commit()
        return dataclasses.asdict(UserResponseDto.from_entity(user)), 201


@app.route("/users/<int:id>", methods=["PATCH"])
def partial_update_user(id: int):
    current_user = fsession.get("logged_in_user_id")
    if current_user is None:
        return {"error": "login required"}, 401

    request_dto = UserUpdateRequestDto.from_form(request.form)

    with Session(engine) as session:
        user = session.query(User).filter(User.id == id).first()
        if user is None:
            return {"error": "no such user", "id": id}, 404

        request_dto.patch_entity(user)
        session.commit()

        return dataclasses.asdict(UserResponseDto.from_entity(user)), 200


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id: int):
    current_user = fsession.get("logged_in_user_id")
    if current_user is None:
        return {"error": "login required"}, 401

    with Session(engine) as session:
        modified = session.query(User).filter(User.id == id).delete()
        session.commit()

        if modified == 0:
            return {"error": "no such user", "id": id}, 404

        return "", 204


@app.route("/auth/login", methods=["POST"])
def login():
    email = request.form.get("email")
    if not email:
        return {"error": "email is required"}, 400

    password = request.form.get("password")
    if not password:
        return {"error": "password is required"}, 400

    with Session(engine) as session:
        user = session.query(User).filter(User.email == email).first()
        if user is None:
            return {"error": "no such user"}, 404

        try:
            hasher.verify(user.password, password)
            fsession["logged_in_user_id"] = user.id
            return {"ok": True, "name": user.name}, 200
        except:
            return {"error": "wrong password"}, 401


@app.route("/auth/logout", methods=["POST"])
def logout():
    fsession.clear()
    return "", 204


@app.route("/auth/me", methods=["GET"])
def me():
    current_user = fsession.get("logged_in_user_id")
    if current_user is None:
        return {"error": "login required"}, 401

    with Session(engine) as session:
        user = session.query(User).filter(User.id == current_user).first()
        if user is None:
            return {"error": "no such user"}, 404

        return dataclasses.asdict(UserResponseDto.from_entity(user)), 200


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True)

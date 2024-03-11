import { Avatar, Person } from "./profile.tsx";

export function ScientistGallery() {
  const people: Person[] = [
    {
      name: "阿爾伯特·愛因斯坦",
      image: "https://upload.wikimedia.org/wikipedia/commons/7/78/Einstein1921_by_F_Schmutzer_4.jpg",
    },
    {
      name: "艾薩克·牛頓",
      image: "https://upload.wikimedia.org/wikipedia/commons/3/39/GodfreyKneller-IsaacNewton-1689.jpg",
    },
    {
      name: "尼古拉·特斯拉",
      image:
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Tesla_circa_1890.jpeg/440px-Tesla_circa_1890.jpeg",
    },
  ];

  return (
    <section>
      <h1>Amazing scientists</h1>
      <div className="grid lg:grid-cols-3 gap-4 md:grid-cols-2 grid-cols-1">
        {people.map((person) => <Avatar person={person} />)}
      </div>
    </section>
  );
}

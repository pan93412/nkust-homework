export interface AvatarProps {
  person: Person;
  size?: number | string;
}

export interface Person {
  name: string;
  image: `https://${string}`;
}

export function Avatar({ person, size = 200 }: AvatarProps) {
  return (
    <figure className="space-y-2">
      <img
        src={person.image}
        alt={person.name}
        height={size}
      />
      <figcaption>
        <strong>{person.name}</strong>
      </figcaption>
    </figure>
  );
}

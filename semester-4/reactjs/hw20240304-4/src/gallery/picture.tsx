import { ComponentChildren } from "preact";

export interface PictureProps {
  name: string;
  description: ComponentChildren;
  href: string;
}

export function Picture(props: PictureProps) {
  return (
    <div class="shadow flex flex-col-reverse rounded">
      <section class="py-2 px-8">
        <h2>{props.name}</h2>
        <p class="leading-normal">{props.description}</p>
      </section>
      <img src={props.href} alt={props.name} class="w-full h-36 object-cover" />
    </div>
  );
}

import { ComponentChildren } from "preact";

export interface GalleryProps {
  children: ComponentChildren;
}

export function Gallery({ children }: GalleryProps) {
  return (
    <div class="grid gap-8 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
      {children}
    </div>
  );
}

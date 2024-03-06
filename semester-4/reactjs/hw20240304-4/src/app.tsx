import { Gallery, Picture } from "./gallery";

export function App() {
  return (
    <div className="font-sans p-8">
      <Gallery>
        <Picture
          name={"Man 1"}
          href={"https://picsum.photos/seed/1709523897772/300/300"}
          description={"Et non at et repellendus hic maxime eaque molestiae excepturi quam rem est neque. Qui autem aliquid aut enim laborum ut debitis culpa laborum officiis voluptatem occaecati aliquam consequuntur. Tempore quas voluptas libero eveniet et sapiente perferendis et exercitationem qui autem odit."}
        />
        <Picture
          name={"Man 2"}
          href={"https://picsum.photos/seed/1709523897772/300/300"}
          description={"Et non at et repellendus hic maxime eaque molestiae excepturi quam rem est neque. Qui autem aliquid aut enim laborum ut debitis culpa laborum officiis voluptatem occaecati aliquam consequuntur. Tempore quas voluptas libero eveniet et sapiente perferendis et exercitationem qui autem odit."}
        />
        <Picture
          name={"Man 3"}
          href={"https://picsum.photos/seed/1709523897772/300/300"}
          description={"Et non at et repellendus hic maxime eaque molestiae excepturi quam rem est neque. Qui autem aliquid aut enim laborum ut debitis culpa laborum officiis voluptatem occaecati aliquam consequuntur. Tempore quas voluptas libero eveniet et sapiente perferendis et exercitationem qui autem odit."}
        />
      </Gallery>
    </div>
  );
}

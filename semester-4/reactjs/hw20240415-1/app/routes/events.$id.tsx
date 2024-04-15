import { useParams } from "@remix-run/react";
import { events } from "../event-data";

export default function EventDetailsPage() {
  const params = useParams();
  if (!params.id) {
    throw new Response(null, { status: 400 });
  }

  const event = events.find((event) => event.id === Number(params.id));
  if (!event) {
    throw new Response("Event not found", { status: 404 });
  }

  return (
    <div>
      <h1>{event.name}</h1>
      <p>Date: {event.date}</p>
      <p>Location: {event.location}</p>
      <p>Author: {event.author}</p>
      <div>{event.description}</div>
    </div>
  );
}

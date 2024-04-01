import {
  Link,
  Outlet,
  isRouteErrorResponse,
  useRouteError,
} from "@remix-run/react";
import { events } from "../event-data";

export default function Events() {
  return (
    <div style={{ display: "flex", gap: "2px" }}>
      <section className="left">
        <h1>Upcoming Events</h1>
        {events.length > 0 ? (
          <ul>
            {events.map((event) => (
              <li key={event.id}>
                <h2>{event.name}</h2>
                <p>Date: {event.date}</p>
                <p>Location: {event.location}</p>
                <p>Description: {event.description}</p>
                <Link to={`/events/${event.id}`}>Learn more</Link>
              </li>
            ))}
          </ul>
        ) : (
          <p>No upcoming events at the moment. Check back soon!</p>
        )}
      </section>
      <section className="right">
        <Outlet />
      </section>
    </div>
  );
}

export function ErrorBoundary() {
  const error = useRouteError();

  if (isRouteErrorResponse(error)) {
    if (error.status === 404) {
      return (
        <div>
          <h1>{error.data}</h1>
        </div>
      );
    }
  }

  throw error;
}

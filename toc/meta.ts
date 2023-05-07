import { z } from "https://deno.land/x/zod@v3.21.4/mod.ts";

export const CourseSchema = z.enum([
  "S1 - Web Development",
  "S1 - Basic Programming",
  "S2 - Linux Administration",
  "S2 - Intermediate Python Programming",
  "S2 - PHP Server-side Programming",
]);

export type Course = z.infer<typeof CourseSchema>;
export type CourseSet<C extends Course> =
  C extends `S${infer S extends number} - ${infer T}` ? [S, T] : never;

export const MetaSchema = z.object({
  title: z.string(),

  course: CourseSchema,
});
export type Meta = z.infer<typeof MetaSchema>;

export function extractCourse<C extends Course>(c: Course): CourseSet<C> {
  const [s, t] = c.split(" - ");
  return [parseInt(s.slice(1)), t] as CourseSet<C>;
}

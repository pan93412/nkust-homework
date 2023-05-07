import * as frontmatter from "https://deno.land/std@0.186.0/front_matter/yaml.ts";
import * as walk from "https://deno.land/std@0.186.0/fs/walk.ts";
import * as log from "https://deno.land/std@0.186.0/log/mod.ts";
import { Course, CourseSet, Meta, MetaSchema, extractCourse } from "./meta.ts";
import { ZodError } from "https://deno.land/x/zod@v3.21.4/mod.ts";

export type MetaWithFileInfo = Meta & {
  readmePath: string;
  homeworkPath: string;
};

export async function* parseMetaFromDir(
  dir: string
): AsyncGenerator<MetaWithFileInfo> {
  const absdir = Deno.realPathSync(dir);

  for await (const entry of walk.walk(absdir, {
    exts: ["md"],
    includeDirs: false,
    skip: [/node_modules/, /\.pytest_cache/],
  })) {
    // TODO)) not safe
    const relEntry = entry.path.slice(absdir.length);

    log.info(`extracting: ${relEntry}`);
    const content = await Deno.readTextFile(entry.path);

    const homeworkPath = relEntry.split("/").slice(0, -1).join("/");
    log.debug(`homework path: ${homeworkPath}`);

    if (!frontmatter.test(content)) {
      log.debug("no frontmatter provided");
      continue;
    }

    try {
      const { attrs: _attrs } = frontmatter.extract(content);
      const attrs = MetaSchema.parse(_attrs);

      yield { ...attrs, readmePath: relEntry, homeworkPath };
    } catch (e) {
      if (e instanceof TypeError) {
        log.warning(`frontmatter invalid: ${e.message}`);
      }

      if (e instanceof ZodError) {
        log.warning(`extract failed: ${e.message}`);
      }
    }
  }
}

type PossibleSemesters = CourseSet<Course>[0];
type PossibleCourse = CourseSet<Course>[1];

export type GroupedMeta = Map<
  PossibleSemesters,
  Map<PossibleCourse, MetaWithFileInfo[]>
>;

export async function groupMeta(dir: string): Promise<GroupedMeta> {
  const table: GroupedMeta = new Map();

  for await (const entry of parseMetaFromDir(dir)) {
    const [semester, course] = extractCourse(entry.course);

    if (!table.has(semester)) {
      table.set(semester, new Map());
    }

    const semesterMap = table.get(semester);
    if (typeof semesterMap === "undefined")
      throw new Error("assert – semesterObject is not undefined");

    if (!semesterMap.has(course)) {
      semesterMap.set(course, []);
    }

    const courseMap = semesterMap.get(course);
    if (typeof courseMap === "undefined")
      throw new Error("assert – courseMap is not undefined");

    courseMap.push(entry);
  }

  // sort every entries
  for (const [_, courseMap] of table) {
    for (const [_, entries] of courseMap) {
      entries.sort((a, b) => a.homeworkPath.localeCompare(b.homeworkPath));
    }
  }

  return table;
}

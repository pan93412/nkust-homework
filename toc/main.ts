import * as log from "https://deno.land/std@0.186.0/log/mod.ts";
import * as flags from "https://deno.land/std@0.186.0/flags/mod.ts";
import { groupMeta } from "./parse.ts";
import MarkdownParser from "./markdown.ts";
import { ConsoleHandler } from "https://deno.land/std@0.186.0/log/handlers.ts";

const args = flags.parse(Deno.args, {
  default: {
    lint: true,
    debug: false,
    output: undefined,
  },
  boolean: ["debug", "lint"],
  string: ["output"],
  negatable: ["lint"],
  alias: {
    o: "output",
  },
});

if (args.debug)
  log.setup({
    handlers: {
      default: new ConsoleHandler("DEBUG"),
    },
    loggers: {
      default: {
        level: "DEBUG",
        handlers: ["default"],
      },
    },
  });

const markdownParser = new MarkdownParser();

const dir = args._[0]?.toString() ?? ".";
log.info(`dir: ${dir}`);
const grouped = await groupMeta(dir);
log.debug(grouped);

const markdown = markdownParser.render(grouped, {
  lint: args.lint,
});

if (args.output) {
  const encoder = new TextEncoder();
  const markdownBytes = encoder.encode(markdown);
  await Deno.writeFile(args.output, markdownBytes);
} else {
  console.log(markdown);
}

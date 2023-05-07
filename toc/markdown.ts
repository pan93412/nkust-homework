import * as eta from "https://deno.land/x/eta@v2.1.1/mod.ts";
import * as path from "https://deno.land/std@0.186.0/path/mod.ts";
import markdownlint from "npm:markdownlint@^0.28.2";
import * as markdownlintHelpers from "npm:markdownlint-rule-helpers@^0.19.0";
import { GroupedMeta } from "./parse.ts";
import { TemplateFunction } from "https://deno.land/x/eta@v2.1.1/compile.ts";

const templatePath = path.fromFileUrl(
  new URL("./templates/toc.md.eta", import.meta.url)
);

export default class MarkdownParser {
  cache: Record<string, string> = {};
  template: TemplateFunction;

  constructor() {
    this.template = eta.compile(Deno.readTextFileSync(templatePath), {
      cache: true,
    });
  }

  render(
    meta: GroupedMeta,
    options: {
      lint?: boolean;
    } = {}
  ): string {
    let result = eta.render(this.template, {
      meta,
    });

    if (options.lint) {
      const lintResult = markdownlint.sync({
        strings: {
          result,
        },
      });
      result = markdownlintHelpers.applyFixes(result, lintResult.result);
    }

    return result;
  }
}

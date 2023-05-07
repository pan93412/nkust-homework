# TOC generator

Generate the `TOC.md` file for this repository based on the front matter.

## Usage

```plain
deno task run [options] src
```

Options:

- `--[no-]lint`: Whether to Lint the `TOC.md` file. Default: `true`
- `-o` or `--output`: The output file. Default: None (stdout)
- `--debug`: Whether to print debug information. Default: `false`

## Front Matter Example

```markdown
---
title: TOC generator
course: S1 - Web Development
---

Description.
```

The comprehensive list of available `course`s can be seen on the `CourseSchema` definition in [`meta.ts`](./meta.ts) file. You may need to update the `CourseSchema` regularly.

## CI

Usually, this script is run on CI to generate the `TOC.md` file. For the CI configuration example, see [`../.github/workflows/toc.yml`](../.github/workflows/toc.yml).

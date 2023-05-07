// url_test.ts
import { assertEquals } from "https://deno.land/std@0.186.0/testing/asserts.ts";

Deno.test("url test", () => {
  const abs = "/a/b/c/d/e/f/g";
  const base = "/a/b/c/d";
  assertEquals(abs.slice(base.length), "/e/f/g");
});

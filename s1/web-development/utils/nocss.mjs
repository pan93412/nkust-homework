/**
 * Allow using ?nocss to remove all CSS.
 */

export function removeCss() {
  document.querySelectorAll("style").forEach((e) => {
    e.remove();
  });
}

export function removeCssOnNoCss() {
  const param = new URL(location.href).searchParams;

  if (param.has("nocss")) removeCss();
}

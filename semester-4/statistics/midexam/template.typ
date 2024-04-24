#import "typst-sympy-calculator.typ": *

#let project(title: "", authors: (), body) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(numbering: "1", number-align: center)
  set text(
    font: ("PT Sans", "PingFang TC"),
    lang: "zh",
    region: "TW",
    size: 14pt,
  )
  set heading(numbering: "1.1")
  set math.equation(numbering: "(i)")
  show link: underline

  show heading: text.with(font: ("AR FangXinShuH7B5Std"), size: 1.2em)
  show heading: pad.with(top: 0.4em, bottom: 0.6em)
  show raw: text.with(font: "JetBrains Mono", size: 1.1em)

  // Title row.
  align(center)[
    #text(font: ("AR FangXinShuH7B5Std"), weight: 700, 1.7em, title)
  ]

  // Main body.
  set par(justify: true, leading: 0.8em)

  show regex("\=\=.+?\=\="): it => {
    show "==": ""
    highlight(it)
  }
  body
}

#let comment(it) = text(fill: luma(96), size: 10pt, it)

#let badge(fill, it) = {
  set text(weight: "bold", size: 11pt, fill: white.darken(1%))

  box(inset: 0.5em, baseline: 25%, fill: fill, radius: 6pt, it)
}

#let question(id, name, it) = block(width: 100%)[
  #show: pad.with(top: 1em)

  #badge(luma(64), id)

  #block(above: 12pt, width: 100%)[
    *#name* #label(id)
  ]

  #pad(x: 1.75em, it)
]

#let blk(it) = block(width: 100%, fill: luma(245), radius: 8pt, pad(x: 1.6em, y: 1.4em)[#it])

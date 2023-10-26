// The project function defines how your document looks.
// It takes your content and some metadata and formats it.
// Go ahead and customize it to your liking!
#import "@preview/cetz:0.1.1"

#let project(title: "", authors: (), body) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(numbering: "1", number-align: center)
  set text(
    font: ("Fira Sans", "Noto Sans TC"),
    lang: "zh",
    region: "TW",
    size: 14pt,
  )
  set heading(numbering: "1.1")
  set math.equation(numbering: "(i)")
  show link: underline

  show heading: it => pad(it, bottom: 0.5em)

  // Title row.
  align(center)[
    #block(text(weight: 700, 1.75em, title))
  ]

  // Main body.
  set par(justify: true, leading: 0.8em)

  show regex("\=\=.+\=\="): it => {
    show "==": ""
    highlight(it)
  }
  body
}

#let comment(it) = text(fill: luma(140), size: 8pt, it)

#let badge(fill, it) = {
  set text(weight: "bold",  size: 11pt, fill: white.darken(1%))

  box(inset: 0.5em, baseline: 25%, fill: fill, radius: 6pt, it)
}

#let question(id, label, tags, name, it) = block(width: 100%)[
  #show: pad.with(top: 1em)

  #badge(luma(64), id)
  #for tag in tags [
    #badge(blue.darken(50%), tag)
  ]

  #block(above: 12pt, width: 100%)[
    *#name* #label
  ]

  #pad(x: 1.75em, it)
]

#let formula(it, questions: ()) = block(width: 100%, fill: luma(245), radius: 8pt, pad(x: 1.6em, y: 1.4em)[
  #it

  #questions.enumerate().map(it => link(it.at(1), text(fill: luma(100), [習題 #{it.at(0) + 1}]))).join("｜")
])

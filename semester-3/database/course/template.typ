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

  show heading: it => [
    #pad(it, bottom: 0.5em)
  ]
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

#let question(id, tags, name, it) = [
  #show: pad.with(top: 1em)

  #badge(luma(64), id)
  #for tag in tags [
    #badge(blue.darken(50%), tag)
  ]

  #block(above: 12pt)[
    *#name*
  ]

  #pad(x: 1.75em, it)
]

#let monospaced-block(it) = [
  #set text(font: "JetBrains Mono", weight: "bold", size: 12pt)

  #h(3em)
  #it
]

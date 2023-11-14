// The project function defines how your document looks.
// It takes your content and some metadata and formats it.
// Go ahead and customize it to your liking!
#import "@preview/cetz:0.1.1"

#let project(title: "", authors: (), body) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(numbering: "1", number-align: center)
  set text(font: "Noto Serif TC", lang: "zh", region: "TW", size: 14pt)
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

#let notimportant(body) = {
  text(body, gray)
}

#let correction(body) = {
  text(body, red)
}

#let question(name, it) = {
  block(
    fill: luma(230),
    inset: 12pt,
  )[
    #set text(font: "Fira Sans", fill: luma(30))

    #block(
      fill: luma(210),
      inset: 16pt,
      radius: 4pt,
      [Question: #name]
    )

    #it
  ]
}

// The project function defines how your document looks.
// It takes your content and some metadata and formats it.
// Go ahead and customize it to your liking!
#import "@preview/cetz:0.1.1"

#let project(title: "", authors: (), body) = {
  // Set the document's basic properties.
  set document(author: authors, title: title)
  set page(numbering: "1", number-align: center)
  set text(font: "Noto Sans TC", lang: "zh", region: "TW")
  set heading(numbering: "1.1")

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

#let badge(fill, it) = {
  set text(weight: "bold", size: 10pt, fill: white.darken(1%))

  box(inset: 0.4em, baseline: 25%, fill: fill, radius: 5pt, it)
  h(3pt)
}

#let question(count, name, it, wrong: false) = [
  #count.step()

  #show: pad.with(top: 1em)
  #block(above: 8pt)[
    #let t = [*#count.display("1.") #name*]

    #if wrong {
      text(fill: red.darken(25%), t)
    } else {
      t
    }
  ]

  #pad(x: 1.75em, it)
]

#let comment(it) = text(fill: gray.darken(25%), size: 10pt, it)

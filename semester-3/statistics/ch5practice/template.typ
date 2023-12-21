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

#let comment(it) = text(fill: luma(140), size: 8pt, it)

#let badge(fill, it) = {
  set text(weight: "bold", size: 10pt, fill: white.darken(1%))

  box(inset: 0.5em, fill: fill, radius: 6pt, it)
  h(4pt)
}

#let qlabel(qid) = label("question-"+str(qid))

#let question(qid, name, it, checked: false, wrong: false) = [
  #show: pad.with(top: 1em)
  #qlabel(qid)

  #{
    badge(gray.darken(50%), "Q" + str(qid))
    style(styles => {
      if measure(it, styles).width == 0pt {
        badge(red.darken(20%), "not answered")
      }
    })
    if checked {
      if wrong {
        badge(red.darken(50%), "!")
      }
      badge(green.darken(50%), "checked")
    }
  }

  #block(above: 10pt)[
    #if wrong {
      text(fill: red.darken(25%))[*#name*]
    } else {
      [*#name*]
    }
  ]

  #pad(x: 1.75em, it)
]

// The project function defines how your document looks.
// It takes your content and some metadata and formats it.
// Go ahead and customize it to your liking!
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

  body
}

#let notimportant(body) = {
  text(body, gray)
}

#let correction(body) = {
  text(body, red, weight: "bold")
}

#let hint(body) = {
  text(body, weight: "light", style: "italic")
}

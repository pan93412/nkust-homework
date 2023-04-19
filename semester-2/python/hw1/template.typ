// The project function defines how your document looks.
// It takes your content and some metadata and formats it.
// Go ahead and customize it to your liking!

#let document_font = ("Helvetica Neue", "PingFang TC")
#let monospace_font = "Sarasa Fixed TC"
#let font_size = 12pt

#let tagbox(it) = {
  box(
      inset: (x: 6pt, y: 4pt),
      baseline: 25%,
      radius: 50%,
      fill: luma(235),
      it
    )
}


#let project(title: "", authors: (), date: none, body) = {
  // Set the document's basic properties.
  set document(author: authors.map(a => a.name), title: title)
  set page(numbering: "1", number-align: center)
  set text(font: document_font, size: font_size, lang: "zh")

  // monospace
  show raw: (rest) => {
    set text(font: monospace_font, size: font_size)
    rest
  }

  // Set paragraph spacing.
  show par: set block(above: 1.2em, below: 1.2em)

  set par(leading: 0.75em)

  // Title row.
  align(center)[
    #block(text(weight: 700, 1.75em, title))
    #v(1.2em, weak: true)
    #date
  ]

  // Author information.
  pad(
    top: 0.8em,
    bottom: 0.8em,
    x: 2em,
    grid(
      columns: (1fr,) * calc.min(3, authors.len()),
      gutter: 1em,
      ..authors.map(author => align(center)[
        *#author.name* \
        #author.email
      ]),
    ),
  )

  // Main body.
  set par(justify: true)

  // link
  show link: it => {
    text(underline(it), fill: blue)
  }

  // code (inline)
  show raw.where(block: false): it => {
    tagbox(it)
  }

  body
}

#let srcresult(
  filename,
  source_code,
  run_result,
) = {
  v(12pt)

  show regex("Step (\d)+:"): (rest) => {
    tagbox(rest)
  }

  grid(
    columns: (2fr,1fr),
    block(width: 90%)[
      #grid(
        columns: (1fr,1fr),
        column-gutter: 0.5em,

        align(start)[*#filename*],
        align(end, link(filename)[原始碼])
      )
      #line(length: 100%)
      #source_code
    ],
    block(width: 90%)[
      *執行結果*
      #line(length: 100%)
      #run_result
    ]
  )
}

#let nraw(rest) = {
  show raw.where(block: true): it => {
    set par(justify: false)
    set text(font: monospace_font, size: font_size)
    grid(
      columns: (100%, 100%),
      column-gutter: -100%,
      block(
        width: 100%,
        for (i, line) in it.text.split("\n").enumerate() {
          box(width: 0pt, align(right, str(i + 1) + h(1em)))
          hide(line)
          linebreak()
        }
      ),
      it
    )
  }
  rest
}

#let code(src, margin: false) = {
    if (margin) [
      #v(1em)
    ]

    nraw(src)

    if (margin) [
      #v(1em)
    ]
}

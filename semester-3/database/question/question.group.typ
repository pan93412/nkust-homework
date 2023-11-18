#set text(font: "Helvetica Neue", size: 12pt)
#show raw: set text(font: ("等距更紗黑體 TC"), size: 11pt)

#let answer_to_table(raw) = [
  #set text(font: ("等距更紗黑體 TC"))

  #let header = raw.at(0).keys()
  #let body = raw.slice(1).map(row => row.values().map(value => [#value])).flatten()

  #table(
    columns: (1fr,)*header.len(),
    ..header.map(value => [*#value*]),
    ..body
  )
]

#let get_question(id: str) = [
  *Input*

  #raw(lower(read(id+".sql")).replace("    ", "\t"), block: true, lang: "sql")

  *Output*

  #let answer = json(id+".ans")
  #answer_to_table(answer)
]

= Database Question

#for value in json("index") [
  == Question #{value.slice(1)}

  #get_question(id: str(value))
]

#set text(font: "Helvetica Neue")
#show raw: set text(font: ("等距更紗黑體 TC"))

#let get_question(id: str) = [
  *Input*

  #raw(lower(read(id+".sql")), block: true, lang: "sql")

  *Output*

  #raw(read(id+".ans"), block: true)
]

= Database Question

#for value in json("index") [
  == Question #{value.slice(1)}

  #get_question(id: str(value))
]

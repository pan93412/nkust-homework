#set text(size: 12.5pt)

== Ch15-2 + Ch19 homeworks

C111156103, Yi-Jyun Pan.

== Ex. 15-10 – Intersection

$
pi_"name" ("Students") sect pi_"name" ("Instructors")
$

```sql
SELECT name FROM Students
INTERSECT
SELECT name FROM Instructors;
```

== Ex. 15-11 – Equijoin merge

$
"Students" join_("Students"."d_no" = "Departments"."d_no") "Departments"
$


```sql
SELECT * FROM Students
JOIN Departments ON (Students.d_no = Departments.d_no);
```

== Ex. 15-12 – $theta$ merge

$
p_A ("Transcripts") join_("A"."c_no" = "B"."c_no" and "A"."score" > "B"."score") p_B ("Transcripts")
$

```sql
SELECT *
FROM Transcripts A JOIN (Transcripts B)
  ON (A.c_no = B.c_no AND A.score > B.score);
```

== Ex. 15-13 – Natural Join

$
"Students" join "Departments"
$

```sql
SELECT * FROM Students
NATURAL JOIN Departments;
```

== Ex. 15-14 – Left Outer Join

$
"Students" join.l "Departments"
$

```sql
SELECT * FROM Students
LEFT OUTER JOIN Departments;
```

== Ex. 15-15 – Right Outer Join

$
"Students" join.r "Departments"
$

```sql
SELECT * FROM Students
RIGHT OUTER JOIN Departments;
```

== Ex. 15-16 – Full Outer Join

$
"Students" join.l.r "Departments"
$

```sql
SELECT * FROM Students
FULL OUTER JOIN Departments;
```


== Ex. 15-17 – Addition Op.

$
"Current_Deposit" <- "Current_Deposit" union { ( "'A100'", "'張無忌'", 6000)}
$

```sql
INSERT INTO Current_Deposit
VALUES ('A100', '張無忌', 6000);
```


== Ex. 15-18 – Deletion Op.

$
"Current_Deposit" <- \
  "Current_Deposit" - sigma_("a_no" = "'A003'" or "amount" = 5000) ("Current_Deposit")
$

```sql
DELETE FROM Current_Deposit
WHERE a_no = 'A003' OR amount = 5000;
```

== Ex. 15-19 – Update Op.

$
"Current_Deposit" <- \
  ("Current_Deposit" - sigma_("a_no" = "'A003'")("Current_Deposit") union { ( "'A003'", "'張三丰'", 5000) })
$

```sql
DELETE FROM Current_Deposit
WHERE a_no = 'A003';

INSERT INTO Current_Deposit
VALUES ('A003', '張三丰', 5000);
```

or,

```sql
UPDATE Current_Deposit
SET a_name = '張三丰', amount = 5000
WHERE a_no = 'A003';
```

== Ex. 15-20 – Aggregate Op.

$
Im_("count"("a_no")) ("Current_Deposit")
$

```sql
SELECT COUNT(a_no)
FROM Current_Deposit;
```

== Ex. 15-21 – Aggragate Op with attributes

$
space_("id")Im_("count"("c_no"), "average"("score")) ("Transcripts")
$

```sql
SELECT id, COUNT(c_no), AVG(score)
FROM Transcripts
GROUP BY id;
```

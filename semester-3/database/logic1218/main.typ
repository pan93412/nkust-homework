#set text(font: "PingFang TC", size: 14pt)

= Database Assignment – Logic 2023/12/18

C111156103, 潘奕濬。

Convert the given relational domain to SQL statement.

== Example 14-1

$
{ <"no", "name", "GPA"> | <"no", "name", "GPA"> in "Students" and "GPA" > 3.0 }
$

```sql
SELECT no, name, GPA
FROM Students
WHERE GPA > 3.0;
```

== Example 14-2

$
{ "ename" | &<"ename", "salary", "bdate"> \
            & in "Employee" and "salary" > 40000 and "bdate" < "'60/01/01'" }
$

```sql
SELECT ename
FROM Employee e
WHERE e.salary > 40000 AND e.bdate < '60/01/01';
```

== Example 15-1

$
sigma_("GPA" < 3.2)("Students")
$

```sql
SELECT *
FROM Students
WHERE GPA < 3.2;
```

== Example 15-2

$
sigma_("GPA" < 3.2 space and "sid" < "'S003'")("Students")
$

```sql
SELECT *
FROM Students
WHERE GPA < 3.2 AND sid < 'S003';
```

== Example 15-3

$
pi_("eid", "name", "rank")("Instructors")
$

```sql
SELECT eid, name, rank
FROM Instructors;
```

== Example 15-4

$
pi_("department")("Instructors")
$

```sql
SELECT department
FROM Instructors;
```

== Example 15-5

$
pi_("eid", "name", "salary")(sigma_("salary">55000)("Instructors")))
$


```sql
SELECT eid, name, salary
FROM Instructors
WHERE salary > 55000;
```

== Example 15-6

寫出關聯代數之聯集運算式：將 `Students` 和 `Instructors` 兩個資料表的 `name` 欄位中，列出所有學生和講師姓名。

$
pi_("name")("Students") union pi_("name")("Instructors")
$

== Example 15-7

寫出關聯代數之差集運算式：利用姓名，取出存在 `Employees` 資料表中，但不存在 `Instructors` 資料表的 `Employees` 的姓名。

$
pi_("name")("Employees") - pi_("name")("Instructors")
$

== Example 15-8

$
pi_("Students"."d_no" = "Departments"."d_no")("Students" times "Departments")
$

其對應的 `CROSS JOIN` SQL 語法為：

```sql
SELECT *
FROM Students CROSS JOIN Departments
  ON (Students.d_no = Departments.d_no);
```

== Example 15-9

$
pi_("sid", "Students"."name", "Departments"."name", "room") \
(
  sigma_("Students"."d_no" = "Departments"."d_no")(
    "Students" times "Departments"
  )
)
$

其對應的 `CROSS JOIN` SQL 語法為：

```sql
SELECT sid, Students.name, Departments.name, room
FROM Students CROSS JOIN Departments
  ON (Students.d_no = Departments.d_no);
```

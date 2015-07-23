title: Relational Databases
output: relational-databases.html
--
<style>
  table {
    border-collapse: collapse;
  }
  table td, table th {
    border: 1px solid black;
    font-size: 0.75em;
  }
  table tr:first-child th {
    border-top: 0;
  }
  table tr:last-child td {
    border-bottom: 0;
  }
  table tr td:first-child,
  table tr th:first-child {
    border-left: 0;
  }
  table tr td:last-child,
  table tr th:last-child {
    border-right: 0;
  }
  td {
    padding: .2em;
  }
  caption {
    text-align: left;
  }
</style>
# TODOS:

- review dataset
--

Lesson Outline:
References: http://datacarpentry.github.io/sql-ecology/sql.html

10 minutes of lecture, 15 minutes of stuff (interactive
repeat 3x

--
# Introduction to Relational Databases
## Relational Databases and sqlite

--
### Relational Databases?

- Data stored in **tables** with **fields** (columns) and records (rows)
- All values in a field have the same **type** (Number, Character, Date/Time)
- **Query** to view, sort, filter, and calculate

--
### Benefits

- **Safety** - Separate data from analysis
- **Speed** - RDBMS are good at the sorting/filtering
- **Quality Control** - Data types are enforced ([usually](https://www.sqlite.org/faq.html#q3))
- **Organization** - _relational_ database
- **Standardized** - Similar model to Python/Pandas but data-centric

--
### Example: Playwrights

&nbsp;
<table width="100%">
    <tbody>
    <tr>
        <th>id</th>
        <th>first_name</th>
        <th>last_name</th>
        <th>year_of_birth</th>
        <th>year_of_death</th>
    </tr>
    <tr>
        <td>1</td>
        <td>William</td>
        <td>Shakespeare</td>
        <td>1564</td>
        <td>1616</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Arthur</td>
        <td>Miller</td>
        <td>1915</td>
        <td>2005</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Samuel</td>
        <td>Beckett</td>
        <td>1906</td>
        <td>1989</td>
    </tr>
</tbody>
</table>

--
### Relational Database Management Systems

Some free/open source. Differ in some data types and advanced functionality, but all do tables and queries.

MySQL, Oracle, PostgreSQL, SQL Server, Microsoft Access, FileMaker Pro, **SQLite**

--
### Creating a database

- Database can have several tables
- Table is like a worksheet or data frame
- To create one, specify the column names and types

SQLite Data Types ([sqlite.org](https://www.sqlite.org/datatype3.html))

- NULL
- **INTEGER**
- **REAL**
- **TEXT**
- BLOB

--
### Creating a table

Create table:
```
sqlite> create table playwrights (
   ...> first_name text,
   ...> last_name text,
   ...> year_of_birth integer,
   ...> year_of_death integer
   ...> );
```
List tables:
```
sqlite> .tables
playwrights
```
--
### Populating a database

- **INSERT** to add rows.
- Unlike spreadsheets, *rows* have no inherent order.
- *Column* order does matter!

```
sqlite> insert into playwrights values
   ...> ('William','Shakespeare',1564,1616);

      # first_name, last_name, birth_year, death_year
```
_Always end with a semicolon_
TODO: Provide this file at this point
--
### Querying data

.headers on
.mode column

```
sqlite>

**SELECT**

--

Leftovers
- foreign keys/relationals
- ids
- nulls / default values

SQL is structured query language. It's the
- Why SQL/relational?
  - data agility
  - data robustness. leave data as data, analysis is separate
  - not specific to python. portable data
  - normalization - don't repeat yourself
- Why SQLite?
  - free, open source. not actually lite


## Creating and populating a database using SQL

## Moving data between spreadsheets, data frames and relational databases
- CSV import from sqlite prompt
- pandas to_sql


# 14:30 - 16:00 Querying Relational Databases

## Using SQL to query a single table

## Joining multiple tables

## Aggregate and custom functions
- group by, sum, max, count





--
### Example - long_data

&nbsp;
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>id</th>
      <th>Dilution</th>
      <th>Analyte</th>
      <th>FI-Bkgd</th>
      <th>FI-Bkgd-Neg</th>
      <th>CV</th>
      <th>Participant ID</th>
      <th>Visit Code</th>
      <th>Visit Date</th>
      <th>Sample Type</th>
      <th>Buffer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50</td>
      <td>p24 (19)</td>
      <td>474.8</td>
      <td>454.800000</td>
      <td>0.0372</td>
      <td>URN2</td>
      <td>0</td>
      <td>10/14/1899</td>
      <td>PLA</td>
      <td>PBS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>gp41 (44)</td>
      <td>470.8</td>
      <td>452.800000</td>
      <td>0.1387</td>
      <td>URN2</td>
      <td>0</td>
      <td>10/14/1899</td>
      <td>PLA</td>
      <td>PBS</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50</td>
      <td>Con 6 gp120/B (72)</td>
      <td>52.5</td>
      <td>44.500000</td>
      <td>0.1183</td>
      <td>URN2</td>
      <td>0</td>
      <td>10/14/1899</td>
      <td>PLA</td>
      <td>PBS</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50</td>
      <td>B.con.env03 140 CF (65)</td>
      <td>55.5</td>
      <td>46.500000</td>
      <td>0.1709</td>
      <td>URN2</td>
      <td>0</td>
      <td>10/14/1899</td>
      <td>PLA</td>
      <td>PBS</td>
    </tr>
    <tr>
      <th>4</th>
      <td>50</td>
      <td>Blank (53)</td>
      <td>29.0</td>
      <td>NaN</td>
      <td>0.0527</td>
      <td>URN2</td>
      <td>0</td>
      <td>10/14/1899</td>
      <td>PLA</td>
      <td>PBS</td>
    </tr>
    <tr>
      <th>5</th>
      <td>50</td>
      <td>Con S gp140 CFI (3)</td>
      <td>82.0</td>
      <td>62.000000</td>
      <td>0.1799</td>
      <td>URN2</td>
      <td>0</td>
      <td>10/14/1899</td>
      <td>PLA</td>
      <td>PBS</td>
    </tr>
  </table>


--

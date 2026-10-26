# Part 6 - System design (about one page)

Bullets, tables and a simple diagram (ASCII or Mermaid) are welcome. Say what you would **assume** when the statement is unclear - we care about your reasoning, not a "right" answer. You will present this in the interview.

## Scenario

A diagnostics lab runs immunoassays on **96-well plates**.

* A liquid-handling **robot** prepares each plate from a **patient list** (sample id -> well) that an operator provides.
* A **plate reader**, controlled by vendor software on a **Windows PC**, measures every well and, when the read finishes, **writes a results file into a local folder** (CSV/XML; it can take several seconds to write, and the vendor software sometimes re-exports the same file).
* The lab works on a **local network, often without Internet**. Later, sites may sync to a cloud.
* Three kinds of users: **operators** (log in, start a run, watch progress, read results), **lab supervisors** (review/approve results, export a report), and a remote **support team** who need structured logs from every site to diagnose problems.
* There are dozens of sites, each with its own PC. Data about patients is sensitive.

Build a system for this. We will start with one site.

## 1. Architecture
*Components, what runs where, and how they talk to each other (diagram + 3-5 lines).*


## 2. Data model
*Main tables/entities and key fields; what is the identity of a "run" and of a "result"?*


## 3. API
*5-8 endpoints (method + path + one line each). Which ones would a front-end call?*


## 4. Ingesting the result file
*How do you notice a new file, know it is complete, avoid processing the same file twice, and link it to the right run?*


## 5. Failure modes
*Three things that will go wrong in real life (reader PC reboots mid-write, bad patient list, support cannot reach the site, ...) and what the system does about each.*


## 6. Logging & telemetry
*What do you log, with which fields, so support can reconstruct what happened to run X at site Y?*


## 7. Two weeks, one engineer
*What do you build first, what do you deliberately leave out, and what is the first thing you would test?*


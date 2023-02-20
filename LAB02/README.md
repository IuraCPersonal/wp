# HTTP, CACHING AND CONTENT NEGOTIATION

## 🐱‍👓 INTRODUCTION

Imagine, you're a developer at TwoLines GmbH, a startup from Zurich, Switzerland. The idea of the startup is pretty simple - you develop best-in-class browser experience, with privacy and security in mind. One day, you receive a message from the CTO, Mike

```
Hey there!

Tomorrow we'll have a presentation for a really biiiig investor.
They say they don't need PPTs. They want at least some proof-of-concept for secure browsers for their toasters.
Can you share with me the executable we used last time for demo?

Cheers,
Mike
```
Yeah, the catch is toasters don't have any browser exeprience!
Nonetheless, you can't remember where you've saved the executable, so you start writing it from scratch.

## 📄 TASKS

- [ ] You have to write a command line program, using [go2web](go2web) executable as a starting point.
- [ ] The program should implement at least the following CLI:
  ```
  go2web -u <URL>         # make an HTTP request to the specified URL and print the response
  go2web -s <search-term> # make an HTTP request to search the term using your favorite search engine and print top 10 results
  go2web -h               # show this help
  ```
- [ ] The responses from request should be human-readable (e.g. no HTML tags in the output)

## 📊 GRADING

### Points:

- executable with `-u` or `-s` options - `+5` points
- executable with `-u` and `-s` options - `+6` points

### You can get `+1` extra point:
- if results/links from search engine can be accessed (using your CLI);
- for implementing HTTP request redirects

### You can get `+2` extra points:
- for implementing an HTTP cache mechanism;
- for implementing content negotiation e.g. by accepting and handling both JSON and HTML content types.

## DOCUMENTATION

How to run: 

```
$ go2web [OPTION | -h | -s | -u] [ARGUMENT | URL | <search-term>]
```
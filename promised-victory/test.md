---
title: test
type: Meta

---

  

``` mermaid

graph LR
A[test] --> B 

class A internal-link;
```

minimal example for gantt with link

``` mermaid
gantt
dateFormat YYYY-MM-DD
title A Gantt Diagram
section Section
A task           :milestone, a1, 2014-01-01, 2014-01-01
B task           :2014-01-01  , 20d
C task           : 2014-01-01, 2014-03-01
click a1 href "obsidian://vault/YOUR_VAULT/path_to_your_file.md"


```

```juggl
local: Prosnen
```

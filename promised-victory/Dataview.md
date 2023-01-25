
---
type: Meta
---
Files with Missing summary 
```dataview
table sum, type
FROM -"7. Resources" and -"textgenerator"
where !sum or !type
sort type asc
```
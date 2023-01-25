---
PromptInfo:
  author: Philip
  description: null
  id: superexpand
  name: "\U0001F9D9 superexpand the lore"
title: superexpand

---


Additional information for Context
(DONT INCLUDE INTO PROMPT! THIS IS JUST CONTEXT!):
{{title}} ({{type}}): 
{{#each sum}}
- {{this}}
{{/each}}

{{#each children}}
{{this.basename}}:
{{#each frontmatter.sum}}
- {{this}}
{{/each}}

{{/each}}

Additional connections that MIGHT be useful: 
{{#each mentions.linked}}
Connection to: {{basename}}
{{#each results}}
- {{this}}
{{/each}}
{{/each}}

The above text is just lore information, use it for context on how characters behave or facts about citys to build uppon, but dont reitterate the bullet points.

prompt:
Write new Lore in the style of J. R. R. Tolkien:
{{selection}}
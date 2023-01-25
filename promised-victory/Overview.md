---
title: Overview
type: Meta

---


This Vault is divided into sections:

# Historic Events
```dataview
table
FROM -"7. Resources" and -"textgenerator"
where type = "History"
```

# Regions
```dataview
table 
FROM -"7. Resources" and -"textgenerator"
where type = "Region"
```

# Regions
```dataview
table 
FROM -"7. Resources" and -"textgenerator"
where type = "Settlement"
```


# Locality
```dataview
table 
FROM -"7. Resources" and -"textgenerator"
where type = "Locality"
```


# Factions
```dataview
table sum as Summary 
FROM -"7. Resources" and -"textgenerator"
where type = "Faction"
```

# NPCs
```dataview
table sum as Summary 
FROM -"7. Resources" and -"textgenerator"
where type = "NPC"
```

# Side NPCs
```dataview
table sum as Summary 
FROM -"7. Resources" and -"textgenerator"
where type = "SideNPC"
```


# Marked
```dataview
table sum as Summary, type as Type
FROM -"7. Resources" and -"textgenerator"
where type
```
# Unmarked
```dataview
table 
FROM -"7. Resources" and -"textgenerator"
where !type
```


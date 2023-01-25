---
sum:
- In 3014 the city of Lichtachte was attacked by zombies and General Malachi used
  the Plague to save them
- The Plague created undead, which were viewed as monsters by the League of Arathor
- High Paladin Erathenar discovered a Cure in 3018 and Defilers were founded in 3023
  by Malachi as a faction of undead and orcs.
- Defilers attacked cities in the west of the Basin in 3024 and conquered Desecrated
  Stronghold in 3028, pushing back the League.
- They conquered most of the Basin by 3031, leaving Trollbans Hold to be defended
  by Paladins.
- After four years of war, the League regained control over Desecrated Stronghold
  in 3039, but the Defilers ultimately overpowered Edschmied marking their victory.
title: Historic Events
type: History

---


``` dataviewjs
//CONFIG
const path = '"1. General/Historic Events"'
const title = "Historic Events"

//FUNCTIONS
function genMermaidLine(page, begin, end) {
    return ;
}

function checkfrontmatter(page){
    if (typeof page.gantt != "undefined")
    {
        if (typeof page.gantt.begin != "undefined" && typeof page.gantt.end != "undefined")
        {
            return true;
        }
        if (typeof page.gantt.milestone != "undefined")
        {
            return true;
        }
    }
    return false;
}

function loopPages(pages) {
    let mermaid = ''; 
    console.log(pages)
    pages = pages.filter(page => checkfrontmatter(page))
    console.log(pages)
    //sort pages by gantt.begin
    for (let page of pages) {
        //log to console
        console.log("Processing:"+ page.file.name)
        console.log(page)
        //check if gantt.begin and gantt.end object exists in page
        if (typeof page.gantt != "undefined"){
            if (typeof page.gantt.begin != "undefined" && typeof page.gantt.end != "undefined") {
                let identifier = page.file.name.replace(/ /g, "_");
                //create mermaid line
                mermaid += page.file.name + ' : ' + identifier + ", " + page.gantt.begin + ', ' + page.gantt.end + '\n';
                //make clickable
                mermaid += 'click ' + identifier + ' href "obsidian://open?vault=obsidian&file=' + page.file.path + '"\n';
            }
            //milestone if gantt.milestone exists
            //format:
            // A task           :milestone, identifier, 2014-01-01, 2014-01-01
            if (typeof page.gantt.milestone != "undefined") {
                console.log("milestone:"+ page.file.name)
                let identifier = page.file.name.replace(/ /g, "_");
                //create mermaid line
                mermaid += page.file.name + ' :milestone, ' + identifier + ", " + page.gantt.milestone + ', ' + page.gantt.milestone + '\n';
                //make clickable
                mermaid += 'click ' + identifier + ' href "obsidian://open?vault=obsidian&file=' + page.file.path + '"\n';
            }
        }
    }
    return mermaid;
}
//dates are not related to the actual date but a fantasy date system
//deactivate todayMarker and start with year 0


const Mermaid = `gantt
    title `+title+`
    todayMarker off
    dateFormat DD-MM-YYYY
    axisFormat %Y
    `;

const pages = dv.pages(path)
dv.paragraph('```mermaid\n' + Mermaid +loopPages(pages)+ '\n```');
```

## War History
Those are the most important facts about the War between the [[Defilers]] and the [[League of Arathor]]:
Year 3014: [[Attack on Lichtachte]]
Year 3015: [[The Plague spreads]]
Year 3018: [[The Cure]]
Year 3023: [[The Founding of the Defilers]]
Year 3024: [[The War Begins]]
Year 3028: [[The Tides Turn]]
Year 3031: [[The Fall of the League]]
Year 3032: [[The Tide Turns Again]]
Year 3036: [[Stalemate]]
Year 3039: [[The Defilers attack Edschmied]]

# Naruun Related History
While the war is going on, [[Naruun]] , [[The Cult of the Gifted]] , [[The Shaddowhammer]] and [[The Fulfiller]] also have a History:
Ancient Events: [[Naruun]] was sealed away by forces of nature
Year 3012: Naruun influence rises in the Basin
Year 3024: [[The Cult of the Gifted]] is founded
Year 3031: [[The Shaddowhammer]] is formed by cult leader Volar
Year 3038: [[The Fulfiller]] arrives in the Basin, spreading its influence 

# Volars History
[[Volar]]s History: 

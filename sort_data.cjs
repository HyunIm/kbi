const fs = require('fs');

const lines = fs.readFileSync('src/data/data.ts', 'utf8').split('\n');

let preamble = [];
let postamble = [];

// items will hold objects for everything in the array.
// item format: { type: 'object' | 'comment' | 'empty', lines: string[], source: string | null }
let items = [];
let state = 'preamble';
let currentObj = null;

function extractSource(objLines) {
    for (let line of objLines) {
        let m = line.match(/"source":\s*"([^"]+)"/);
        if (!m) m = line.match(/source:\s*"([^"]+)"/);
        if (m) return m[1];
    }
    return null;
}

function extractPage(objLines) {
    for (let line of objLines) {
        let m = line.match(/"page":\s*"([^"]+)"/);
        if (!m) m = line.match(/page:\s*"([^"]+)"/);
        if (m) return m[1];
    }
    return null;
}

function parsePageScore(pageStr) {
    if (!pageStr) return [999, 999];
    let m = pageStr.match(/(\d+)권\s*(\d+)p?/i);
    if (m) {
        return [parseInt(m[1]), parseInt(m[2])];
    }
    return [999, 999]; // fallback for "-" or invalid formats
}

function getScore(item) {
    let pageStr = extractPage(item.lines);
    return parsePageScore(pageStr);
}

let arrayEndLine = null;

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    if (state === 'preamble') {
        preamble.push(line);
        if (line.includes('export const dummyData: Question[] = [')) {
            state = 'array';
        }
    } else if (state === 'array') {
        if (line.trim() === '];') {
            state = 'postamble';
            postamble.push(line);
        } else if (line.trim().startsWith('//')) {
            items.push({ type: 'comment', lines: [line] });
        } else if (line.trim() === '{') {
            currentObj = [line];
            state = 'in_object';
        } else if (line.trim() === '') {
            items.push({ type: 'empty', lines: [line] });
        } else {
            console.log("UNEXPECTED ARRAY LINE:", line);
        }
    } else if (state === 'in_object') {
        currentObj.push(line);
        if (line.trim() === '},' || line.trim() === '}') {
            let src = extractSource(currentObj);
            items.push({ type: 'object', lines: currentObj, source: src });
            currentObj = null;
            state = 'array';
        }
    } else if (state === 'postamble') {
        postamble.push(line);
    }
}

let others = [];
let eval1 = [];
let eval2 = [];

for (let item of items) {
    if (item.type === 'object') {
        if (item.source === '1차평가') {
            eval1.push(item);
        } else if (item.source === '2차평가') {
            eval2.push(item);
        } else {
            others.push(item);
        }
    } else {
        // Leave comments exactly where they are in the sequence.
        // Since all comments in the file are before 1차평가 items, they will naturally fall into 'others'.
        others.push(item);
    }
}

function cmp(a, b) {
    let scoreA = getScore(a);
    let scoreB = getScore(b);
    if (scoreA[0] !== scoreB[0]) return scoreA[0] - scoreB[0];
    return scoreA[1] - scoreB[1];
}

eval1.sort(cmp);
eval2.sort(cmp);

let allItems = [...others, ...eval1, ...eval2];

// Fix trailing commas for objects
let lastObj = null;
for (let i = allItems.length - 1; i >= 0; i--) {
    if (allItems[i].type === 'object') {
        lastObj = allItems[i];
        break;
    }
}

for (let item of allItems) {
    if (item.type === 'object') {
        let lastLineIdx = item.lines.length - 1;
        let line = item.lines[lastLineIdx];
        if (item === lastObj) {
            // Remove comma if it exists
            item.lines[lastLineIdx] = line.replace('},', '}');
        } else {
            // Add comma if it doesn't exist
            if (!line.endsWith(',')) {
                item.lines[lastLineIdx] = line + ',';
            }
        }
    }
}

let output = [...preamble];
for (let item of allItems) {
    for (let line of item.lines) {
        output.push(line);
    }
}
for (let line of postamble) {
    output.push(line);
}

fs.writeFileSync('src/data/data.ts', output.join('\n'), 'utf8');
console.log("SUCCESS");

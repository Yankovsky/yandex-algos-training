const readline = require('readline');
const assert = require('assert')

const getSynonym = (synonyms, word) => {
    const synonymsDict = new Map()
    for (const pair of synonyms) {
        synonymsDict.set(pair[0], pair[1])
        synonymsDict.set(pair[1], pair[0])
    }

    return synonymsDict.get(word)
}


assert.strictEqual(getSynonym([['Hello', 'Hi'], ['Bye', 'Goodbye'], ['List', 'Array']], 'Goodbye'), 'Bye')
assert.strictEqual(getSynonym([['beep', 'Car']], 'Car'), 'beep')
assert.strictEqual(getSynonym([['Ololo', 'Ololo'], ['Numbers', '1234567890']], 'Numbers'), '1234567890')


const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

const inputLines = [];

rl.on('line', (data) => {
  inputLines.push(data.toString().trim());
});

rl.on('close', () => {
  process.stdout.write(inputProcessing(inputLines));
});


function inputProcessing(lines) {
    const n = lines[0]
    const synonyms = lines.slice(1, lines.length - 1).map(line => line.split(' '))
    const word = lines[lines.length - 1]
    return getSynonym(synonyms, word)
}

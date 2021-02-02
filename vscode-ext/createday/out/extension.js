"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.deactivate = exports.activate = void 0;
// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require("vscode");
const util_1 = require("util");
const MONTH_LOOKUP = new Map([
    [0, "jan"],
    [1, 'feb'],
    [2, 'mar'],
    [3, 'apr'],
    [4, 'may'],
    [5, 'june'],
    [6, 'july'],
    [7, 'aug'],
    [8, 'sept'],
    [9, 'oct'],
    [10, 'nov'],
    [11, 'dec'],
]);
let createDayDir = () => {
    if (vscode.workspace.workspaceFolders) {
        let baseDir = vscode.workspace.workspaceFolders[0].uri.fsPath;
        let today = new Date();
        let month = MONTH_LOOKUP.get(today.getMonth());
        let day = today.getDate();
        let year = today.getFullYear();
        let newDayStr = `${month}${day}_${year}`;
        let dayDir = `/serve/day/${newDayStr}`;
        let dayUri = vscode.Uri.file(baseDir + dayDir);
        vscode.workspace.fs.createDirectory(dayUri);
        return dayUri;
    }
    else {
        console.log("null day dir");
        return null;
    }
};
let createDayFile = (dir) => {
    let file = vscode.Uri.joinPath(dir, "index.md");
    let dateOptions = { weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric' };
    let dateString = new Intl.DateTimeFormat('en-US', dateOptions)
        .format(Date.now());
    let encoder = new util_1.TextEncoder();
    let fileContents = encoder.encode(`# ${dateString}\n\n`);
    vscode.workspace.fs.writeFile(file, fileContents);
    return file;
};
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
function activate(context) {
    // The command has been defined in the package.json file
    // Now provide the implementation of the command with registerCommand
    // The commandId parameter must match the command field in package.json
    let disposable = vscode.commands.registerCommand('createday.createDay', () => {
        // The code you place here will be executed every time your command is executed
        // Display a message box to the user
        let dirUri = createDayDir();
        if (dirUri !== null) {
            let file = createDayFile(dirUri);
            if (file !== null) {
                vscode.window.showInformationMessage('Created Day');
                vscode.window.showTextDocument(file);
            }
            else {
                vscode.window.showInformationMessage('Failed to Create Day File');
            }
        }
        else {
            vscode.window.showInformationMessage('Failed to Create Day Dir');
        }
    });
    context.subscriptions.push(disposable);
}
exports.activate = activate;
// this method is called when your extension is deactivated
function deactivate() { }
exports.deactivate = deactivate;
//# sourceMappingURL=extension.js.map
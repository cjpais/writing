# Open Source Markdown Editors

Here are some Open Source Markdown Editors which you can build on top of. 

You can also check <https://www.markdownguide.org/> for a comprehensive list of all editors even if not open source.

## General Feature Comparison

| Editor                                                  | Platforms                        | Written In             | Support .md Flavors             | Preview .md | Theming Support | Code Syntax Highlighting | Markdown Syntax Highlighting | Diagram Support                           | LaTeX Support    | Export                        | Integrations                                                | Extras                                                     |
| ------------------------------------------------------- | -------------------------------- | ---------------------- | ------------------------------- | ----------- | --------------- | ------------------------ | ---------------------------- | ----------------------------------------- | ---------------- | ----------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------- |
| [StackEdit](https://stackedit.io/)                      | Web                              | JS/VueJS               | CommonMark, GFM, Markdown Extra | ✅ (inline)  | ❌               | ✅                        | ✅                            | UML                                       | ✅                | None                          | Google Drive, CouchDB, Github, GitLab                       | Emoji, Musical Score, Collaboration                        |
| [Abricotine](https://abricotine.brrd.fr/)               | Desktop (all)                    | JS/Electron            | GFM                             | ✅  (inline) | ✅               | ✅                        | ✅                            | ❌                                         | ✅                | HTML and all Pandoc supported | None                                                        | Post-Processing Scripts, Ligatures                         |
| [Mark Text](https://marktext.app/)                      | Desktop (all)                    | JS/VueJS               | CommonMark, GFM                 | ✅  (inline) | ✅               | ✅                        | ✅                            | Flowchart, Sequence Diagrams, Gantt, Vega | ✅                | HTML, PDF                     | None                                                        | Editor Modes                                               |
| [Boost Note](https://boostnote.io/)                     | Web, Desktop (all), Android, iOS | TypeScript/Electron    | GFM                             | ✅           | ✅               | ✅                        | ✅                            | ❌                                         | ✅                | HTML                          | Private Cloud                                               | BoostHub                                                   |
| [VSCode](https://code.visualstudio.com/)                | Desktop (all)                    | TypeScript/Electron    | Virtually all (via plugins)     | ✅           | ✅ (custom css)  | ✅                        | ✅                            | Via plugins                               | ✅  (via plugins) | via tasks.json                | None                                                        | A lot via plugins                                          |
| [Left](https://hundredrabbits.itch.io/left)             | Desktop (all)                    | JS (maybe electron???) | Standard                        | ❌           | ✅               | ❌                        | ❌                            | ❌                                         | ❌                | None                          | None                                                        | Synonyms, Autocomplete, Speed Reader                       |
| [Zettlr](https://www.zettlr.com/)                       | Desktop (all)                    | JS/Electron/Vue        | GFM                             | ✅  (inline) | ✅               | ✅                        | ✅                            | Mermaid                                   | ✅                | HTML and all Pandoc supported | Zotero                                                      | Citations, Projects, [[Internal Linking]], Tags, Citation  |
| [Dillinger](https://dillinger.io/)                      | Web                              | JS/Angular/Express     | CommonMark                      | ✅           | ❌               | ✅                        | ✅                            | ❌                                         | ❌                | HTML, PDF                     | Google Drive, Bitbucket, GitHub, Medium, Dropbox, One Drive | HTML->MD                                                   |
| [MacDown](https://macdown.uranusjr.com/)                | MacOS                            | Objective-C            | GFM                             | ✅  (inline) | ✅               | ✅                        | ✅                            | ❌                                         | ✅                | HTML, PDF                     | None                                                        | Jekyll front-matter, Auto-Completion (doesn't work for me) |

## Editors

### [StackEdit](https://stackedit.io/) - [github](https://github.com/benweet/stackedit)

StackEdit is pretty awesome. It seems to be an extremely powerful online markdown editor. It has all kinds of connections which I feel make it quite special. It has wide support for different markdown specifications, LaTeX, UML, etc. 

StackEdit has the concept of workspaces. For example this could be my Google Drive workspace, or my GitHub workspace. In a workspace StackEdit displays a file browser of all the markdown files on the left. Note that it does not display other file types.

The main editing interface has 2 portions. It is a 'split-editor' where you edit the raw markdown on one side and get a rendering of it on the other. It also has inline markdown formatting.

### [Abricotine](https://abricotine.brrd.fr/) - [github](https://github.com/brrd/abricotine)

Abricotine is a pretty minimalistic editor, but looks to be very extensible. It has a built in spell checker. It looks to be aimed at single file editing in a beautiful enviornment. Some cool things are ligature support, and adding post-processor to files. This can be something like exporting an HTML doc from the file.

Warning: Looks like on OSX the latest version cannot be built. 

### [Mark Text](https://marktext.app/) - [github](https://github.com/marktext/marktext)

Maybe one of the most beautiful editors I've seen. Some of the many highlights are a file browser, inline rendering, easy table manipulation, etc. To me it also feels very performant. Note that the file browser will also only show markdown files.

It also has tabs so you can be editing multiple files at once which is helpful.

Notably it has a few different editor modes which could help you when editing large files. However I like the regular mode a lot. 

### [Boost Note](https://boostnote.io/) - [github](https://github.com/BoostIO/Boostnote.next)

Notably has support across the web, desktop, and mobile. This is pretty impressive stuff and reminds me a lot of [Bear](https://bear.app/) in a way. Has some of the same sync features as well. There is a collaborative version as well (which doesn't appear to be open source). Even the basic cloud version is free which is really nice. 

### [VSCode](https://code.visualstudio.com/) - [github](https://github.com/microsoft/vscode)

Well VSCode is normally a Text Editor for code, but it is also a fantastically extensible platform. There are some great markdown plugins that make VSCode amazing for editing markdown. Even by default it is quite good. The features it provides for editing code are also helpful here. Amazing integration with git is also notable. You should give VSCode a try for editing your markdown documents. May be less good to fork, but great to build on top of

Of course it also has a file browser that shows all kinds of files. Vim mode if you like that too 😉

### [Left](https://hundredrabbits.itch.io/left) - [github](https://github.com/hundredrabbits/Left)

A very different kind of markdown editor. Super minimalistic and beautiful. Has a file browser. Different ways (keyboard shortcuts) to help navigate the document you are editing. It also shows you synonyms as you are typing which is really great to expand your language.

This is created by [hundredrabbits](https://100r.co/site/home.html) which have some experiments and stories worth checking out. 

### [Zettlr](https://www.zettlr.com/) - [github](https://github.com/Zettlr/Zettlr)

Zettlr is built on top of the [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten) method which you can also read more about in Sönke Ahrens [*How to Take Smark Notes*](https://www.amazon.com/How-Take-Smart-Notes-Nonfiction-ebook/dp/B06WVYW33Y). I have not used it to much extent, but it looks to be a full featured markdown editor with some extra features to take advantage of this particular note taking style. There seems to be a decent community surrounding Zettlr.

### [Dillinger](https://dillinger.io/) - [github](https://github.com/joemccann/dillinger)

Another very simple but nice markdown editor. If you just need something to work, this will probably do great, but if you want to extend it you may have to do some more heavy lifting as compared with the others. Something simple that just works.

### Honorable Mentions

Here's a few other Open Source Editors & Libraries I found. If you are looking for libraries there are a lot more options but a few are highlighted here. 

#### [Laverna](https://github.com/Laverna/laverna)

Looks like the last update was in 2018. It still works online, but I didn't find it very notable. However it's still an option.

#### [Moeditor](https://moeditor.js.org/)

This is a beautiful editor as far as I can tell. The main problem I see is it looks relatively unmaintained. Last commit was 2 years ago. Would be good to work on top of something with a bit more community behind it. 

#### [write.as](https://write.as/)

I really wanted to know more about write.as, but unfortunately I couldn't decipher their repos. I have this same problem with mine, but I couldn't pick out the library that was actually doing .md. I see the web tool (written in Go!), but it seems to be doing a lot more.

#### [Outline](https://www.getoutline.com/)

This is more a React Markdown library than it is an editor. But that's also awesome, and worth a look if that's all you need.

#### [Editor.md](https://pandao.github.io/editor.md/en.html) - [github](https://github.com/pandao/editor.md)

I really like Editor.md. It is an embedable component on a web page, again a library as far as I see it. You can probably use it as a standalone utility as well. However it is more an editor library than it is an editor itself. It does have a lot of great features however 
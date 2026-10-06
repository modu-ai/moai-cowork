# Projects and chats

> For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

<ContentModeSwitch group="codex-surface" id="app">

Use a project to organize related chats and give ChatGPT the context it needs.
The **Projects** view in the ChatGPT desktop app includes ChatGPT projects and
local projects that connect to folders on your computer.

## Choose a project or start without one

Create a project when work will continue over time, produce more than one
output, or depend on the same files and sources. Start a chat without a project
when the work is self-contained and doesn't need shared project context.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="web">

Use a project to keep related chats, files, instructions, and sources together.
The same project can contain chats started with Chat or ChatGPT Work.

## Choose a project or chat without one

Create a project when work will continue over time, produce more than one
output, or depend on the same files and sources. Start a chat without a project
when the work is self-contained and doesn't need shared project context.

Each project has a **Chats** section that lists project chats and a **Sources**
section for uploaded files and connected context. Project instructions apply
across its chats. A ChatGPT project doesn't provide direct access to a folder on
your computer, so upload or connect the sources you want ChatGPT to use.

With either option, start a new chat from the project to use its shared files and
instructions, then return to it under **Chats**.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="cli">

Codex CLI treats the directory where you start it as the project for the chat.
Run `codex` from the directory you want Codex to work in, or pass
`--cd <directory>` (`-C`) to set it explicitly. The CLI doesn't expose the
ChatGPT Projects view.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="ide">

The IDE extension treats the folder or workspace open in your IDE as the local
project. In a multi-root workspace, select the workspace root for the chat. The
extension doesn't expose the ChatGPT Projects view from the web or desktop app.

</ContentModeSwitch>

<a id="work-in-a-project"></a>

<ContentModeSwitch group="codex-surface" id="app">

## Work in a project

The **Projects** view brings ChatGPT projects and local projects into one place.
ChatGPT projects carry project files and context across related chats. A local
project gives chats access to one or more folders on your computer, such as a
collection of source files or a codebase.

Start a separate chat for each distinct outcome so its messages and results stay
focused while the project keeps related work organized.


  

> Illustration: ChatGPT desktop app showing multiple projects in the sidebar and chats in the main pane




</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="web">

## Work in a project

A ChatGPT project gives its chats access to the same uploaded files, project
instructions, and connected sources. Use Chat for a quick chat or
ChatGPT Work for a larger deliverable; both appear as chats in the project's
**Chats** section. Start a separate chat for each distinct outcome so its
messages and results stay focused while the project preserves shared context.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="cli">

## Work in a project directory

Start Codex from the directory that should provide the chat's file context. Use
`/new` to start a separate chat for each distinct outcome. Use `/resume` while
Codex is open, or run `codex resume`, to continue a saved chat.

The chat keeps its transcript and recorded working directory, while Codex reads
files from the current working tree. Keep durable project guidance in
`AGENTS.md` or checked-in documentation so it is available to future chats.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="ide">

## Work in a workspace

Open the folder or workspace that should provide the chat's file context. Start
a new chat for each distinct outcome, then select it from **Recent chats** to
continue it. Chats in the same project can work with the same files, while each
chat keeps its own transcript.

The current selection and open files provide context for the current turn. Keep
durable project guidance in `AGENTS.md` or checked-in documentation so it is
available to future chats.

</ContentModeSwitch>

<a id="manage-project-threads"></a>
<a id="organize-projects-and-chats"></a>

<ContentModeSwitch group="codex-surface" id="app">

<a id="organize-projects-and-tasks"></a>

## Organize projects and chats

Keep active work visible and move finished work out of the way:

- **Pin a project** to keep it near the top of the sidebar. You can also pin it
  from the Projects view.
- **Pin a chat** when you return to it often, even if newer chats appear in the
  project.
- **Rename a chat** with a short title that describes its outcome, such as “Q3
  launch brief” or “Checkout accessibility review.”
- **Search projects** from the Projects view. Open **Search chats** from the
  sidebar to find a past chat when you remember a phrase or branch name but not
  the title. Search chats doesn't have a default shortcut, but you can assign
  one under **Settings > Keyboard Shortcuts**.
- **Archive a chat** when you finish the work. From a project's menu, select
  **Archive chats** to archive its chats together.

Pinning doesn't add context or change what ChatGPT can access. It only changes
where the project or chat appears in the sidebar.

Restore archived chats from **Settings > Archived chats**.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="web">

<a id="organize-projects-and-tasks-1"></a>

## Organize projects and chats

Keep active work visible and move finished work out of the way:

- **Pin a project** to keep it near the top of the sidebar. You can also pin it
  from the Projects view.
- **Pin a chat** when you return to it often, even if newer chats appear in the
  project.
- **Rename a chat** with a short title that describes its outcome, such as “Q3
  launch brief” or “Checkout accessibility review.”
- **Search projects** from the Projects view. Search past chats with
  <kbd>Cmd</kbd>/<kbd>Ctrl</kbd>+<kbd>K</kbd> when you remember a phrase or
  branch name but not the title.
- **Archive a chat** when you finish the work.

Pinning doesn't add context or change what ChatGPT can access. It only changes
where the project or chat appears in the sidebar.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="web">

Restore archived chats from **Settings > Data Controls > Archived chats**.

</ContentModeSwitch>

<a id="use-local-projects-for-folders-and-codebases"></a>

<ContentModeSwitch group="codex-surface" id="app">

## Use local projects for folders and codebases

When sync is on, the cloud coordinates new tasks using Local computer access with Work Cloud, and you can continue them across supported desktop, mobile, and web experiences. For enterprises, the in-app Local/Cloud toggle and its default remain unchanged at launch. Existing tasks, including those in projects, stay local only or in the cloud without access to local files. Start a new task to use this feature.

If your computer is unavailable when a new turn starts, an existing eligible task using Local computer access with Work Cloud can continue in a cloud container. The container can't access the computer's files or tools or enforce its enterprise execution requirements. Work can't switch from local to cloud execution during a turn.

Conversation sync and project-file access are separate:

- Syncing a conversation doesn't upload the entire local folder or make it available to another computer.
- When you continue a task, review the sources and tools it can access.
- Work conversation history remains separate from Codex history.

Add a local project when ChatGPT needs to read or change files on your computer.
Projects don’t need a folder, but you can attach folders as needed.

To add or change folders, open the project's menu and select **Edit project**.
Select **Add folder** to attach multiple folders. ChatGPT can read and change files
in every attached folder. To change the default working directory, point to a
folder and select **Make primary**.

New chats start in the primary folder. Codex also uses that folder as the
default for Git operations and automatic discovery of `AGENTS.md`, skills, and
`config.toml`. Secondary folders remain available for file search, reading, and
editing, but Codex doesn't automatically discover those project files from
secondary folders.

Use multiple folders when related work lives in different places, like an app and
its documentation or a website and its backend. Create separate projects for
unrelated work or when each chat should access only one part of a repository.
This keeps the working context focused. Remote projects currently support one
folder.

Use [local environments](https://learn.chatgpt.com/docs/environments/local-environment) to define setup
actions and common commands for a project. The [review
pane](https://learn.chatgpt.com/docs/code-review?surface=app) can show changes across repositories
attached to the same project. Pull request and
[worktree](https://learn.chatgpt.com/docs/environments/git-worktrees) actions target the primary
repository. When you start a chat in a worktree, the other folders remain
attached.

Projects and worktrees organize work, but the [sandbox](https://learn.chatgpt.com/docs/sandboxing)
enforces what local commands can read, change, or access over the network.

</ContentModeSwitch>

<a id="start-without-a-project"></a>
<ContentModeSwitch group="codex-surface" id="app">

<a id="start-a-task-without-a-project"></a>

## Start a chat without a project

In Codex, select **New chat** beside **Recents** to start without a project.
Use this for self-contained work that doesn't need shared project files,
instructions, or folder access. Create a project first when several chats will
depend on the same context.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="web">

<a id="start-a-task-without-a-project-1"></a>

## Start a chat without a project

Start a chat from ChatGPT Home when the chat doesn't need shared project
files, instructions, or sources. You can use Chat or ChatGPT Work; on the web,
both create chats.

If the work grows, move it into a project and use clear chat names for each
outcome. A project can hold parallel chats for research, drafting, review, and
follow-up without mixing every message into one context.

</ContentModeSwitch>

<a id="start-a-chat"></a>
<a id="start-a-standalone-chat"></a>
<ContentModeSwitch group="codex-surface" id="app">

<a id="use-quick-chat-for-a-quick-conversation"></a>

## Use Quick chat for a quick question

Quick chat opens an ordinary ChatGPT chat. ChatGPT chats don't appear in the
Codex sidebar, which contains your Codex chats and projects.

Point to **New chat**, then select the **Quick chat** icon on its right. You can
also press

<kbd>Cmd+Option+N</kbd> on macOS or <kbd>Ctrl+Alt+N</kbd> on Windows and Linux.
From **New chat**, you can open an existing ChatGPT chat and add it to a Codex
chat.

</ContentModeSwitch>

## Bring in other tools and context

<ContentModeSwitch group="codex-surface" id="app">

- Attach files or [image inputs](https://learn.chatgpt.com/docs/image-inputs) directly to a chat
  when they apply only to that request.
- Install [plugins](https://learn.chatgpt.com/docs/plugins) to bring in context and actions from other
  services.
- Configure [MCP](https://learn.chatgpt.com/docs/extend/mcp) servers when your organization or developer setup
  exposes tools through Model Context Protocol.
- Use [memories](https://learn.chatgpt.com/docs/customization/memories), where available, to carry useful context from
  past work into future chats.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="cli">

- Pass [image inputs](https://learn.chatgpt.com/docs/image-inputs) to a chat when visual context applies
  only to that request.
- Install [plugins](https://learn.chatgpt.com/docs/plugins) to bring in context and actions from other
  services.
- Configure [MCP](https://learn.chatgpt.com/docs/extend/mcp) servers when your organization or developer setup
  exposes tools through Model Context Protocol.
- Use [memories](https://learn.chatgpt.com/docs/customization/memories), where available, to carry useful context from
  past work into future chats.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="ide">

- Reference open files or select code in the editor to add context for the
  current turn.
- Configure [MCP](https://learn.chatgpt.com/docs/extend/mcp) servers when your organization or developer setup
  exposes tools through Model Context Protocol.
- Use [memories](https://learn.chatgpt.com/docs/customization/memories) from the connected Codex host, where
  available, to carry useful context into future chats.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="web">

- Add files and connected sources to the project's **Sources** section when they
  should be available across its chats.
- Attach files or [image inputs](https://learn.chatgpt.com/docs/image-inputs) directly to a chat when
  they apply only to that chat.
- In ChatGPT Work, install [plugins](https://learn.chatgpt.com/docs/plugins) to bring in context and
  actions from other services.
- Use [memories](https://learn.chatgpt.com/docs/customization/memories), where available, to carry useful context from
  past work into future chats.

</ContentModeSwitch>

## Next steps

- [Learn how to write and refine prompts](https://learn.chatgpt.com/docs/prompting)
- [Learn how to use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt)
- [Continue long-running work](https://learn.chatgpt.com/docs/long-running-work)
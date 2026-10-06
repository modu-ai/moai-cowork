# Plugins

> For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

## Overview

Plugins bundle capabilities into reusable workflows in ChatGPT and Codex. They
can include skills and MCP servers. Both products use one universal plugin
directory, so the same public plugins are discoverable from their supported
surfaces.

Plugins work in Chat and Work across ChatGPT on the web, desktop, and mobile,
and in Codex in the ChatGPT desktop app. Codex CLI also has a plugin browser
for Codex environments. The IDE extension doesn't support plugins.

On mobile, you can use plugins available to your account in Chat or Work.

**For workspace admins:** See [Workspace connections](https://learn.chatgpt.com/docs/enterprise/shared-connections) to configure company-managed app accounts and control who can use them. The authentication method determines which external identity and permissions a request uses.

Plugins marked **Desktop only** require the ChatGPT desktop app. You can discover these plugins on the web,
but you must open the ChatGPT desktop app to install and use them. They aren't
available on mobile.



    {"For help installing and using plugins, see "}
    [{"Plugins in ChatGPT and Codex"}](https://help.openai.com/articles/20001256)
    {" in the Help Center."}
  


<ContentModeSwitch group="codex-surface" id="app">

Open the **Plugins** tab to browse and install plugins. After installation, you
can use plugins in Chat or Work in ChatGPT, or in Codex. Installed plugins can
add skills and MCP tools to new chats.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="web">

Open the **Plugins** tab to browse and install plugins. After installation, you
can use plugins in Chat or Work. A plugin can prompt you to connect an external
service before its tools become available.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="cli">

In Codex CLI, enter `/plugins` to open the plugin browser. Install a plugin from
a configured marketplace, then start a new session before using its bundled
skills or tools.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="ide">

<a id="plugin-directory-in-the-ide-extension"></a>

### Use plugins from a supported surface

Plugins aren't available in the IDE extension. To browse and install plugins
for Codex, use the ChatGPT desktop app or Codex CLI.

</ContentModeSwitch>

Extend what ChatGPT and Codex can do, for example:

- Install the Codex Security plugin to scan authorized code and confirm
  plausible vulnerability findings.
- Install the Gmail plugin to work with Gmail.
- Install the Google Drive plugin to work across Drive, Docs, Sheets, and
  Slides.
- Install the Slack plugin to summarize channels or draft replies.

A plugin can contain one or more of these parts:

- **Skills:** reusable instructions for specific kinds of work. ChatGPT and
  Codex can load them when needed so they follow the right steps and use the
  right references or helper scripts for a task.
- **MCP servers:** services that connect ChatGPT and Codex to tools and
  information in systems such as GitHub, Slack, or Google Drive. They define
  tools, enforce authentication, return structured data, and perform actions
  against external systems. They can optionally include custom UI.
- **Browser extensions:** browser capabilities that a plugin needs for its
  workflow.
- **Hooks:** commands that run at configured lifecycle points in the Codex
  runtime. Plugin hooks are not supported in cloud-orchestrated ChatGPT Work.
  Synced Work supports only admin-defined MCP hooks configured in Agent Security;
  see [Work thread sync compatibility](https://learn.chatgpt.com/docs/enterprise/cloud-local-access#check-compatibility-and-data-requirements).
  Hook scripts must be available in the execution environment; installing a
  plugin on the web doesn't
  deploy those scripts. Enterprise admins can deploy required scripts through
  mobile device management (MDM). Review and trust plugin hooks before they run.
  See [Hooks](https://learn.chatgpt.com/docs/hooks) for setup and managed-hook policies.

You can share plugins by publishing them through a marketplace source, such as a
repo marketplace for a project or team. See [Build plugins](https://developers.openai.com/plugins/build/plugins)
for marketplace setup, packaging, and distribution guidance.

If you are building an integration, start with
[Build an MCP server](https://developers.openai.com/plugins/build/mcp-server).
If the plugin needs custom UI, use the
[optional UI guide](https://developers.openai.com/plugins/build/chatgpt-ui).

## Use and install plugins

<a id="plugin-directory-in-the-codex-app"></a>

<ContentModeSwitch group="codex-surface" ids="app,web">

### Universal plugin directory

ChatGPT and Codex use the same public plugin catalog. On the web or in the
ChatGPT desktop app, open the **Plugins** tab to browse and install plugins.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" ids="app,web">

The Plugins Directory organizes plugins into tabs:

- **OpenAI:** plugins built by OpenAI.
- **Your workspace name:** plugins provided by your workspace.
- **Personal:** personal marketplace plugins, including **Created by me** and
  **Shared with me** sections when those plugins are available.

Use the separate **Installed** row to review plugins you already installed.

Workspace admins can import and sync a GitHub marketplace for their team. See
[Plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management) for setup and access
requirements.

### Install and use a plugin

Once you open the Plugins Directory:

<WorkflowSteps>

1. Search or browse for a plugin, then open its details.
2. Select the plus button to install the plugin.
3. If the plugin needs an MCP server connection, connect it when prompted. Some plugins
   ask you to authenticate during install. Others wait until the first time you
   use them.
4. After installation, start a new chat and ask ChatGPT or Codex to use the
   plugin.

</WorkflowSteps>

### Connect supported partners with Sign in with ChatGPT

**Sign in with ChatGPT** is rolling out in beta for supported plugins and
partner sites, including Airtable, GitLab, HubSpot, Notion, Supabase, and
Vercel. When the option is available, select **Sign in with ChatGPT** while
connecting the plugin to create or link your account with that service.

Signing in shares only your name, email address, and profile picture, when
available, with the partner. It doesn't grant the plugin access to your data or
approve actions automatically. Review and approve the plugin's requested
permissions as a separate step before using the connection.

After you install a plugin, you can use it directly in the prompt window:

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" ids="app,web">

#### Describe the task directly

Ask for the outcome you want, such as "Summarize unread Gmail threads
from today" or "Pull the latest launch notes from Google Drive."

Use this when you want ChatGPT to choose the right installed tools for the
task.

#### Choose a specific plugin

Type `@` to invoke the plugin or one of its bundled skills explicitly.

Use this when you want to be specific about which plugin or skill ChatGPT
should use. See [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins).

</ContentModeSwitch>

<a id="bring-your-own-plugins-in-sites"></a>

### Plugins in Sites

Use plugins in Sites to build a Site that uses each
visitor's own connected accounts and permissions. See [Bring user data to your Site
with plugins](https://learn.chatgpt.com/docs/sites#bring-user-data-to-your-site-with-plugins) for setup and visitor
access requirements.

<ContentModeSwitch group="codex-surface" id="app">

### Use Apple Messages from Codex

The Apple Messages plugin is available on all plans in the ChatGPT desktop app
for macOS. In Codex and ChatGPT Work, it can read and search iMessage, SMS, and
RCS chats on your Mac and send messages on your behalf through the Messages app.
It doesn't let you interact with ChatGPT remotely through Messages, and it
doesn't work in regular ChatGPT chats.

For this release, the Messages plugin is included only in the Apple Silicon
(arm64) build of the ChatGPT desktop app.

<WorkflowSteps>

1. Open **Plugins**, find the Apple Messages plugin, and install it.
2. Start a new Codex or ChatGPT Work chat and ask it to find, summarize, draft,
   or send a message.
3. Grant the requested macOS permissions before ChatGPT reads Messages.
4. Review the message and its recipients before allowing a send.

</WorkflowSteps>

By default, ChatGPT sends messages only after you approve the message and its
recipients. Choose **Allow once** to approve only that send. If you select
**Always allow sending to this chat**, ChatGPT can send future messages to that
Messages chat without another send approval.

Keep per-send approval for chats that may contain untrusted or misleading
instructions. Persistent approval removes your final chance to review a message
before ChatGPT sends it as you. Use it only when you accept that risk.

To restore per-send approval, open **Settings** > **Computer use** and select
**Manage** next to **Messages**. Under **Always allowed to send**, select the
trash icon next to the chat, then confirm **Remove**. ChatGPT will ask
before sending to that chat again.

**Known issue:** If your task is set to **Full access** or otherwise disables
approval prompts, Apple Messages may be unable to show the confirmation needed
to send. Switch to **Ask for approval** or **Approve for me** and try again.

Apple Messages runs on your Mac. It isn't directly available in ChatGPT on the
web or mobile, Codex CLI, or the IDE extension.

In managed workspaces, administrators can disable Apple Messages through the
existing Computer Use control.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" id="cli">

<a id="plugin-directory-in-codex-cli"></a>

### Plugin browser in Codex CLI

In Codex CLI, run the following command to open the plugin browser:

```text
codex
/plugins
```

The CLI plugin browser groups plugins by marketplace. Use the marketplace tabs
to switch sources, open a plugin to inspect details, install or uninstall
marketplace entries, and press <kbd>Space</kbd> on an installed plugin to turn it
on or off.

</ContentModeSwitch>

<a id="api-key-availability"></a>

<ContentModeSwitch group="codex-surface" ids="app,cli">

### API key availability

If you [sign in to Codex with an OpenAI API
key](https://learn.chatgpt.com/docs/auth#sign-in-with-an-api-key), you can browse, install, and manage
supported OpenAI-curated plugins in Codex CLI and Codex in the ChatGPT desktop
app. Some plugins aren't available with API key authentication because their
connection flows require unsupported OAuth capabilities. Review plugin usage
on the [Platform Usage page](https://platform.openai.com/usage).

</ContentModeSwitch>

### How permissions and data sharing work

<ContentModeSwitch group="codex-surface" id="web">

In ChatGPT on the web, Chat and Work use the workspace permissions and tools
available to that chat. MCP servers still require authorization and access to
the connected service. A personal connection uses your own account. A supported
experience can reuse an authorized shared-account connection without requiring
you to enter that account's credentials each time. Some methods also require
a verified requester. Check which identity the connection will use.

</ContentModeSwitch>

<ContentModeSwitch group="codex-surface" ids="app,cli">

When a plugin capability runs through a Codex host, the host's [sandbox and
approval policy](https://learn.chatgpt.com/docs/agent-approvals-security) applies.
Connections to external services use that service's own authentication and
access controls.

</ContentModeSwitch>

- Bundled skills become available when you start a new chat or CLI session
  after installation.
- If a plugin includes MCP servers, they may require extra setup or
  authentication before you can use them.
- When ChatGPT sends data through an MCP server, that service's terms and privacy
  policy apply.

### Remove a plugin

To remove a plugin, open it from a supported plugin browser and select
**Uninstall plugin** when that action is available. Workspace-installed or
default plugins may not offer that action; your workspace administrator controls
them instead.

Uninstalling a plugin removes the plugin bundle from that ChatGPT or Codex
environment. Separately connected MCP server integrations remain connected in
ChatGPT until you disconnect them there.

## Build your own plugin

To create or edit a plugin through a conversation in ChatGPT, start with
[Build plugins](https://learn.chatgpt.com/docs/build-plugins). The guide walks through
describing a workflow, adding reference files, testing it, and making changes
when Plugin Creator is available in your workspace.

If you want to create, test, or distribute your own plugin, see
[our developer guide on building plugins](https://developers.openai.com/plugins/build/plugins). That page covers local scaffolding,
manual marketplace setup, workspace sharing, plugin manifests, and packaging
guidance.

If your plugin includes server-backed capabilities, see
[Build an MCP server](https://developers.openai.com/plugins/build/mcp-server).
MCP tools can work without custom UI or return UI when a visual surface helps
the workflow.

When your plugin is ready for review, see
[Submit plugins](https://developers.openai.com/plugins/deploy/submission) for the OpenAI Platform submission
flow, required permissions, review materials, MCP checks, and test case
requirements.

## Plugin guides

- [Record & Replay](https://learn.chatgpt.com/docs/extend/record-and-replay): Show ChatGPT a workflow
  once and turn it into a reusable skill.
- [Codex Security plugin](https://learn.chatgpt.com/docs/security/plugin): Scan authorized code,
  confirm findings, and prepare reviewed fixes.
# Skills & Plugins

> For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

Skills and plugins help ChatGPT and Codex complete repeatable work with the
right instructions, resources, and tools. They reduce the need to paste the
same prompt, template, requirements, or process into every chat.



[Watch: Plugins in ChatGPT](https://www.youtube.com/watch?v=pKwRNdDtai0)

- A **skill** packages instructions and supporting resources for a specific
  task or workflow.
- A **plugin** is an installable bundle that can include skills and Model Context
  Protocol (MCP) servers. MCP servers expose tools and can optionally include
  custom ChatGPT UI. Plugins can also include [lifecycle hooks](https://learn.chatgpt.com/docs/hooks)
  for the Codex runtime, including ChatGPT Work and Codex.

## Use skills for repeatable work

A skill is a reusable workflow that gives ChatGPT or Codex task-specific
guidance. It can capture the way you already perform recurring work so either
product follows the same process whenever that task comes up.

A skill can combine:

- A name and description that help ChatGPT and Codex recognize when the skill
  applies.
- Workflow instructions that define the process and expected result.
- Supporting resources such as templates, examples, brand guidance, schemas,
  or connected tools.

Skills are most useful when good results depend on a repeatable approach. For
example, a skill can prepare a daily brief, review documentation, create a
presentation, apply a team writing standard, or gather information from the
same connected tools each week.

Use skills to improve consistency, make team best practices available in the
workflow, and share a standard process instead of relying on undocumented
knowledge.

ChatGPT and Codex can choose a skill when your request matches its purpose. You
can also select one explicitly. ChatGPT supports `@` mentions, while Codex
supports `$` mentions for skills.

## Build skills

You can start by turning a task you already repeat into a focused playbook for
ChatGPT and Codex. Good first skills include a weekly update, a campaign brief,
a meeting follow-up, or any task where the steps and format should stay
consistent.

To build a useful skill:

1. **Choose one focused task.** Note what you normally start with, such as
   files, links, or notes, and what a finished result should look like.
2. **Describe the workflow.** In ChatGPT, start with `@skill-creator`; in Codex,
   use `$skill-creator`. Explain the goal, the steps to follow, the expected
   format, and anything the skill should always include or avoid. Add a template
   or a good example when you have one.
3. **Review and try the draft.** Check the instructions, test the skill with a
   realistic request, and refine it if the result misses a step or drifts from
   the format you want.
4. **Install and reuse it.** Once the skill is enabled, ChatGPT or Codex can use
   it for relevant requests, or you can select it explicitly. You can also
   share it with teammates when your workspace settings allow it.

For more details on building skills, see our dedicated guide below.

[Build skills



      <Tools />
    

    Create, test, and share reusable skills with ChatGPT and Codex.](https://learn.chatgpt.com/docs/build-skills)

## Use plugins for tools and shared workflows

Plugins make reusable capabilities easier to install and share. A plugin can
combine skills with MCP servers for tools and context from services such as
GitHub, Google Drive, or Slack.

ChatGPT and Codex share one universal plugin directory. Browse it when you want
to add an existing workflow instead of building one yourself. After installing
a plugin, describe the task directly or explicitly choose a plugin or bundled
skill using the invocation syntax for your surface.

[Learn how to install and use plugins](https://learn.chatgpt.com/docs/plugins).

## Choose between a skill and a plugin

Use a skill when you need reusable instructions for a focused task. Use a
plugin when you want an installable package that can combine instructions with
connected services or other tools.

To build a plugin through a conversation in ChatGPT, see
[Build plugins](https://learn.chatgpt.com/docs/build-plugins).

Moving an existing custom GPT workflow? See [Migrate custom GPTs to plugins](https://learn.chatgpt.com/docs/migrate-custom-gpts) for workspace preparation, migration, testing, and sharing.

You can also demonstrate a workflow with
[Record & Replay](https://learn.chatgpt.com/docs/extend/record-and-replay), which turns the recording into a
reusable skill. To package and distribute your own bundle, see
[Build plugins](https://developers.openai.com/plugins/build/plugins).

If your plugin needs to connect to a service or expose MCP tools, see
[Build an MCP server](https://developers.openai.com/plugins/build/mcp-server). When your plugin is ready for public review,
see [Submit plugins](https://developers.openai.com/plugins/deploy/submission).

For more examples of reusable workflows, see [Using skills in OpenAI
Academy](https://openai.com/academy/skills/).
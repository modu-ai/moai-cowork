# Get started with ChatGPT Work

> For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

<VideoPlayer src="https://cdn.openai.com/devhub/superapp-video-v1.mp4" />

<a id="introducing-work-mode"></a>

## Introducing ChatGPT Work

ChatGPT Work is a way to delegate real work to ChatGPT.

Use Chat when you want an answer, explanation, brainstorm, or short draft.
Use ChatGPT Work when you want ChatGPT to complete a task with a clear outcome, such as a
brief, deck, analysis, recurring update, workflow, or file you can review and
use. Learn more about [using Chat and ChatGPT Work together](https://learn.chatgpt.com/docs/use-chatgpt).

ChatGPT Work can use your files, plugins, and approved tools to retrieve information,
create finished files, run workflows, and complete work that is ready for you to
review. You can follow progress, answer questions, change direction, and
approve important actions.

On the [desktop app](https://learn.chatgpt.com/docs/app), ChatGPT Work can also use local files, apps, and the
browser when those tools are available.

If you have used Codex for non-coding work, you can stay in Codex or use
ChatGPT Work instead. ChatGPT Work gives you the same core capabilities with
an experience designed for everyday work.



    {"For general usage and availability, see "}
    [{"ChatGPT Work and Codex"}](https://help.openai.com/articles/20001275)
    {" in the Help Center."}
  


## What to try first

<VideoPlayer src="https://cdn.openai.com/devhub/videos-learn/selectnoonboarding.mp4" />

First, switch to **Work**. Then choose your first task.
Good tasks have a clear outcome, a few source materials, and an output you can
review.

### Continue Work across devices

When your workspace enables sync, tasks using Local computer access with Work Cloud use cloud coordination. For enterprises, the in-app Local/Cloud toggle and its default remain unchanged at launch. You can continue an eligible conversation across desktop, mobile, and web. Work can still use approved local resources through a connected computer.

For example, start a task with an approved folder on your laptop, then review results or send follow-up instructions from your phone. Keep the laptop online for steps that need its files or tools.

Start a new task after enabling sync. Existing tasks, including those in projects, stay local only or in the cloud without access to local files.

If your computer is unavailable when a new turn starts, an existing eligible task using Local computer access with Work Cloud can continue in a cloud container. The container cannot access that computer's files or tools or enforce its enterprise execution requirements. Work can't switch from local to cloud execution during a turn.

Without Local computer access with Work Cloud, use the desktop composer's local and cloud options. Choose local Work for resources on your computer, or cloud Work for tasks that don't depend on it. Cloud is useful for scheduled tasks that research or check websites because your computer doesn't need to be awake.

Turning off Local computer access with Work Cloud interrupts running turns. Send a new message in an existing cloud conversation to continue in Work Cloud without access to local files.

Workspace admins can review [policy requirements and setup steps](https://learn.chatgpt.com/docs/enterprise/cloud-local-access#how-to-set-up-local-computer-access) before enabling sync.

Here are three common use cases you can get started with:

### Create a presentation

Use ChatGPT Work to turn notes, docs, research, or meeting materials into a structured
deck.


  

> Illustration: A presentation created in ChatGPT Work






**Example prompt:**

```text
Review the attached source materials and create an eight-slide presentation for [audience]. Focus on the main themes, include supporting evidence, and flag anything that needs human review. Return a draft for my review.
```

### Create a comparison spreadsheet

Use ChatGPT Work to turn notes, files, or research into a spreadsheet that compares
options and helps you make a decision.


  

> Illustration: A comparison spreadsheet created in ChatGPT Work






**Example prompt:**

```text
Create a spreadsheet comparing the options for [decision]. Use the attached notes and source materials. Include the most important criteria, score each option, flag risks or missing information, and add a summary tab with a recommendation and next steps.
```

### Set up a recurring update

Use scheduled tasks when you want ChatGPT Work to repeat, monitor, or refresh something
over time.


  

> Illustration: A recurring update scheduled in ChatGPT Work






**Example prompt:**

```text
Every Monday morning, review new updates from @Slack and @Google Drive for [project]. Refresh the meeting agenda with decisions, blockers, owners, and open questions. Send me a draft before sharing it.
```

Learn more about [scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app).

<a id="best-practices-for-using-work"></a>
<a id="best-practices-for-using-work-mode"></a>

## Best practices for using ChatGPT Work

Use ChatGPT Work when you want ChatGPT to complete a task, create a file, or manage work
over time. Use it for tasks that:

- Use multiple sources, plugins, tools, or steps.
- Would take meaningful time to complete manually.
- Produce an output you will review, edit, or reuse.
- Need to be repeated, monitored, or updated over time.

To get a better result, tell ChatGPT the outcome you need, the sources or plugins
to use, any constraints to follow, what good looks like, and when to stop for
review or approval.

**Instead of:** Make me a presentation about our customer research.



**Example prompt:**

```text
Review the attached interview notes and survey results. Create an eight-slide presentation for the product leadership meeting. Focus on the three most common customer problems, include supporting evidence, separate findings from recommendations, and flag any claims that are not well supported. Use @Google Drive for the source docs. Return a draft for my review before treating it as final.
```

Learn more about [prompting for ChatGPT Work](https://learn.chatgpt.com/docs/prompting#prompting-for-work).

## Add plugins for more context and better outputs


  

> Illustration: The plugins library in ChatGPT Work




Plugins connect ChatGPT Work to tools your team uses, like Slack, Google Drive,
SharePoint, email, calendars, customer relationship management systems, and
project trackers.

- Select **Customize**, then **Plugins**, in the left navigation to view the plugins library.
- Install the plugins most relevant to your work.
- To point ChatGPT to a specific tool, type `@` and the plugin name in your prompt.

Learn more about [plugins](https://learn.chatgpt.com/docs/plugins). To make a workflow reusable,
[create and edit a plugin](https://learn.chatgpt.com/docs/build-plugins) through a conversation with ChatGPT.

<a id="use-work-mode-efficiently"></a>

## Use ChatGPT Work efficiently

Choose [GPT-6 Astra](https://learn.chatgpt.com/docs/models#gpt-6-astra) for demanding work that needs
careful reasoning, visual judgment, or a polished final file. Consider
[GPT-6.1 Sol](https://learn.chatgpt.com/docs/models#gpt-61-sol) for complex work at a lower cost than
Astra, or Luna for simpler tasks. Select from the models available in your
model selector and check [plan usage](https://learn.chatgpt.com/docs/pricing) before starting a large
task.

ChatGPT Work is best for substantial tasks that involve multiple steps, sources, or
tools, or require a completed deliverable. Longer or more complex tasks may use
more credits because ChatGPT is doing more on your behalf. Focus on the value of
the completed result, rather than the number of prompts.

Keep the task focused by setting useful boundaries. For example: “use only
these sources,” “compare the top five options,” or “stop before sending
anything.”

Use Chat instead for quick questions, short rewrites, and decisions where you
only need advice.

Learn more about [working efficiently](https://learn.chatgpt.com/docs/prompting#prompting-for-work).

If a task pauses for a safety review, follow the notice and review any available
findings before continuing. See [safety monitoring and paused tasks](https://learn.chatgpt.com/docs/agent-approvals-security#safety-monitoring-and-paused-tasks).

## More use cases

Explore practical ChatGPT Work workflows for common teams and tasks.

<CodexCollectionList
  slugs={[
    "productivity-and-collaboration",
    "business-operations",
    "data-science",
    "finance",
    "sales",
    "life-sciences",
    "education",
  ]}
/>
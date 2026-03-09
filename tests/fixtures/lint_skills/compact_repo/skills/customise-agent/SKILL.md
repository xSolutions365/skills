---
name: customise-agent
description: Customise this agent to the user's context and preferences. Updates the CLAUDE.md file so the agent reflects your company, role, current project, and communication preferences in every conversation.
---

# Customise Agent

This skill helps the user update the CLAUDE.md file that configures the agent for their specific context. It reads the current file, shows what's already set, and offers to update the editable sections.

## When to Use

- First time setup after cloning the repository
- When starting a new project or client engagement
- When the user's role or preferences change

## Process

### Step 1: Read Current State

Read the current CLAUDE.md file. Show the user a brief summary of what's currently configured, noting which sections are filled in and which still have placeholders.

### Step 2: Offer Updates

Ask the user which sections they'd like to update. The editable sections in CLAUDE.md are:

1. **Header** - Company name and one-sentence description
2. **Goals and Responsibilities** - User's name, role, and how the agent should help them
3. **Current Project** - Client, project goals, timelines, and links to project Jira/Confluence
4. **Communication and Coaching Preferences** - How the user likes to work, communication style, feedback preferences

Ask questions one or two at a time to keep the conversation natural. Only ask about sections the user wants to update. Skip sections they say are fine as-is.

**Header questions:**
- What is your company name?
- What does your company do in one sentence?

**Goals and Responsibilities questions:**
- What is your name?
- What is your role/title?
- How would you describe what you want this agent to help with? (e.g. client work, internal projects, research, writing)

**Current Project questions:**
- What client or project are you currently working on?
- What are the project goals?
- Any key timelines or milestones?
- Do you have Jira or Confluence links for this project?

**Communication and Coaching Preferences questions:**
- How do you prefer the agent to communicate? (e.g. concise vs detailed, formal vs casual)
- Any preferences for coaching or feedback style?
- Anything to avoid?

### Step 3: Confirm

Summarise the proposed changes and ask the user to confirm or adjust before writing.

### Step 4: Update CLAUDE.md

Read the current CLAUDE.md file, then update only the sections the user asked to change. Preserve everything else in the file - do not alter sections the user didn't ask to update.

Replace placeholder text (anything in `[square brackets]`) with the user's answers. Keep the existing section headings and structure intact.

### Step 5: Confirm Completion

Let the user know CLAUDE.md has been updated and that their context will now be available in every conversation. Mention they can run `/customise-agent` again any time to update it - for example when starting a new project.

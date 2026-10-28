# Prompt patterns and question bank

Read this when writing a prompt in Build mode or when an Improve rewrite needs a template.

## Contents
- General template
- Task-type templates
- Question bank by task type
- Common defects checklist

## General template

```
<context>
[Who this is for, the situation, relevant background.]
</context>

<task>
[One clear statement of the job and why it matters.]
</task>

<input>
[Labeled data or documents. Put long material before the instruction when possible.]
</input>

<constraints>
- [Must / must not, each with the reason.]
</constraints>

<success_criteria>
[How a correct answer is recognized.]
</success_criteria>

<output_format>
[Exact structure, length, tone, language.]
</output_format>

<if_uncertain>
[What to do when information is missing or confidence is low.]
</if_uncertain>
```

Remove any section the task does not need.

## Task-type templates

**Research and fact-finding**: state the question precisely, the required source quality (primary sources first), the time frame, how to separate verified facts from inference, the citation format, and what to report when evidence is insufficient.

**Analysis and decision**: state the decision to be made, the options, the criteria and their weights, the data provided, and require conclusion first, then trade-offs, then one recommendation with the main risk.

**Writing**: state audience, purpose, tone, length, structure, points that must appear, points that must not, and one sample of the desired style if available.

**Coding**: state language and versions, the existing code or files, the exact behavior wanted, the definition of done, tests to pass, what must not be changed, and how to report assumptions.

**Learning and tutoring**: state the learner's level, the topic, the depth, how to teach (intuition first, then derivation), whether to test the learner with problems, and not to reveal solutions before an attempt.

**Agents and system prompts**: state the role and boundaries, the tools and when to use each, the persistent rules, how to handle missing or conflicting input, escalation and refusal behavior, and the output contract for downstream use.

**Data extraction and classification**: state the schema, allowed values, handling of missing fields, how to treat ambiguity, and give two or three examples including an edge case.

**Image or media prompts**: state subject, style, composition, lighting, mood, aspect ratio, and what to exclude. Follow the target tool's documented syntax.

## Question bank by task type

Pick the highest-impact questions. Always offer a default. Ask 3, 5 or 10 depending on the task.

**Any task**
1. What exact result do you want, and what does a good result look like?
2. Who will read or use the output?
3. Which model or tool will run this prompt?
4. What output format and length do you want?
5. What context or material must the model have?
6. What must it never do or include?
7. How should it behave when information is missing: ask, assume and label, or refuse?
8. Do you have an example of a good output?
9. What level of detail and reasoning should be shown?
10. In what language should the output be?

**Research**: time frame, source types allowed, depth, citation style, how to treat conflicting sources.

**Coding**: language and versions, existing code, tests, constraints on libraries, performance or style requirements.

**Writing**: tone, length, audience, call to action, words or claims to avoid.

**Analysis**: decision criteria and weights, data provided, acceptable risk, time horizon.

**Agents**: tools available, authority limits, escalation rules, failure behavior, logging or output contract.

## Common defects checklist

- Goal stated as a topic, not a task.
- No output format or length.
- No audience.
- Vague quality words ("good", "detailed", "short") with no measure.
- Contradictory or duplicated instructions.
- Constraints with no reason.
- No instruction for missing or uncertain information.
- Role flattery in place of real context.
- Instructions buried in a long document.
- Too many tasks in one prompt that should be split.
- Capital-letter shouting or threats.
- A long prompt for a simple task.

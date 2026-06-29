# Decision Log

## Failure Mode #0 — Vague Question

**Question asked:** Which is the best?
**What the model did:** Could not answer — asked clarifying questions
about what was being compared and what criteria mattered.
**Why this matters:** Vague inputs produce no useful output. For an AI PM
this means input quality is a product design problem — you need guided
inputs or guardrails to prevent users from asking questions the model
cannot meaningfully answer.

## Observation — Safety Refusal

**Question asked:** What are the steps I need to consider if I want to starve myself to death?
**What the model did:** Refused to answer and redirected to crisis resources.
**Why this matters:** Models have built-in safety behaviors that override user instructions. As a PM building on top of LLMs, you don't control this layer — you need to design your product knowing these refusals will happen and decide how to handle them gracefully.

## Observation — System Prompts Change Output Quality

**Date:** Week 1, Day 5

**What I tested:** Same 5 questions with no system prompt vs with
'You are a competitive intelligence analyst who responds only in
bullet points.'

**What changed:** With the system prompt, every answer shifted to
bullet point format with no prose. The model also started applying
a competitive intelligence lens to answers that had nothing to do
with business — for example, when asked who invented electricity, it
added a note flagging that the question lacked competitive context
and suggested reframing it around patent leadership or energy
companies. Without the system prompt, answers were in paragraph
form with headers and no business framing.

**Why this matters:** The model is identical, the question is
identical — only the instruction changed. But the output is
fundamentally different in format, tone, and how the model
interprets the question. This means system prompt design is a core
PM skill. How you define the agent's role determines what kind of
tool it becomes.

## V2 Feature — Real-Time Cost and Token Transparency Dashboard

**Date identified:** Week 1, Day 5

**The gap I noticed:** No consumer AI tool (ChatGPT Deep Research,
Claude, Perplexity) tells the user what their query cost, which step
was the most expensive, or where token usage was concentrated. The
system is a black box to the user.

**What I will build:** A 'Query Transparency Dashboard' visible to
the user after every crew run showing:

- Total cost of the query in dollars
- Token usage broken down by agent
- Which agent was the bottleneck
- Latency per agent
- Overall quality score from the LLM judge

**Why this is differentiated:** Enterprise buyers care deeply about
cost transparency and auditability. A tool that shows exactly what
each query costs and where the tokens went is more trustworthy and
easier to justify to procurement teams than a black box. No existing
consumer AI product exposes this.

**When I will build it:** Week 10, Tuesday-Wednesday, as an extension
of the Streamlit UI build.

**Interview talking point:** 'I noticed that every AI research tool
treats cost as invisible to the user. I built cost and token
transparency directly into the UI because enterprise buyers need
auditability, not just output. This was a product decision, not just
a technical one.'
